import unittest
from solve import parse, part1, part2

SAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class Tests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse(SAMPLE), [6000, 4000, 11000, 24000, 10000])

    def test_part1(self):
        self.assertEqual(part1(SAMPLE), 24000)

    def test_part2(self):
        self.assertEqual(part2(SAMPLE), 45000)


if __name__ == "__main__":
    unittest.main()
