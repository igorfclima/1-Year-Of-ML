import numpy as np
import random as rd

def random_notes():
    student_one = [rd.randint(0, 10) for _ in range(4)]
    student_two = [rd.randint(0, 10) for _ in range(4)]
    student_three = [rd.randint(0, 10) for _ in range(4)]
    student_four = [rd.randint(0, 10) for _ in range(4)]
    return np.array([student_one,
                     student_two,
                     student_three,
                     student_four])


def calc_averages(notes):
    avgs = []
    for student in notes:
        avgs.append(np.mean(student))
    return np.array(avgs)

def calc_test_average(notes: np.array):
    avgs = []
    num_colunas = notes.shape[1]
    for i in range(num_colunas):
        row = np.array(notes[:i])
        avgs.append(np.mean(row))
    return np.array(avgs)
