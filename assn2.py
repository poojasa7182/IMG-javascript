from mysql.connector.errors import custom_error_exception


class InvalidMatrixException(Exception):
    def __init__(self, message="The given input is not a matrix"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}'

class Matrix:
    def __init__(self,matrix1):
        self.r=int(len(matrix1))
        self.c=int(len(matrix1[0]))
        self.matrix1 = matrix1
        for i in range(self.r):
            if((len((self.matrix1)[i]))!=self.c):
                raise InvalidMatrixException
        self.matrix1 = matrix1
        
    def __repr__(self):
        return self.matrix1
    
    def __add__(self,other):
        x=int(len(other.matrix1))
        y=int(len((other.matrix1)[0]))
        a = [[0]*x for _ in range(y)]
        if(self.r==x and self.c==y):
            for i in range(self.r):
                for j in range(self.c):
                    a[i][j]=((self.matrix1)[i][j]+(other.matrix1)[i][j])
            return a
        else:
            return("Matrix addition not possible!")
    
    def __sub__(self,other):
        x=int(len(other.matrix1))
        y=int(len((other.matrix1)[0]))
        if(self.r==x and self.c==y):
            a = [[0]*x for _ in range(y)]
            for i in range(self.r):
                for j in range(self.c):
                    a[i][j]=((self.matrix1)[i][j]-(other.matrix1)[i][j])
            return a 
        else:
            return("Matrix subtraction not possible!")
    
    def __mul__(self,other):
        # print(type(other))
        # print(type(self.matrix1))
        x=int(len(other.matrix1))
        y=int(len((other.matrix1)[0]))
        a = [[0]*self.r for _ in range(y)]
        if(self.c==x):
            for i in range(self.r):
                for j in range(y):
                    for k in range(self.c):
                            a[i][j]= a[i][j]+(self.matrix1)[i][k]*(other.matrix1)[k][j]
            return a
        else:
            return("Matrix multiplication not possible!")

    def __abs__(self):
        if(self.r==self.c):
            mat = self.matrix1
            if(len(mat) == 2):
                value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
                return value

            sum = 0
            for current_column in range(len(mat)):
                sign = (-1) ** (current_column)

                sub_det = abs(Matrix([row[: current_column] + row[current_column+1:] for row in (mat[: 0] + mat[1:])]))

                sum += (sign * mat[0][current_column] * sub_det)

            return sum
        else: 
            return("Determinant cannot be found!")
    def __pow__(self,other):
        if(self.r==self.c):
            a = Matrix(self.matrix1)
            # print(a*a)
            # print(type(a))
        
            for i in range (other-1):
                a = self*a
                a = Matrix(a)
            return a.matrix1
        else: 
            return("Power can be found only for square matrices")

if __name__ == '__main__':
    mat = Matrix([(1, 6),(1,2,5)])
    
    print(mat**2)