import unittest
import day1


class TestStringMethods(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(day1.part_one([0, 1]), 1)
        self.assertEqual(day1.part_one([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]), 7)

    def test_part_two(self):
        self.assertEqual(day1.part_two([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]), 5)


if __name__ == '__main__':
    unittest.main()
