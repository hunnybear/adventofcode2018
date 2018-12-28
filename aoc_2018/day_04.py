"""
Solution for day 4 of AOC
"""

import datetime
import functools
import re

BEGINS_SHIFT = 'begins shift'
FALLS_ASLEEP = 'falls asleep'
WAKES_UP = 'wakes up'

_LOG_RE_STR = r'\[(?P<timestamp>[\d\-:\s]+)\]\s+(?:Guard #(?P<guard>\d+) )?(?P<action>(?:' + BEGINS_SHIFT + ')|(?:' + FALLS_ASLEEP + ')|(?:' + WAKES_UP + '))'
_LOG_RE = re.compile(_LOG_RE_STR)

_TIMESTAMP_FMT = '%Y-%m-%d %H:%M'

_DATE_MASK = {'year':1, 'month':1, 'day':1}


def _parse_log_line(log_line, current_guard=None):
    match = _LOG_RE.fullmatch(log_line)
    timestamp_str = match.group('timestamp')
    guard = int(match.group('guard') or current_guard)
    action = match.group('action')

    timestamp = datetime.datetime.strptime(timestamp_str, _TIMESTAMP_FMT)

    return timestamp, guard, action


class SleepLog(object):
    """
    The stream of events making up the day of a single guard.
    """

    def __init__(self, guard, sleep_events=None):
        if sleep_events is None:
            sleep_events = []
        self.guard = guard
        self.sleep_events = sleep_events

        self._total_time = None
        self._date = None

    def __and__(self, other):
        overlaps = []
        try:
            # Other sleep logs
            other_events = other.get_sleep_events(mask_date=True)
        except AttributeError:
            # if it's not a SleepLog, assume that
            assert all(len(i) == 2 for i in other)
            for event in other:
                assert(isinstance(event[0], datetime.datetime) and
                       isinstance(event[1], datetime.datetime))

        for self_event in self.get_sleep_events(mask_date=True):
            for other_event in other_events:
                overlap = _get_overlap(self_event, other_event)
                if overlap is not None:
                    overlaps.append(overlap)
        return overlaps

    def get_total_time(self):
        total_time = datetime.timedelta(seconds=0)
        for event in self.sleep_events:
            total_time += event[1] - event[0]

        return total_time

    def get_date(self):
        """
        Get the date for the calendar day that this log is for (whether or not
        it starts late in the day on the previous day).
        """
        if self._date is not None:
            return self._date

        dates = []
        for event in self.sleep_events:
            dates += [dt.date() for dt in event]
        self._date = max(set(dates), key=lambda x: dates.count(x))
        return self._date


    def get_sleep_events(self, mask_date = True):
        for event in self.sleep_events:
            if mask_date:
                start = datetime.datetime(hour=event[0].hour, minute=event[0].minute, **_DATE_MASK)
                end = datetime.datetime( hour=event[1].hour, minute=event[1].minute, **_DATE_MASK)
                yield(start, end)
            else:
                yield event


def _assemble_sleep_logs(input_data):
    guard = None

    # Dict format: {guard_id: [(start, stop)], ...}
    sleep_times = {}
    sleep_start = None
    events = []
    for log_event in sorted(input_data.splitlines()):
        events.append(_parse_log_line(log_event, current_guard=guard))
        guard = events[-1][1]

    current_log = SleepLog(guard)
    sleep_logs = [current_log]
    for timestamp, guard, action in events:
        assert guard
        if action == BEGINS_SHIFT:
            # already did what needs to be done by assigning guard
            # TODO check if this is, in fact, based on a correct assumption
            assert sleep_start is None
            sleep_start = None
            current_log = SleepLog(guard)
            sleep_logs.append(current_log)

        elif action == FALLS_ASLEEP:
            assert sleep_start is None
            sleep_start = timestamp
        elif action == WAKES_UP:
            assert sleep_start is not None
            sleep_times.setdefault(guard, []).append((sleep_start, timestamp))
            current_log.sleep_events.append((sleep_start, timestamp))
            sleep_start = None

    if sleep_start is not None:
        print("dangling sleep: {0} {1}".format(guard, sleep_start))
    return sleep_logs


def _get_guard_sleep_times(sleep_logs):

    sleep_total_times = {}

    for log in sleep_logs:
        sleep_total_times.setdefault(log.guard, datetime.timedelta())
        day_sleep = sum([e[1] - e[0] for e in log.get_sleep_events()], datetime.timedelta())
        sleep_total_times[log.guard] += day_sleep

    return sleep_total_times

def _get_sleep_minutes(sleep_logs, guards=None):
    sleep_minutes = {}

    for log in sleep_logs:
        if guards is not None and log.guard not in guards:
            continue
        for start_time, end_time in log.get_sleep_events():
            sleep_minutes.setdefault(log.guard, dict()).setdefault(log.get_date(), set()).update(range(start_time.minute, end_time.minute))

    return sleep_minutes


def minute_count_key(sleep_minutes, minute):
        count = 0
        for minutes in sleep_minutes.values():
            if minute in minutes:
                count += 1

        return count


def part_01(input_data):

    sleep_logs = _assemble_sleep_logs(input_data)

    guard_sleep_times = _get_guard_sleep_times(sleep_logs)
    # Not actually most likely to sleep, just most minutes slept, as per
    # instructions :p

    sleepiest_guard = max(guard_sleep_times.keys(), key=lambda x:guard_sleep_times[x])

    sleep_minutes = _get_sleep_minutes(sleep_logs, guards=[sleepiest_guard])[sleepiest_guard]

    max_minute = max(set.union(*sleep_minutes.values()), key=functools.partial(minute_count_key, sleep_minutes))

    # Print debugging
    # print('\n'.join(str(v) for v in sleep_minutes.values()))
    # print('max minute: {}'.format(max_minute))
    return max_minute * sleepiest_guard




def part_02(input_data):

    sleep_logs = _assemble_sleep_logs(input_data)

    sleep_minutes = _get_sleep_minutes(sleep_logs)

    max_guard = None
    max_minute = None
    max_minute_count = 0

    max_unsure = False

    # minutes that have an equal count to current max
    unsure = set()

    for guard_id, guard_sleep_minutes in sleep_minutes.items():
        guard_sleep_minutes_values = guard_sleep_minutes.values()
        guard_max_minute = None
        guard_max_minute_count = 0
        guard_unsure = set()
        for day_minute in set.union(*guard_sleep_minutes_values):
            current_minute_count = ([day_minute in day_minutes for day_minutes in guard_sleep_minutes_values]).count(True)
            if current_minute_count > guard_max_minute_count:
                guard_unsure.clear()
                guard_max_minute_count = current_minute_count
                guard_max_minute = day_minute
            elif current_minute_count == guard_max_minute_count:
                guard_unsure.add((day_minute))

        if guard_max_minute_count > max_minute_count:
            max_guard = guard_id
            max_minute = guard_max_minute
            max_minute_count = guard_max_minute_count
            max_unsure = bool(guard_unsure)
        elif guard_max_minute_count == max_minute_count:
            unsure.add((guard_id, guard_max_minute))

    if unsure:
        print('unsure!')
        print(sorted(unsure))
        print(max_minute_count)
    assert not unsure

    return max_guard * max_minute



    sorted_guards = list(sorted(guard_sleep_times, key=lambda x: sum(functools.partial(minute_count_key, sleep_minutes[x]).values())))


    most_consistent_guard = sorted_guards[0]






