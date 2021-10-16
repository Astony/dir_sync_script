import os

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
