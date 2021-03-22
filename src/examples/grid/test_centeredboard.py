import unittest

from examples.grid.centeredboard import CenteredBoard


class CenteredBoardTest(unittest.TestCase):
    def test_board(self):
        n = 19
        left_i = -9
        right_i = 9
        b = CenteredBoard(n)
        v = 5

        self.assertIsNone(b.setval(0, 0, v))
        self.assertEqual(b.getval(0, 0), v)

        self.assertIsNone(b.setval(left_i, left_i, v))
        self.assertEqual(b.getval(left_i, left_i), v)

        self.assertIsNone(b.setval(right_i, right_i, v))
        self.assertEqual(b.getval(right_i, right_i), v)

        self.assertTrue(b.inrange(0, 0))
        self.assertTrue(b.inrange(left_i, left_i))
        self.assertTrue(b.inrange(right_i, right_i))

        self.assertFalse(b.inrange(left_i - 1, left_i - 1))
        self.assertFalse(b.inrange(right_i + 1, right_i + 1))

        with self.assertRaises(IndexError):
            b.setval(right_i + 1, right_i + 1, v)


if __name__ == '__main__':
    unittest.main()
