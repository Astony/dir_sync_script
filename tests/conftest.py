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
