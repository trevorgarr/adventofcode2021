import unittest
import day2

# Currently doesn't work

class TestDayOneMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day2.part_one("forward 1"), (0, 0))
        self.assertEqual(day2.part_one("down 1"), (0, 0))
        self.assertEqual(day2.part_one("up 1"), (0, 0))

    def test_part_two(self):
        self.assertEqual(day2.part_two("forward 1"), (0, 0))


if __name__ == '__main__':
    unittest.main()
