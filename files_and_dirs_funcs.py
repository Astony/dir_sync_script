import os
import shutil

from loguru import logger


def delete_dir(source_root, rep_root, dir):
    deleted_path = rep_root + "/" + dir
    shutil.rmtree(deleted_path)
    logger.info(f"directory {deleted_path} was deleted")


def create_dir(source_root, rep_root, dir):
    created_path = rep_root + "/" + dir
    os.mkdir(rep_root + "/" + dir)
    logger.info(f"directory {created_path} was created")


def copy_file(source_root, rep_root, file):
    created_file = rep_root + "/" + file
    shutil.copy(source_root + "/" + file, rep_root)
    logger.info(f"file {created_file} was copied from {source_root + '/' + file}")


def delete_file(source_root, rep_root, file):
    deleted_file = rep_root + "/" + file
    os.remove(deleted_file)
    logger.info(f"file {deleted_file} was deleted")
