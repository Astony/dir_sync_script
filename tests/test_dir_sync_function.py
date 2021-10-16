from sync_func import compare_hash, sync_func, sync_objects


def test_compare_hash_func(create_files):
    assert not compare_hash("tests/file1.txt", "tests/file2.txt")
    assert compare_hash("tests/file1.txt", "tests/file3.txt")
