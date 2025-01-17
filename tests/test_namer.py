﻿import os
import unittest

from approvaltests.namer.namer_base import NamerBase
from approvaltests.namer.stack_frame_namer import StackFrameNamer


class NamerTests(unittest.TestCase):
    def test_class(self):
        self.assertEqual("NamerTests", StackFrameNamer().get_class_name())

    def test_method(self):
        n = StackFrameNamer()
        self.assertEqual("test_method", n.get_method_name())

    def test_name_works_from_inside_an_other_method(self):
        self.an_other_method()

    def an_other_method(self):
        n = StackFrameNamer()
        self.assertEqual(
            "test_name_works_from_inside_an_other_method", n.get_method_name()
        )

    def test_file(self):
        directory = StackFrameNamer().get_directory()
        assert os.path.exists(directory + "/test_namer.py")

    def test_basename(self):
        n = StackFrameNamer()
        self.assertTrue(
            n.get_basename().endswith("NamerTests.test_basename"), n.get_basename()
        )

    def test_received_name(self):
        filename = StackFrameNamer().get_received_filename("./stuff")
        self.assertEqual(filename, "./stuff.received.txt")

    def test_approved_name(self):
        filename = StackFrameNamer().get_approved_filename("./stuff")
        self.assertEqual(filename, "./stuff.approved.txt")

    def test_alternative_extension(self):
        n = StackFrameNamer(extension=".html")
        filename = n.get_approved_filename("./stuff")
        self.assertEqual(filename, "./stuff.approved.html")


if __name__ == "__main__":
    unittest.main()
