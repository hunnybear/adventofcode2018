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
        [hb_lib.testing.CaseParameters("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""", 240)],
        [hb_lib.testing.CaseParameters("""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""", 4455)],
    ),
    (, # Day 5
    ),
    (, # Day 6
    ),
    (, # Day 7
    ),

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




