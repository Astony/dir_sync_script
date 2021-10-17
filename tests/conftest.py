import os
import shutil

import pytest


def create_file(path: str, content: str):
    """Create txt file with specific content"""
    with open(f"{path}", "w") as file:
        file.write(content)


@pytest.fixture
def create_files():
    """Create files with equal or non-equal content"""
    create_file("tests/file1.txt", "hello, world")
    create_file("tests/file2.txt", "hello, world!")
    create_file("tests/file3.txt", "hello, world")
    yield
    os.remove("tests/file1.txt")
    os.remove("tests/file2.txt")
    os.remove("tests/file3.txt")


@pytest.fixture
def create_dirs_and_files():
    os.makedirs("tests/dir1/dir2")
    os.makedirs("tests/dir3/dir4")
    create_file("tests/dir1/file1.txt", "aaa")
    create_file("tests/dir3/file2.txt", "bbb")
    yield
    shutil.rmtree("tests/dir1")
    shutil.rmtree("tests/dir3")


@pytest.fixture
def create_nested_dirs_and_files_first_case():
    """Create common case for synch function"""
    os.makedirs("tests/source/dir1")
    os.mkdir("tests/source/dir2")
    os.mkdir("tests/source/dir3")
    create_file("tests/source/dir1/file1.txt", "abacaba")
    os.makedirs("tests/replica/dir1")
    os.mkdir("tests/replica/dir4")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_nested_dirs_and_files_second_case():
    """Create common case for synch function"""
    os.makedirs("tests/source/dir1/dir2")
    create_file("tests/source/dir1/dir2/file1.txt", "hello")
    os.makedirs("tests/replica/dir1")
    os.mkdir("tests/replica/dir4")
    create_file("tests/replica/dir4/file2.txt", "hello")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_two_different_files():
    """Create two different files"""
    os.mkdir("tests/source")
    os.mkdir("tests/replica")
    create_file("tests/source/file1.txt", "aaa")
    create_file("tests/replica/file1.txt", "bbb")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_empty_source_dir():
    """Create empty source dir and non-empty replic's one"""
    os.mkdir("tests/source")
    os.makedirs("tests/replica/dir1")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_empty_replica_dir():
    """Create empty replica dir and non-empty source one"""
    os.makedirs("tests/source/dir1/dir2")
    os.mkdir("tests/replica")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")
