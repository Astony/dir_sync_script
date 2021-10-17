import os
import shutil

from loguru import logger


def delete_dir(source_root, rep_root: str, dir: str) -> None:
    """
    Delete specific directory

    :param rep_root: Root with the directory that has to be deleted
    :type rep_root: str
    :param dir: Name of directory
    :type dir: str
    :return: None
    """
    deleted_path = rep_root + "/" + dir
    shutil.rmtree(deleted_path)
    logger.info(f"directory {deleted_path} was deleted")


def create_dir(source_root, rep_root: str, dir: str) -> None:
    """
    Create specific directory

    :param rep_root: Root with the directory that has to be created
    :type rep_root: str
    :param dir: Name of directory
    :type dir: str
    :return: None
    """
    created_path = rep_root + "/" + dir
    os.mkdir(rep_root + "/" + dir)
    logger.info(f"directory {created_path} was created")


def copy_file(source_root: str, rep_root: str, file: str) -> None:
    """
    Copy file from one directory to another

    :param source_root: Root with the directory with original file
    :type source_root: str
    :param rep_root: Root with the directory where original file will be copied
    :type rep_root: str
    :param file: Name of file
    :type file: str
    :return: None
    """
    created_file = rep_root + "/" + file
    shutil.copy(source_root + "/" + file, rep_root)
    logger.info(f"file {created_file} was copied from {source_root + '/' + file}")


def delete_file(source_root, rep_root: str, file: str) -> None:
    """
    Delete specific file

    :param rep_root: Root with the file that has to be deleted
    :type rep_root: str
    :param file: Name of file
    :type file: str
    :return: None
    """
    deleted_file = rep_root + "/" + file
    os.remove(deleted_file)
    logger.info(f"file {deleted_file} was deleted")
