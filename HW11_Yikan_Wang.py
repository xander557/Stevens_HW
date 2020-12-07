"""
Homework 11
This file scans data and pretty prints the data

Author: Yikan

"""

from collections import defaultdict
from logging import exception

from prettytable import PrettyTable
from Student_Repository_Yikan import file_reader


def main():
    """populate data and prints"""
    autoReader = Summaries()
    autoReader.print_summary()


def common(list1, list2):
    """
    A helper method
    return true if two list contains same item
    vice versa
    """
    for x in list2:
        if x in list1:
            return False
    return True


def diff(list1, list2):
    """
    A helper method
    :param list1: bigger list
    :param list2: smaller list
    :return: The Items that is in list1 but not list2
    """
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    return result


class Summaries:
    """ Field: dictionaries that stores data of students/grade
                    and instructors.
            Methods that populate those dictionaries.
            A method that prints the summaries
    """

    def __init__(self):
        self.grade_dict = {'A': 4.0, 'A-': 3.75,
                           'B+': 3.25, 'B': 3.0,
                           'B-': 2.75, 'C+': 2.25,
                           'C': 2.0, 'C-': 0,
                           'D+': 0, 'D': 0, 'D-': 0, 'F': 0}
        self.course_dict = defaultdict()
        self.major_dict = defaultdict()
        self.scan_majors()
        self.student_dict = defaultdict()
        self.instructor_dict = defaultdict()
        self.scan_student_info()
        self.scan_instructors()

    def scan_majors(self):
        """scans majors.txt and populate it to a dictionary"""
        path = "majors.txt"
        for i in file_reader(path, 3, '\t', True, 2):
            self.major_dict[i[0]] = [[], []]
        for i in file_reader(path, 3, '\t', True):
            if i[1] == 'R':
                self.major_dict[i[0]][0].append(i[2])
            elif i[1] == 'E':
                self.major_dict[i[0]][1].append(i[2])
            else:
                raise ValueError("Course Flag Error")
        print("Majors Scanned")

    def scan_student_info(self):
        """scans students.txt and populate it to a dictionary"""

        path = "students.txt"
        for i in file_reader(path, 3, '\t', True, 0):
            self.student_dict[i[0]] = [i[1], i[2], 0, 0, [], [], []]

        path = "grades.txt"
        for i in file_reader(path, 4, '\t', True):
            self.student_dict[i[0]][2] += self.grade_dict[i[2]]
            self.student_dict[i[0]][3] += 1
            self.student_dict[i[0]][4].append(i[1])

            # populate course_dict
            try:
                self.course_dict[i[1]][0].append(i[0])

            except Exception as e:
                self.course_dict[i[1]] = [[], '', '', '']
                self.course_dict[i[1]][0].append(i[0])
            self.course_dict[i[1]][1] = i[3]
        for i in self.student_dict.values():
            i[5] = diff(self.major_dict[i[1]][0], i[4])
            if common(self.major_dict[i[1]][1], i[4]):
                i[6] = self.major_dict[i[1]][1]
        print('Student Scanned')

    def scan_instructors(self):
        """scans instructors.txt and populate it to dictionary"""

        path = "instructors.txt"
        for i in file_reader(path, 3, '\t', True):
            self.instructor_dict[i[0]] = [i[1]]
            self.instructor_dict[i[0]].append(i[2])

        keys = self.course_dict.keys()
        for key in keys:
            ins_Id = self.course_dict[key][1]
            self.course_dict[key][2] = self.instructor_dict[ins_Id][0]
            self.course_dict[key][3] = self.instructor_dict[ins_Id][1]

        print('Instructor Scanned')

    def print_summary(self):
        """pretty print the result"""
        pt_student = PrettyTable(field_names=['CWID', 'Name', 'Major',
                                              'Completed Courses', 'Remaining required',
                                              'Remaining Electives', 'GPA'])
        for Id in self.student_dict.keys():
            row = [Id]
            gpa = 0.0
            if self.student_dict[Id][3] != 0:
                gpa = self.student_dict[Id][2] / self.student_dict[Id][3]
                gpa = round(gpa, 2)
            data = [self.student_dict[Id][0], self.student_dict[Id][1],
                    self.student_dict[Id][4], self.student_dict[Id][5],
                    self.student_dict[Id][6], gpa]
            row.extend(data)
            pt_student.add_row(row)
        print(pt_student)

        pt_course = PrettyTable(field_names=['CWID', 'Name', 'Department', 'Course', 'Students'])
        for key in self.course_dict.keys():
            row = [self.course_dict[key][1], self.course_dict[key][2],
                   self.course_dict[key][3], key, len(self.course_dict[key][0])]
            pt_course.add_row(row)
        print(pt_course)

        pt_major = PrettyTable(field_names=['Major', 'Required Courses',
                                            'Electives'])
        for major in self.major_dict:
            row = [major]
            row.extend(self.major_dict[major])
            pt_major.add_row(row)
        print(pt_major)


if __name__ == '__main__':
    main()
