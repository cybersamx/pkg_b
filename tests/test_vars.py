import math
import unittest
from dataclasses import dataclass

from pkg_b.vars import variance


@dataclass
class VarsTestCase:
    m: list[float]
    stddev_expect: float


def compare(a: float, b: float) -> bool:
    epsilon = 0.00001
    return math.fabs(a-b) < epsilon


class TestVars(unittest.TestCase):
    tcs = [
        VarsTestCase([1, 2, 3, 4], 1.25),
        VarsTestCase([610, 450, 160, 420, 310], 22440),
    ]

    def test_count(self):
        for tc in self.tcs:
            res = variance(tc.m)
            expect = tc.stddev_expect
            self.assertTrue(compare(res, expect))


if __name__ == '__main__':
    unittest.main()
