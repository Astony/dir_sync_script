import hashlib
import os
from typing import Callable, Generator, List, Tuple

from loguru import logger

from files_and_dirs_funcs import copy_file, create_dir, delete_dir, delete_file


def get_hash(file_path: str) -> bytes:
    """Get file's hash

    :param file_path: Path to file that is required to get hash
    :type file_path: str
    :return: file's hash
    :rtype: bytes
    """
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.digest()


def compare_hash(file_path1: str, file_path2: str) -> bool:
    """Compare files hash

    :param file_path1: Path to first file
    :type file_path1: str
    :param file_path2: Path to second file
    :type file_path2: str
    :return: Match between hash of two files
    :rtype: bool
    """
    return get_hash(file_path1) == get_hash(file_path2)


def sync_objects(
    source_root: str,
    rep_root: str,
    source_obj: List,
    replicas_obj: List,
    create_func: Callable,
    delete_func: Callable,
    obj_type: str,
) -> None:
    """
    Synchronize folders and files replic directory with source within one directory


    :param source_root: Path to the directory in which the synchronization will take place
    :type source_root: str
    :param rep_root: Path to the directory - source copy
    :type rep_root: str
    :param source_obj: All folders and files in the source root
    :type source_obj: List
    :param replicas_obj: All folders and files in the replic root
    :type replicas_obj: List
    :param create_func: Function that creates folder or copy file
    :type create_func: Callable
    :param delete_func: Function that deletes folder or file
    :type delete_func: Callable
    :param obj_type: Type of object that will be synchronized. It can take "dir" or "file" value
    :type obj_type: str
    :return: None
    """
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


def get_metadata(path: str) -> Tuple:
    """
    Get all metadata of root including root's directories and files

    :param path: Path to directory
    :type path: str
    :return:
    """
    for root, dirs, files in os.walk(path):
        return root, dirs, files


def sync_func(source_path: str, replic_path: str) -> None:
    """
    Synchronize all folders and files of replic directory with source

    :param source_path: Path to the directory in which the synchronization will take place
    :type source_path: str
    :param replic_path: Path to the directory - source copy
    :type replic_path: str
    :return: None
    """
    while True:

        source_root, source_dirs, source_files = get_metadata(source_path)
        rep_root, rep_dirs, rep_files = get_metadata(replic_path)
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
        break
