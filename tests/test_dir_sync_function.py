import os

import pytest

from files_and_dirs_funcs import copy_file, create_dir, delete_dir, delete_file
from sync_func import compare_hash, sync_func, sync_objects


def read_files():
    """Read content of two files"""
    with open("tests/source/file1.txt", "r") as file:
        source_file_text = file.read()
    with open("tests/replica/file1.txt", "r") as file:
        replic_file_text = file.read()
    return source_file_text, replic_file_text


def test_compare_hash_func(create_files):
    """Test that compare hash function can distinguish files with equal and non-qual content"""
    assert not compare_hash("tests/file1.txt", "tests/file2.txt")
    assert compare_hash("tests/file1.txt", "tests/file3.txt")


def test_sync_dirs_in_current_dir(create_dirs_and_files):
    """Test that sync function synchronize folders within a directory"""
    sync_objects(
        "tests/dir1", "tests/dir3", ["dir2"], ["dir4"], create_dir, delete_dir, "dir"
    )
    assert os.path.exists("tests/dir3/dir2")
    assert not os.path.exists("tests/dir3/dir4")


def test_sync_files_in_current_dir(create_dirs_and_files):
    """Test that sync function synchronize files within a directory"""
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


def test_main_sync_func_common_first_case(create_nested_dirs_and_files_first_case):
    """Common case that main sync function synchronize all files between source and replica"""
    assert not os.path.exists("tests/replica/dir1/file1.txt")
    sync_func("tests/source", "tests/replica")
    assert os.path.exists("tests/replica/dir1/file1.txt")
    assert os.path.exists("tests/replica/dir2")
    assert os.path.exists("tests/replica/dir3")


def test_main_sync_func_common_second_case(create_nested_dirs_and_files_second_case):
    """Common case that main sync function synchronize all files between source and replica"""
    assert os.path.exists("tests/replica/dir4/file2.txt")
    assert not os.path.exists("tests/replica/dir1/dir2/file1.txt")
    sync_func("tests/source", "tests/replica")
    assert os.path.exists("tests/replica/dir1/dir2/file1.txt")
    assert not os.path.exists("tests/replica/dir4")


def test_updating_different_files_with_equal_names(create_two_different_files):
    """Test that two files with equal names and different content will be synchronized"""
    source_file_text, replic_file_text = read_files()
    assert source_file_text != replic_file_text
    sync_func("tests/source", "tests/replica")
    source_file_text, replic_file_text = read_files()
    assert source_file_text == replic_file_text


def test_empty_source_dir(create_empty_source_dir):
    """Test main sync function in case when source dir is empty"""
    assert os.path.exists("tests/replica/dir1")
    sync_func("tests/source", "tests/replica")
    assert not os.path.exists("tests/replica/dir1")


def test_empty_replica_dir(create_empty_replica_dir):
    """Test main sync function in case when replica dir is empty"""
    assert not os.path.exists("tests/replica/dir1/dir2")
    sync_func("tests/source", "tests/replica")
    assert os.path.exists("tests/replica/dir1/dir2")


def test_not_existing_path_case(create_two_different_files):
    """Test with non-existing path to directory"""
    with pytest.raises(IOError, match=f"Directory /tests/abacaba doesn't exists"):
        sync_func("tests/source", "/tests/abacaba")
