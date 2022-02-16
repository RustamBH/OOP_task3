class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        # res += f'Средняя оценка за домашние задания: {av_grade(self.grades)}\n'
        res += f'Средняя оценка за домашние задания: {self.__av_student_grade()}\n'
        res += f'Курсы в процессе изучения: {self.courses_in_progress}\n'
        res += f'Завершенные курсы: {self.finished_courses}\n'
        return res

    def __av_student_grade(self):
        av_sum_grade = 0
        num_grades = 0
        for course in self.grades:
            # av_sum_grade += sum(grades[course]) / len(grades[course])
            av_sum_grade += sum(self.grades[course])
            num_grades += len(self.grades[course])
        # return round(av_sum_grade, 2)
        if num_grades > 0:
            return round(av_sum_grade / num_grades, 2)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        # return av_grade(self.grades) < av_grade(other.grades)
        return self.__av_student_grade() < other.__av_student_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        # res += f'Средняя оценка за лекции: {av_grade(self.grades)}\n'
        res += f'Средняя оценка за лекции: {self.__av_lecturer_grade()}\n'
        return res

    def __av_lecturer_grade(self):
        av_sum_grade = 0
        num_grades = 0
        for course in self.grades:
            # av_sum_grade += sum(grades[course]) / len(grades[course])
            av_sum_grade += sum(self.grades[course])
            num_grades += len(self.grades[course])
        # return round(av_sum_grade, 2)
        if num_grades > 0:
            return round(av_sum_grade / num_grades, 2)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        # return av_grade(self.grades) < av_grade(other.grades)
        return self.__av_lecturer_grade() < other.__av_lecturer_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        # res = f'Имя: {self.name}\n'
        # res += f'Фамилия: {self.surname}'
        return res


def av_grade_all_students(list_students, course):
    # global students_list
    av_sum_grade = 0
    num_grades = 0
    for student in list_students:
        # print(student.grades[course])
        # return f'{student.name}, {student.surname}\n'
        if course in student.grades:
            av_sum_grade += sum(student.grades[course])
            num_grades += len(student.grades[course])
    if num_grades > 0:
        return round(av_sum_grade / num_grades, 2)
    else:
        return 0


def av_grade_all_lecturers(list_lecturers, course):
    # global lecturers_list
    av_sum_grade = 0
    num_grades = 0
    for lecturer in list_lecturers:
        if course in lecturer.grades:
            av_sum_grade += sum(lecturer.grades[course])
            num_grades += len(lecturer.grades[course])
    if num_grades > 0:
        return round(av_sum_grade / num_grades, 2)
    else:
        return 0


# def av_grade(grades):
#     av_sum_grade = 0
#     num_grades = 0
#     for course in grades:
#         # av_sum_grade += sum(grades[course]) / len(grades[course])
#         av_sum_grade += sum(grades[course])
#         num_grades += len(grades[course])
#     # return round(av_sum_grade, 2)
#     if num_grades > 0:
#         return round(av_sum_grade / num_grades, 2)
#     else:
#         return 0


cool_reviewer = Reviewer('Grey', 'Johnson')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['C++']
print(cool_reviewer)

student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Sam', 'Thomson')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_1, 'Git', 6)
student_1.rate_hw(lecturer_1, 'Git', 7)
student_1.rate_hw(lecturer_1, 'Git', 8)

print(lecturer_1)

lecturer_2 = Lecturer('James', 'Fridman')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_2, 'Git', 8)
student_1.rate_hw(lecturer_2, 'Git', 8)
student_1.rate_hw(lecturer_2, 'Git', 9)

print(lecturer_1 > lecturer_2)

cool_reviewer.rate_hw(student_1, 'Python', 9)
cool_reviewer.rate_hw(student_1, 'Python', 9)
cool_reviewer.rate_hw(student_1, 'Python', 9)

cool_reviewer.rate_hw(student_1, 'Git', 10)
cool_reviewer.rate_hw(student_1, 'Git', 10)

print(student_1)

student_2 = Student('Lara', 'Croft', 'woman')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_2.rate_hw(lecturer_1, 'Python', 8)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_1, 'Git', 7)
student_2.rate_hw(lecturer_1, 'Git', 7)
student_2.rate_hw(lecturer_1, 'Git', 9)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 5)
student_2.rate_hw(lecturer_2, 'Git', 5)
student_2.rate_hw(lecturer_2, 'Git', 5)

cool_reviewer.rate_hw(student_2, 'Python', 8)
cool_reviewer.rate_hw(student_2, 'Python', 8)
cool_reviewer.rate_hw(student_2, 'Python', 8)

cool_reviewer.rate_hw(student_2, 'Git', 10)
cool_reviewer.rate_hw(student_2, 'Git', 10)

students_list = [student_1, student_2]
course_specific = 'Python'
print(f'Средняя оценка за д/з по всем студентам в рамках курса {course_specific}: {av_grade_all_students(students_list, course_specific)}')

lecturers_list = [lecturer_1, lecturer_2]
course_specific = 'Git'
print(f'Средняя оценка за лекции всех лекторов в рамках курса {course_specific}: {av_grade_all_lecturers(lecturers_list, course_specific)}')
