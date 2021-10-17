import hashlib
import os

from loguru import logger

from files_and_dirs_funcs import copy_file, create_dir, delete_dir, delete_file


def get_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.digest()


def compare_hash(file_path1, file_path2):
    return get_hash(file_path1) == get_hash(file_path2)


def sync_objects(
    source_root, rep_root, source_obj, replicas_obj, create_func, delete_func, obj_type
):
    for obj in replicas_obj:
        if obj not in source_obj:
            delete_func(source_root, rep_root, obj)
        elif obj_type == "file" and not compare_hash(
            source_root + "/" + obj, rep_root + "/" + obj
        ):
            logger.info(
                f"Mismatch between replic file {rep_root + '/' + obj} and source file "
                f"{source_root + '/' + obj} was detected"
            )
            delete_func(source_root, rep_root, obj)
            create_func(source_root, rep_root, obj)
    for obj in source_obj:
        if obj not in replicas_obj:
            create_func(source_root, rep_root, obj)


def get_metadata(path):
    for root, dirs, files in os.walk(path):
        yield root, dirs, files


def sync_func(source_path, replic_path):
    source_metainfo_gen = get_metadata(source_path)
    rep_metainfo_gen = get_metadata(replic_path)

    while True:
        try:
            source_root, source_dirs, source_files = next(source_metainfo_gen)
            rep_root, rep_dirs, rep_files = next(rep_metainfo_gen)
            sync_objects(
                source_root,
                rep_root,
                source_dirs,
                rep_dirs,
                create_dir,
                delete_dir,
                obj_type="dir",
            )
            sync_objects(
                source_root,
                rep_root,
                source_files,
                rep_files,
                copy_file,
                delete_file,
                obj_type="file",
            )
            for dir in source_dirs:
                sync_func(source_root + "/" + dir, rep_root + "/" + dir)
        except StopIteration:
            break
