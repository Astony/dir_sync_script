import os
import shutil

import pytest


def create_file(path, content):
    with open(f"{path}", "w") as file:
        file.write(content)


@pytest.fixture
def create_files():
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
def create_nested_dirs_and_files():
    os.mkdir("tests/source")
    create_file("tests/source/file1.txt", "abacaba")
    os.mkdir("tests/source/dir1")
    os.mkdir("tests/source/dir2")
    os.mkdir("tests/source/dir3")
    os.mkdir("tests/replica")
    os.mkdir("tests/replica/dir1")
    os.mkdir("tests/replica/dir4")
    os.mkdir("tests/replica/dir5")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_two_different_files():
    os.mkdir("tests/source")
    os.mkdir("tests/replica")
    create_file("tests/source/file1.txt", "aaa")
    create_file("tests/replica/file1.txt", "bbb")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")


@pytest.fixture
def create_empty_source_dir():
    os.mkdir("tests/source")
    os.makedirs("tests/replica/dir1")
    yield
    shutil.rmtree("tests/source")
    shutil.rmtree("tests/replica")
