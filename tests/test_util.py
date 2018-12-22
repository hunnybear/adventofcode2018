import unittest

import aoc_2018.util


class TestSplit(unittest.TestCase):
    def test_commas(self):

        input_val = '33, 43, 45'
        res = aoc_2018.util.split_input(input_val)

        self.assertEqual(res, ['33', '43', '45'])

    def test_whitespace(self):

        input_val = "33 43\n45"

        res = aoc_2018.util.split_input(input_val)

        self.assertEqual(res, ['33', '43', '45'])


    def test_mixed(self):

        input_val = "33,\t43\n45"

        res = aoc_2018.util.split_input(input_val)

        self.assertEqual(res, ['33', '43', '45'])
