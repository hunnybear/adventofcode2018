import unittest

import hb_lib.testing
import aoc_2018.day_02

PART_01_CASES = []
PART_02_CASES = []


def load_tests(_loader, _tests, _pattern):

    suite = unittest.TestSuite()

    cases = []

    for case_data in PART_01_CASES:
        cases.append(hb_lib.testing.ParameterizedCase(case_data, run_function=aoc_2018.day_02.part_01))

    for case_data in PART_02_CASES:
        cases.append(hb_lib.testing.ParameterizedCase(case_data, run_function=aoc_2018.day_02.part_02))

    suite.addTests(cases)


    return suite




