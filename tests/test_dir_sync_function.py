import os

from files_and_dirs_funcs import copy_file, create_dir, delete_dir, delete_file
from sync_func import compare_hash, sync_func, sync_objects


def test_compare_hash_func(create_files):
    assert not compare_hash("tests/file1.txt", "tests/file2.txt")
    assert compare_hash("tests/file1.txt", "tests/file3.txt")


def test_sync_dirs_in_corrent_dir(create_dirs_and_files):
    sync_objects(
        "tests/dir1", "tests/dir3", ["dir2"], ["dir4"], create_dir, delete_dir, "dir"
    )
    assert os.path.exists("tests/dir3/dir2")
    assert not os.path.exists("tests/dir3/dir4")


def test_sync_files_in_current_dir(create_dirs_and_files):
    sync_objects(
        "tests/dir1", "tests/dir3", ["dir2"], ["dir4"], create_dir, delete_dir, "dir"
    )
    sync_objects(
        "tests/dir1",
        "tests/dir3",
        ["file1.txt"],
        ["file2.txt"],
        copy_file,
        delete_file,
        "file",
    )
    assert os.path.exists("tests/dir3/file1.txt")
    assert not os.path.exists("tests/dir3/file2.txt")
