import unittest
import class1

class Test_test1(unittest.TestCase):
    def test_1(self): # все равно 0
       expError = 'R'
       expResult = []
       a = 0
       b = 0
       c = 0
       actError, actResult = class1.Yravnenie(a, b, c)
       self.assertEqual(expError, actError)
       self.assertEqual(len(expResult), len(actResult))
    def test_2(self): # a и b равны 0
        expError = "Нет корней"
        expResult = []
        a = 0
        b = 0
        c = 9
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
    def test_3(self): # a равно 0
        expError = ""
        expResult = [ -1 ]
        a = 0
        b = 2
        c = 2
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
    def test_4(self): # Дискриминант меньше 0
        expError = "Нет корней"
        expResult = []
        a = 2
        b = 4
        c = 6
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
    def test_5(self): # Дискриминант равен 0
        expError = ""
        expResult = [ -1 ]
        a = 2
        b = 4
        c = 2
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
    def test_6(self): # Дискриминант больше 0
        expError = ""
        expResult = [ 3, 2 ]
        a = 1
        b = -5
        c = 6
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
        self.assertEqual(expResult[1], actResult[1])
        

if __name__ == '__main__':
    unittest.main()
