"""
Homework 11 test file
Author: Yikan
Test is HW11_Yikan_Wang reads&stores data as expected
New added contaminated data included

I under stand that I should keep width of lines under 59,
but it is very difficult for a long test list in this file
"""
from HW11_Yikan_Wang import Summaries

import unittest
from collections import defaultdict
from typing import List, Iterator


class Summaries_Test(unittest.TestCase):
    """test class of Summaries"""

    def test_summaries(self):
        """test if the class reads&stores data as expected"""
        autoReader = Summaries()
        expected_stu = defaultdict(None, {
            '10103': ['Jobs, S', 'SFEN', 6.75, 2, ['SSW 810', 'CS 501'], ['SSW 540', 'SSW 555'], []],
            '10115': ['Bezos, J', 'SFEN', 4.0, 2, ['SSW 810', 'CS 546'], ['SSW 540', 'SSW 555'], []],
            '10183': ['Musk, E', 'SFEN', 8.0, 2, ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546']],
            '11714': ['Gates, B', 'CS', 10.5, 3, ['SSW 810', 'CS 546', 'CS 570'], [], []]})
        expected_course = defaultdict(None, {
            'SSW 810': [['10103', '10115', '10183', '11714'], '98763', 'Rowland, J', 'SFEN'],
            'CS 501': [['10103'], '98762', 'Hawking, S', 'CS'],
            'CS 546': [['10115', '11714'], '98764', 'Cohen, R', 'SFEN'],
            'SSW 555': [['10183'], '98763', 'Rowland, J', 'SFEN'],
            'CS 570': [['11714'], '98762', 'Hawking, S', 'CS']})
        expected_ins = defaultdict(None, {
            '98764': ['Cohen, R', 'SFEN'],
            '98763': ['Rowland, J', 'SFEN'],
            '98762': ['Hawking, S', 'CS']})

        expected_major = defaultdict(None, {
            'SFEN': [['SSW 540', 'SSW 810', 'SSW 555'], ['CS 501', 'CS 546']],
            'CS': [['CS 570', 'CS 546'], ['SSW 810', 'SSW 565']]})

        self.assertEqual(autoReader.course_dict, expected_course)
        self.assertEqual(autoReader.major_dict, expected_major)
        self.assertEqual(autoReader.instructor_dict, expected_ins)
        self.assertEqual(autoReader.student_dict, expected_stu)



if __name__ == '__main__':
    """starts test"""
    unittest.main(exit=False, verbosity=2)
