import numpy

listOne = numpy.array([2, 7, 13, 4, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 16, 29, 34, 11, 32, 1, 1, 1, 2, 1, 2, 1, 2, 10, 20, 10, 12, 5, 12, 6, 0, 0, 0, 3, 4, 2, 1, 1, 13, 17, 9, 29, 5, 16, 20, 11, 4, 20, 1, 2, 1, 32, 12, 19, 14, 27, 6, 85, 111, 2, 3, 2, 3, 2, 2, 2, 29, 2, 1, 0, 2, 2, 2, 20, 54, 28, 16, 9, 3, 9, 10, 4, 13, 8, 22, 5, 12, 13, 15, 6, 12, 8, 14, 11, 9, 2, 73, 17, 3, 7, 3, 8, 4, 25, 5, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 12, 82, 23, 0, 18, 59, 4, 10, 7, 5, 2, 5, 2, 7, 4, 16, 17, 11, 6, 1, 16, 17, 34, 13, 22, 50, 100, 53, 40, 41, 63, 19, 13, 8, 0, 2, 15, 9, 4, 9, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 1, 1, 66, 42, 38, 27, 2, 1, 6, 2, 14, 3, 3, 23, 18, 12, 26, 4, 7, 13, 12, 10, 14, 14, 16, 5, 63, 0, 1, 2, 8, 15, 29, 55, 28, 50, 28, 42, 10, 15, 11, 15, 9, 16, 3, 41, 8, 1, 4, 3, 0, 9, 0, 6, 0, 10, 1, 14, 19, 6, 5, 5, 5, 51, 23, 49, 19, 4, 48, 36, 4, 2, 1, 1, 3, 0, 1, 8, 10, 21, 17, 8, 3, 1, 9, 5, 5, 6, 5, 4, 9, 13, 3, 15, 4, 3, 2, 2, 3, 1, 3, 8, 8, 21, 18, 10, 14, 25, 17, 46, 67, 10, 27, 14, 7, 6, 6, 2, 3, 18, 8, 30, 13, 3, 8, 9, 13, 12, 5, 3, 7, 1, 19, 22, 37, 27, 39, 52, 45, 8, 68, 8, 8, 33, 15, 13, 10, 10, 18, 8, 14, 8, 2, 8, 1, 10, 2, 13, 7, 7, 13, 23, 1, 8, 3, 4, 12, 7, 5, 10, 6, 7, 19, 8, 11, 13, 24, 8, 1, 7, 4, 19, 2, 3, 18, 18, 19, 14, 2, 2, 5, 10, 2, 0, 3, 1, 9, 4, 16, 5, 7, 13, 13, 8, 43, 10, 24, 8, 34, 14, 29, 31, 23, 49, 51, 26, 4, 5, 11, 4, 8, 7, 7, 7, 4, 4, 4, 1, 4, 2, 2, 5, 5, 13, 34, 111, 65, 93, 30, 17, 63, 3, 8, 39, 12, 24, 30, 8, 5, 14, 8, 21, 13, 1, 1, 7, 12, 1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 32, 118, 45, 30, 4, 61, 9, 18, 26, 18, 22, 22, 2, 2, 16, 44, 31, 24, 32, 24, 48, 16, 60, 44, 6, 7, 4, 29, 12, 4, 8, 18, 5, 1, 2, 0, 3, 0, 4, 10, 6, 15, 3, 2, 3, 2, 12, 38, 19, 21, 19, 8, 14, 16, 29, 4, 19, 10, 17, 10, 3, 21, 14, 13, 22, 6, 13, 21, 5, 9, 15, 4, 7, 4, 4, 1, 3, 2, 3, 1, 4, 1, 2, 2, 3, 2, 2, 3, 113, 4, 10, 7, 3, 7, 4, 3, 1, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 16, 38, 5, 18, 31, 52, 36, 35, 24, 2, 7, 15, 4, 1, 8, 9, 4, 1, 6, 11, 5, 5, 1, 10, 3, 4, 1, 7, 53, 61, 58, 52, 35, 30, 30, 40, 28, 13, 26, 34, 36, 25, 16, 20, 16, 20, 15, 8, 5, 0, 11, 4, 23, 24, 17, 23, 8, 11, 20, 27, 5, 10, 16, 16, 5, 9, 5, 2, 5, 8, 3, 14, 12, 17, 7, 17, 24, 10, 25, 10])
listTwo = numpy.array([49, 37, 21, 25, 32, 23, 40, 24, 19, 30, 22, 49, 26, 42, 49, 39, 22, 32, 49, 19])


sumTurns = numpy.sum(listTwo)

print(sumTurns)
print(len(listOne))

