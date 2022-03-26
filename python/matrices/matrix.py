import math


class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix



    def getSize(self):
        """return size of matrix row col"""
        
        return (self.getRowSize, self.getColSize)

    def getNumberOfCol(self):
        return len(self.__matrix[0])

    def getNumberOfRow(self):
        return len(self.__matrix)


    def scalarMultiplication(self, scalar):
        for y in self.__matrix:
            for x in self.__matrix:
                self.__matrix[y][x] *= scalar

    def getCol(self, colNum):
        col = []
        if colNum  > self.getNumberOfCol():
            raise IndexError(f"column hors de la matrix de taille {self.getSize}")
        for row in self.__matrix:
            col.append(row[colNum])
        return col
    def getRow(self, row):
        return self.__matrix[row]


    def matriceMultiplication(self, otherMatrice):
        newMatrix = []
        if not isinstance(otherMatrice, Matrix):
            raise ValueError("Parameter must be another matrix")

        if self.getNumberOfCol() != otherMatrice.getNumberOfRow():
            raise IndexError("size of matrix must match")
        
        
        for x in range(0,self.getNumberOfRow()):
            row = self.getRow(x)
            newRow = []
            for y in range(0, otherMatrice.getNumberOfCol()):
                col = otherMatrice.getCol(y)
                res = 0;
                for i in range(len(col)):
                    res += row[i] * col[i]

                newRow.append(res);
            newMatrix.append(newRow)

        return Matrix(newMatrix)

    def __trimMatrix(self, row, col, matrix):
        newMatrix = []
        for y in range(len(self.__matrix)):
            newRow = []
            if y == row:
                continue
            for x in range(len(self.__matrix[0])):
                if x != col:
                    newRow.append(self.__matrix[y][x])
                else:
                    continue
            newMatrix.append(newRow)

        return newMatrix
            
            
    def __determinant(self, matrix=None):
        det = 0
    
        if matrix == None:
            copied_matrix = self.__matrix.copy()
        else:
            copied_matrix = matrix

    
        if len(copied_matrix) ==2 and len(copied_matrix[0]) == 2:
            return (copied_matrix[0][0] * copied_matrix[1][1]) - (copied_matrix[0][1] * copied_matrix[1][0])
        
        for i in range(len(copied_matrix)):
            det += copied_matrix[i][0] * self.determinant(self.__trimMatrix(i, 0, copied_matrix)) * math.pow(-1,i)
        
        return det
    
    def getDeterminant(self):
        return self.__determinant()
            
m = Matrix([
            [1,4],
            [1,2]])

a = Matrix([
    [1,1,3],
    [0,-4,3],
    [0,0,4]])



print(a.getDeterminant())
                                


                
        
            