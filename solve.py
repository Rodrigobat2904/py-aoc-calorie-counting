"""Advent of Code 2022 Day 1 style: calorie counting.

Input: groups of integers separated by blank lines (one group per elf).
Part 1: largest group sum. Part 2: sum of the top three group sums.
"""
import sys
from typing import List


def parse(text: str) -> List[int]:
    return [sum(int(x) for x in block.split()) for block in text.strip().split("\n\n")]


def part1(text: str) -> int:
    return max(parse(text))


def part2(text: str) -> int:
    return sum(sorted(parse(text), reverse=True)[:3])


if __name__ == "__main__":
    data = sys.stdin.read()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
