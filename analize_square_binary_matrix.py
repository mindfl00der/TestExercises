"""   The program analyzes a square binary matrix of arbitrary dimension (n * n) and displays a verdict whether
    the analyzed matrix can be converted to a degenerate matrix (all elements of which are equal to 0 (zero))
    or to a matrix all of whose elements are equal to 1 (one) by iteratively inverting the values ​​in any row/column.
      
      The main idea of ​​the algorithm is that the analyzed matrix is ​​segmented into matrices of the 2nd order (2 * 2)
    and if at least one of the matrices of the 2nd order cannot be transformed ==> the entire matrix (n * n) also
    cannot be transformed.

=========================================================================================================================

      Программа анализирует квадратную бинарную матрицу произвольной размерности (n*n) и выводит вердикт может ли
    анализируемая матрица быть преобразована к вырожденной матрице (все элементы которой равны 0 (нулю)) или к матрице
    все элементы которой равны 1 (единице) путем итерационного инвертирования значений в любой строке/столбце.

      Основная идея алгоритма заключается в том, что анализируемая матрица сегментируется на матрицы 2-го порядка (2*2)
    и если хоть одна из матриц 2-го порядка не может быть преобразована ==> вся матрица (n*n) также не может быть
    преобразована.
"""

from datetime import datetime
from random import randint, random

def generateRow(size: int):
    """   The function creates a list of binary values (0 or 1) of given length using a random number generator.

        Keyword arguments:
          size -- the number of elements in the generated list

    =====================================================================================================================

          Функция создает список бинарных значений (0 или 1) заданной длинны используя генератор случайных чисел.
        
        Аргументы функции
         size -- количество элементов в создаваемом списке
    """
    retRow = []
    for i in range(size):
        retRow.append(randint(0, 1))
    return retRow

def detSquare (squareArray: list):
    """   The function calculates the second order matrix determinant (second order determinant), which is equal to
        the difference between the products of the main and secondary diagonals of the matrix.
        A = a[1][1] * a[2][2] - a[1][2] * a[2][1]

        Keyword arguments:
          squareArray -- matrix of the 2nd order (2*2) for which you need to calculate the determinant (determinant)

    =====================================================================================================================

          Функция считает определитель матрицы второго порядка (определитель второго порядка), который равен
        разности произведений главной и побочной диагоналей матрицы. A = a[1][1] * a[2][2] - a[1][2] * a[2][1]
        
        Аргументы функции
         squareArray -- матрица 2-го порядка (2*2) для которой нужно расчитать детерминант (определитель)
    """
    return squareArray[0][0] * squareArray[1][1] - squareArray[0][1] * squareArray[1][0]

def autoFillMatrix(size: int):
    retMatrix = []
    for i in range(size):
        retMatrix.append(generateRow(size))
    return retMatrix

def analyzeMatrix(squareArray: list, size: int): 
    for i in range(size - 1):
        for j in range(size - 1): 
            secondDimension = [[squareArray[i][j], squareArray[i][j + 1]], [squareArray[i + 1][j], squareArray[i + 1][j +1]]]
            print('Matrix for find determinate:\n\t', secondDimension)
            if (secondDimension[0].count(0) + secondDimension[1].count(0)) % 2 != 0:
                return True
    return False

def normalizeRow (denormalizeRow: list):
    return list(map(int, list(map(bool, denormalizeRow))))

def fillMatrix(size):
    retMatrix = []
    i = 0
    while i < size:
        try:
            workRow = list(map(int, input('Enter 0 or 1 values for matrix row (Space-Separated) : ').strip().split()))[:n]
            if len(workRow) == n:
                i += 1
                retMatrix.append(normalizeRow(workRow))
                continue
            raise
        except:
            print('You are wrong in intup. Please, try again.')
    return retMatrix

if __name__ == '__main__':
    retValue = 'Matrix can be converted'
    isntConvertable = 'Matrix can\'t be converted'
    n = int(input('Please inpet matrix size: '))
    if n > 1:
        workArray = []
        if input('Do you want fill matrix manualy y/n? (Default [No]): ').lower() == 'y':
            workArray = fillMatrix(n)
        else:
            workArray = autoFillMatrix(n)
        print('Square Matrix is:\n\t', workArray)
        analyzeTime = datetime.now()
        if analyzeMatrix(workArray, n):
            retValue = isntConvertable
    analyzeTime = datetime.now() - analyzeTime
    print(retValue + '\nAnalyze time: ', analyzeTime)
