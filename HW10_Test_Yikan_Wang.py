"""
Homework 10 test file
Author: Yikan
Test is HW10_Yikan_Wang reads&stores data as expected
New added contaminated data included
"""

import unittest
from collections import defaultdict
from typing import List, Iterator

from HW10_Yikan_Wang import summaries


class Summaries_Test(unittest.TestCase):
    """test class of Summaries"""

    def test_summaries(self):
        """test if the class reads&stores data as expected"""
        autoReader = summaries()
        expected_stu = defaultdict(None, {
            '10103': ['Baldwin, C', 'SFEN', 13.75, 4, ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'],
                      ['SSW 540', 'SSW 555'], []],
            '10115': ['Wyatt, X', 'SFEN', 15.25, 4, ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545'], ['SSW 540', 'SSW 555'],
                      []],
            '10172': ['Forbes, I', 'SFEN', 7.75, 2, ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'],
                      ['CS 501', 'CS 513', 'CS 545']],
            '10175': ['Erickson, D', 'SFEN', 10.75, 3, ['SSW 567', 'SSW 564', 'SSW 687'], ['SSW 540', 'SSW 555'],
                      ['CS 501', 'CS 513', 'CS 545']],
            '10183': ['Chapman, O', 'SFEN', 4.0, 1, ['SSW 689'], ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'],
                      ['CS 501', 'CS 513', 'CS 545']],
            '11399': ['Cordova, I', 'SYEN', 3.0, 1, ['SSW 540'], ['SYS 671', 'SYS 612', 'SYS 800', 'SSW 565'], []],
            '11461': ['Wright, U', 'SYEN', 11.75, 3, ['SYS 800', 'SYS 750', 'SYS 611'],
                      ['SYS 671', 'SYS 612', 'SSW 565'], ['SSW 810', 'SSW 565', 'SSW 540']],
            '11658': ['Kelly, P', 'SYEN', 0, 1, ['SSW 540'], ['SYS 671', 'SYS 612', 'SYS 800', 'SSW 565'], []],
            '11714': ['Morton, A', 'SYEN', 6.0, 2, ['SYS 611', 'SYS 645'], ['SYS 671', 'SYS 612', 'SYS 800', 'SSW 565'],
                      ['SSW 810', 'SSW 565', 'SSW 540']],
            '11788': ['Fuller, E', 'SYEN', 4.0, 1, ['SSW 540'], ['SYS 671', 'SYS 612', 'SYS 800', 'SSW 565'], []]})

        self.assertEqual(autoReader.student_dict, expected_stu)
        expected_course = defaultdict(None, {
            'SSW 567': [['10103', '10115', '10172', '10175'], '98765', 'Einstein, A',
                        'SFEN'],
            'SSW 564': [['10103', '10115', '10175'], '98764',
                        'Feynman, R', 'SFEN'],
            'SSW 687': [['10103', '10115', '10175'], '98764', 'Feynman, R', 'SFEN'],
            'CS 501': [['10103'], '98764', 'Feynman, R', 'SFEN'], 'CS 545': [['10115'], '98764', 'Feynman, R', 'SFEN'],
            'SSW 555': [['10172'], '98763', 'Newton, I', 'SFEN'], 'SSW 689': [['10183'], '98763', 'Newton, I', 'SFEN'],
            'SSW 540': [['11399', '11658', '11788'], '98765', 'Einstein, A', 'SFEN'],
            'SYS 800': [['11461'], '98760', 'poluted, C', 'SYEN'],
            'SYS 750': [['11461'], '98760', 'poluted, C', 'SYEN'],
            'SYS 611': [['11461', '11714'], '98760', 'poluted, C', 'SYEN'],
            'SYS 645': [['11714'], '98760', 'poluted, C', 'SYEN']})
        self.assertEqual(autoReader.course_dict, expected_course)
        expected_ins = defaultdict(None, {'98765': ['Einstein, A', 'SFEN'], '98764': ['Feynman, R', 'SFEN'],
                                          '98763': ['Newton, I', 'SFEN'], '98762': ['Hawking, S', 'SYEN'],
                                          '98761': ['Edison, A', 'SYEN'], '98760': ['poluted, C', 'SYEN']})
        self.assertEqual(autoReader.instructor_dict, expected_ins)
        expected_major = defaultdict(None, {
            'SFEN': [['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
            'SYEN': [['SYS 671', 'SYS 612', 'SYS 800', 'SSW 565'], ['SSW 810', 'SSW 565', 'SSW 540']]})
        self.assertEqual(autoReader.major_dict, expected_major)


if __name__ == '__main__':
    """starts test"""
    unittest.main(exit=False, verbosity=2)
