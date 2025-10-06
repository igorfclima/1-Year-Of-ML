import numpy as np
import random as rd

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

    #array de 1 a 100 com passo 5
    array = np.arange(1, 101, 5)
    print("Array from 1 to 100 with step 5:")
    print(array)

    print("Array statistics:")
    print("Shape: ", array.shape) #tamanho do array
    print("Type: ", array.dtype) #tipo do array
    print("Size: ", array.size) #quantidade de elementos
    print("Dimensions: ", array.ndim) #dimensao do array

def slicing_example():
    M = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    print("Original Array:")
    print(M)

    print("Slicing Examples:")
    print("First two rows and first two columns:")
    matriz = M[0:2, 0:2]
    print(matriz)

    print("First two rows and last two columns:")
    matriz = M[0:2, 2:4]
    print(matriz)

    print("First row:")
    matriz = M[0:1,]
    print(matriz)

    print("Second row:")
    matriz = M[1:2,]
    print(matriz)

    print("Last row:")
    matriz = M[2:3,]
    print(matriz)


def rand_tests():
    print("Random Array:", rd.random())
    rand_array = np.array([rd.randint(1, 100) for _ in range(20)])
    print("Random Array:", rand_array)

    filtered_array = rand_array > 50
    print("Filtered Array (values > 50):", rand_array[filtered_array])

def main():
    array_operations()
    slicing_example()
    rand_tests()

if __name__ == "__main__":
    main()
