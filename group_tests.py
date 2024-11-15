import unittest

from group import groups_of_3


class UnitTests(unittest.TestCase):
    def test_groups_of_3_1(self):
        self.assertEqual(groups_of_3([1,2,3,4,5,6]), [[1,2,3],[4,5,6]])
    def test_groups_of_3_2(self):
        self.assertEqual(groups_of_3([1,2,3,4,5]), [[1,2,3],[4,5]])
    def test_groups_of_3_3(self):
        self.assertEqual(groups_of_3([]), [])