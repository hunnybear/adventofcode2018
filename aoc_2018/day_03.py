"""
day_03.py

code for finding solution of day 3 of the advent of code.

Author: Tyler Jachetta <me@tylerjachetta.net>
"""

import re
import collections

from aoc_2018 import util

_CLAIM_RE_STR = r'#(?P<claim_id>\d+)\s*@\s*(?P<origin>\d+,\d+):\s*(?P<size>\d+x\d+)'
_CLAIM_RE = re.compile(_CLAIM_RE_STR)

Claim = collections.namedtuple('Claim', ['claim_id', 'origin', 'size'])

def _apply_claim(fabric, claim):
    for x in range(claim.origin[0], claim.origin[0] + claim.size[0]):
        for y in range(claim.origin[1], claim.origin[1] + claim.size[1]):
            fabric.setdefault(x, {}).setdefault(y, set()).add(claim.claim_id)


def _create_claims(input_data):
    claims = []
    claim_lines = input_data.splitlines()
    for claim in claim_lines:
        match = _CLAIM_RE.fullmatch(claim)
        claim_info = match.groupdict()

        claim = Claim(
            claim_id=int(claim_info['claim_id']),
            origin=tuple(int(digit) for digit in claim_info['origin'].split(',')),
            size=tuple(int(digit) for digit in claim_info['size'].split('x'))
        )
        claims.append(claim)

    return claims


def _claim_fabric(input_data):

    fabric = {}
    for claim in  _create_claims(input_data):
        _apply_claim(fabric, claim)

    return fabric


def part_01(input_data):

    fabric = _claim_fabric(input_data)

    overlaps = 0
    for col in fabric.values():
        for cell in col.values():
            if len(cell) > 1:
                overlaps += 1

    return overlaps


def part_02(input_data):
    fabric = _claim_fabric(input_data)

    has_overlap = {}

    for col in fabric.values():
        for cell in col.values():
            local_overlap = len(cell) > 1
            for claim_id in cell:
                has_overlap[claim_id] = has_overlap.get(claim_id, False) or local_overlap

    no_overlaps = [k for k,v in has_overlap.items() if not v]

    assert len(no_overlaps) == 1
    return no_overlaps[0]




