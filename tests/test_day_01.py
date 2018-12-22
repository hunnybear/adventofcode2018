"""
test_day_01

Tests for first day of advent of code solution.

From AOC, part 1:

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6

part 2:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.



"""

import unittest
import sys

import testing_core

import aoc_2018.day_01

PART_01_CASES = [
    testing_core.CaseParameters('+1, -2, +3, +1', 3),
    testing_core.CaseParameters('+1, +1, +1', 3),
    testing_core.CaseParameters('+1, +1, -2', 0),
    testing_core.CaseParameters('-1, -2, -3', 6)
]

PART_02_CASES = [
    testing_core.CaseParameters('+1, -1', 0),
    testing_core.CaseParameters('+3, +3, +4, -2, -4', 10),
    testing_core.CaseParameters('-6, +3, +8, +5, -6', 5),
    testing_core.CaseParameters('+7, +7, -2, -7, -4', 14)
]


def load_tests(loader, tests, pattern):

    suite = unittest.TestSuite()

    class TestCase(unittest.TestCase):

        def __init__(self, case_params, part):
            self._case_params = case_params
            self._part = part

            super(TestCase, self).__init__('runTest')

        def runTest(self):

            if self._part == 1:
                run_function = aoc_2018.day_01.part_01

            elif self._part == 2:
                run_function = aoc_2018.day_01.part_02
            else:
                self.assertFalse(True, msg="tests were improperly set up")
            res = run_function(self._case_params.input)
            self.assertEqual(res, self._case_params.result)


    suite.addTests([TestCase(case, 1) for case in PART_01_CASES])
    suite.addTests([TestCase(case, 2) for case in PART_02_CASES])

    return suite



