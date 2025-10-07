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
