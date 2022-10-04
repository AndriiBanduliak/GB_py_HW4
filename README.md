```задача № 1```
## Вычислить число c заданной точностью d

in
Enter a real number: 9
Enter the required accuracy '0.0001': 0.000001

out
9.000000

in
Enter a real number: 8.98785
Enter the required accuracy '0.0001': 0.001

out
8.988

```задача № 2```

## Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Простые делители числа

in
54

out
[2, 3, 3, 3]

in
9990

out
[2, 3, 3, 3, 5, 37]

in
650

out
[2, 5, 5, 13]

```задача № 3```
## Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

in
7

out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]

in
-1

out
Negative value of the number of numbers!
[]

in
10

out
[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
[6, 2, 3, 0, 9]

```задача № 4```
## * Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.

in
9
5
3

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0

in
0
-1
4

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
4*x^2 - 4 = 0
2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

```задача № 5```
## ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
in
"poly.txt"
"poly_2.txt"

out in the file
3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

in
"poly.txt"
"poly_2.txt"

out
The contents of the files do not match!
