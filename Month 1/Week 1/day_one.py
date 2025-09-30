import numpy as np

def array_operations():
    # 1D array
    arr_1d = np.array([1,2,3,4,5])
    print("1D Array:")
    print(arr_1d)

    # 2D array
    arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("2D Array:")
    print(arr_2d)

    np.zeros((3,3))
    np.ones((2,4))
    print("Array of zeros (3x3):")
    print(np.zeros((3,3)))# 3 por 3
    print("Array of ones (2x4):")
    print(np.ones((2,4)))# 2 por 4

def main():
    array_operations()

if __name__ == "__main__":
    main()
