from collections import Counter
import numpy as np

day_so = "0 61 26 80 46 69 36 88 85 67 13 79 20 8 92 95 9 68 54 93 57 55 40 92 18 61 4 43 11 20 42 1 76 49 90 34 17 61 23 79 42 32 63 7 80 3 93 44 69 87 90 96 58 98 39 68 0 69 94 75 13 36 21 24 68 8 28 47 67 47 78 24 99 7 25 98 89 60 1 22 82 90 51 36 16 66 39 66 9 72 87 12 1 88 23 85 75 38 90 10"
arr = day_so.split(' ')
print(arr)
count = 0
for number in arr:
    number = int(number)
    if number != 0 and number % 2 == 0:
        count += 1
# so chan
print(count)

# so nguyen to
count_nguyento = 0
for number in arr:
    number = int(number)
    count_chiahet = 0
    for i in range(2, number):
        if number % i == 0:
            count_chiahet += 1
    if count_chiahet == 0:
        count_nguyento += 1
print(count_nguyento)

# tong cac so chia het cho 3
sum = 0
for number in arr:
    number = int(number)
    if number % 3 == 0:
        sum += number
print(sum)


def word_frequency(words):
    """Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


print(word_frequency(arr))

c = dict(Counter(arr))
print(c)

set_arr = set(arr)
print(len(set_arr))

str_a = "87 47 2 39 96 79 53 15 13 7 65 81 90 14 53 99 21 38 91 93 82 13 76 84 48"
str_b = "97 37 93 70 94 77 0 4 36 56 27 1 17 35 34 83 14 30 37 73 5 99 58 68 37"
arr_a = str_a.split(' ')
arr_b = str_b.split(' ')
arr_a_int = []
arr_b_int = []
for i in arr_a:
    i = int(i)
    arr_a_int.append(i)
for i in arr_b:
    i = int(i)
    arr_b_int.append(i)
A = np.array(arr_a_int)
B = np.array(arr_b_int)
TVH = 0
# vector A = (a1, a2, a3) vector B =(b1, b2, b3), TVH = a1*b1+a2*b2+b3*b3
for i in range(0, A.size, 1):
    TVH += A[i] * B[i]
print("Tich vo huong", TVH)

# Tính tổng giá trị lớn nhất của hai vector
print(max(arr_a_int) + max(arr_b_int))

if 99 in arr_b_int:
    print(99)

arr_a_reshape = A.reshape((5, 5))
arr_b_reshape = B.reshape((5, 5))
C = arr_a_reshape * arr_b_reshape
sum_c = 0
print(C)

for i in range(0, 5):
    for j in range(0, 5):
        # print(C[i][j])
        sum_c += C[i][j]
print(sum_c)


def fibonacciLoop(nthNumber):
    previouspreviousNumber = 0
    previousNumber = 0
    currentNumber = 1
    for i in range(1, nthNumber):
        previouspreviousNumber = previousNumber

        previousNumber = currentNumber

        currentNumber = previouspreviousNumber + previousNumber

    return currentNumber

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya

print(fibonacciLoop(100))

