"""
    Author: Yikan Wang
    This file contains methods of datetime and file manipulations

"""

from datetime import datetime, timedelta
import os
from typing import Tuple, Iterator, List, Dict
import sqlite3
from prettytable import PrettyTable



def student_grades_table_db(self, db_path):
    DB_FILE = "HW11.db"
    stevens_db = sqlite3.connect(DB_FILE)

    print('SQL Student grade Summary')
    query = """
                SELECT  s.Name as Name, s.CWID as CWID, g.grade as Grade, i.name as Instructor_Name
                From
                    students s
                    JOIN grades g
                        ON s.CWID = g.StudentCWID
                    JOIN instructors i
                        ON g.InstructorCWID = i.CWID
                ORDER BY s.Name
            """

    pt = PrettyTable(field_names=['Name', 'CWID', 'Grade', 'Instructor'])

    for row in stevens_db.execute(query):
        pt.add_row(row)

    print(pt)

def date_time() -> Tuple[datetime, datetime, int]:
    """Date arithmetics"""
    # First Question
    date_02272020 = datetime(2020, 2, 27)
    three_days_after_02272020 = date_02272020 + timedelta(days=3)
    # Second Question
    date_02272019 = datetime(2017, 2, 27)
    three_days_after_02272019 = date_02272019 + timedelta(days=3)
    # Third Question
    date_01012007: datetime = datetime(2007, 1, 1)
    date_10312017: datetime = datetime(2017, 10, 31)
    delta = date_10312017 - date_01012007
    result = delta.days
    return three_days_after_02272020, three_days_after_02272019, result


def file_reader(path, fields, sep=',', header=False, keyRow=-1) -> Iterator[List[str]]:
    """Input a path of a file and return the content of the file"""

    file_name = os.path.basename(path)
    try:
        fp = open(path)
    except FileNotFoundError:
        print("Fail to open the path: ", path)
    else:
        with fp:
            keyContainer = []
            line_num = 0
            for line in fp:
                line_num += 1
                try:
                    list_strings = list(line.strip('\n').split(sep))

                    if len(list_strings) != fields or '' in list_strings:
                        raise ValueError
                    if keyRow != -1:

                        keyContainer.append(list_strings[keyRow])
                    if header:
                        header = False
                    else:
                        yield list_strings
                except ValueError:
                    print('Expected {} fields for each line in {},'
                          'appears {} fields on line{}. OR one of the field'
                          'seems not valid/inconsistent'.format(fields, file_name,
                                                   len(list_strings), line_num))


class FileAnalyzer:

    """contains serial methods analyzing files in a folder"""
    def __init__(self, directory: str) -> None:
        """ contains inner field and method of file analyzing."""
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ list out all files in the directory and pass it for further analyzing"""
        try:
            files = [file for file in os.listdir(self.directory) if file.endswith('.py')]  # get all python files
        except FileNotFoundError:
            print('{} cannot be found'.format(self.directory))
        else:
            for file in files:
                file_name = os.path.join(self.directory, file)
                self.files_summary[file_name] = self.analyze_file(file_name)

    def pretty_print(self) -> None:
        """pretty print result of analyzed files """
        print("summary for {}".format(self.directory))
        pt = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for file_name in self.files_summary:
            row = [file_name]
            row.extend(list(self.files_summary[file_name].values()))
            pt.add_row(row)
        print(pt)

    def analyze_file(self, file_name):
        """analyzing each file and populate result to a Dict"""
        try:
            file = open(file_name)
        except FileNotFoundError:
            print('{} not found'.format(file_name))
        else:
            with file:
                function_count = 0
                classes_count = 0
                characters = file.read()
                lines = characters.strip('\n').split('\n')
                for line in lines:
                    if line.strip(' ').startswith('class '):
                        classes_count += 1
                    elif line.strip(' ').startswith('def '):
                        function_count += 1
            return {"Class": classes_count, "Function": function_count,
                    "Lines": len(lines), "Characters": len(characters)}


def main():
    print(date_time())
    path = "/Users/yikanwang/Documents/Fall2020/SSW 810/homework/test_file"
    for i in file_reader(path, 3, ' ', header=True):
        print("|".join(i))
    for i in file_reader(path, 3, ' ', header=False):
        print("|".join(i))

    directory = '/Users/yikanwang/Documents/Fall2020/SSW 810'
    analyzer = FileAnalyzer(directory)
    print(analyzer.files_summary)


if __name__ == '__main__':
    main()
