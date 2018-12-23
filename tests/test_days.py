"""
Streamlining this so I can not write so much gods-damned boilerplate
"""
import importlib
import unittest
import logging

import hb_lib.testing
CASE_DATA = [
    ( # Day 1
        [
            hb_lib.testing.CaseParameters('+1, -2, +3, +1', 3),
            hb_lib.testing.CaseParameters('+1, +1, +1', 3),
            hb_lib.testing.CaseParameters('+1, +1, -2', 0),
            hb_lib.testing.CaseParameters('-1, -2, -3', 6)
        ],
        [
            hb_lib.testing.CaseParameters('+1, -1', 0),
            hb_lib.testing.CaseParameters('+3, +3, +4, -2, -4', 10),
            hb_lib.testing.CaseParameters('-6, +3, +8, +5, -6', 5),
            hb_lib.testing.CaseParameters('+7, +7, -2, -7, -4', 14)
        ]
    ),
    ( # Day 2
        [hb_lib.testing.CaseParameters('abcdef,bababc,abbcde,abcccd,aabcdd,abcdee,ababab', 12)],
        [hb_lib.testing.CaseParameters('abcde,fghij,klmno,pqrst,fguij,axcye,wvxyz', 'fgij')]
    ),
    ( # Day 3
        [hb_lib.testing.CaseParameters("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2", 4)],
        [hb_lib.testing.CaseParameters("#1 @ 1,3: 4x4\n#2 @ 3,1: 4x4\n#3 @ 5,5: 2x2", 3)],
    ),
    ( # Day 4
        [],
        []
    )

]

def load_tests(_loader, _tests, _pattern):
    # This could all be made a bit cleaner with subTest context managers,
    # might want to extend the hb_lib.testing parameterized testcase
    print('loading_tests')
    suite = unittest.TestSuite()

    cases = []

    for day_num, parts in enumerate(CASE_DATA, start=1):
        day_string = "day_{0:0>2}".format(day_num)
        try:
            day_module = importlib.import_module("aoc_2018.{}".format(day_string))
        except ImportError:
            # TODO maybe logging
            print("could not import module for {0}".format(day_string))

        for part_num, part_cases in enumerate(parts, start=1):
            part_string = "part_{0:0>2}".format(part_num)
            try:
                run_function = getattr(day_module, part_string)
            except AttributeError:
                print("no function {0} found in {1}".format(part_string, day_string))
                continue
            for case_data in part_cases:
                cases.append(hb_lib.testing.ParameterizedCase(case_data, run_callable=run_function))

    suite.addTests(cases)

    return suite




