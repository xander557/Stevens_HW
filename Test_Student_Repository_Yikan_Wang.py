"""
Homework 08 test file
Author: Yikan
"""

import unittest
from typing import Iterator

from Student_Repository_Yikan import FileAnalyzer
from Student_Repository_Yikan import file_reader


class FileReaderTest(unittest.TestCase):
    """Test file reader"""

    def test_file_reader_should_throw_if_file_found(self):
        """test bahavior when file not opened successfully"""
        directory = 'nosuchfile.txt'
        with self.assertRaises(StopIteration):
            next(file_reader(directory, 3, ' '))

    def test_file_reader_should_read(self):
        """test bahavior when file opened successfully"""
        path = "/Users/yikanwang/Documents/Fall2020/SSW 810/homework/test_file"
        false_header: Iterator[list[str]] = file_reader(path, 3, ' ')
        self.assertEqual(next(false_header), ['xander', 'score', '3'])
        self.assertEqual(next(false_header), ['julie', 'score', '4'])
        self.assertEqual(next(false_header), ['adam', 'score', '7'])
        self.assertNotEqual(next(false_header), ['noname', 'score', '7'])


class FilesScannerTest(unittest.TestCase):
    """test Files Scanner"""

    def test_files_scanner(self):
        directory = '/Users/yikanwang/Documents/Fall2020/SSW 810'
        analyzer = FileAnalyzer(directory)
        print(analyzer.files_summary)
        expected = {'/Users/yikanwang/Documents/Fall2020/SSW 810/HW01-Xander_Wang.py':
                        {'Class': 0, 'Function': 4, 'Lines': 100, 'Characters': 3390}}
        print('this is dict{}'.format(analyzer.files_summary))
        self.assertEqual(analyzer.files_summary, expected)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
