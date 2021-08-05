import unittest
import assn2

class test_matrix_functions(unittest.TestCase):

    mat1 = assn2.Matrix([(12,7,3),(4 ,5,6),(7 ,8,9)])
    mat2 = assn2.Matrix([(5,8,1),(6,7,3),(4,5,9)])
    mat3 = assn2.Matrix([(1, 2), (4, 5), (3, 6)])
    mat4 = assn2.Matrix([(1,2,3),(4,5,6)])

    def test_add(self):
        r1 = self.mat1 + self.mat2
        r2 = [[17, 15, 4],[10, 12, 9],[11, 13, 18]]
        self.assertEqual(r1,r2)
        
        r1 = self.mat1 + self.mat3
        self.assertEqual(r1,"Matrix addition not possible!")

    def test_sub(self):
        r11 = self.mat1 - self.mat2
        r21 = [[7, -1 , 2],[-2, -2, 3],[3, 3, 0]]
        self.assertEqual(r11,r21)

        r11 = self.mat1 - self.mat3
        self.assertEqual(r11,"Matrix subtraction not possible!")
    
    def test_mul(self):
        r1 = self.mat1 * self.mat2
        r2 = [[114, 160, 60],[74, 97, 73],[119, 157, 112]]
        self.assertEqual(r1,r2)

        r3 = self.mat4*self.mat3
        r2 = [[18,30],[42,69]]
        self.assertEqual(r3,r2)

        r4 = self.mat1*self.mat4
        self.assertEqual(r4,"Matrix multiplication not possible!")

    def test_abs(self):
        r1 = abs(self.mat1) 
        r2 = abs(self.mat2)
        r3 = abs(self.mat3)

        self.assertEqual(r1,-3)
        self.assertEqual(r2,-94)

        self.assertEqual(r3,"Determinant cannot be found!")

    def test_pow(self):
        r1 = self.mat1**3
        r2 = [[3623,2906,2382],[2396,2043,1800],[3842,3258,2853]]
        self.assertEqual(r1,r2)

        r1 = self.mat2**2
        r2 = [[77,101,38],[84,112,54],[86,112,100]]
        self.assertEqual(r1,r2)

        r1 = self.mat4**2
        self.assertEqual(r1,"Power can be found only for square matrices")

if __name__ == '__main__':
    unittest.main()