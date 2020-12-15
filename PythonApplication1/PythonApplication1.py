import class1
 
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

error, answer = class1.Yravnenie(a, b, c)
if len(answer) > 1:
    print("Ответ: ")
    print(answer[0])
    print(answer[1])
elif len(answer) == 1: 
    print("Ответ: ")
    print(answer[0])
else: 
    print("Ошибка: ")
    print(error)



