﻿import os
from random import randint

from approvaltests.string_writer import StringWriter


def test_writes_file(tmpdir):
    contents = "foo" + str(randint(0, 100)) + "\n"
    sw = StringWriter(contents)
    filename = os.path.join(str(tmpdir), "stuff.txt")
    sw.write_received_file(filename)

    with open(filename, "r") as received:
        assert contents == received.read()


def test_writes_file_to_missing_directory(tmpdir):
    contents = "foo\n"
    sw = StringWriter(contents)
    filename = os.path.join(str(tmpdir), "non_existent_folder", "./stuff.txt")
    sw.write_received_file(filename)

    with open(filename, "r") as received:
        assert contents == received.read()


def test_new_lines_with_empty_string():
    sw = StringWriter("")
    sw2 = StringWriter(None)
    assert sw.contents == sw2.contents
