from random import randint

data = [randint(0, 10) for i in range(10)]
data_new = [i for i in range(100) if i % 10 == 0]
print(data)
print(data_new)

#pivot を基準値として、左、右の配列を再起的に繰り返す
def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left, right = [], []
    same = 0

    for i in data:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
        else:
            same += 1

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] * same + right


print(quicksort(data))


#バブルソート
#隣り合う要素同士を比較し、交換していく
#最大値から決まっていく

#バブルソートの原型
for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

#これを関数にすると
def boublesort(data):
    change = True
    for i in range(len(data)):
        if not change:
            break
        change = False

        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

print(boublesort(data))


#挿入ソート
#挿入済みとみなして、どんどん後ろにずらしていく

def sounyusort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > temp):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp
    return data


#選択ソート
#最小値を先頭に持ってくる

def sennkeisort(data):
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j
        data[i], data[min] = data[min], data[i]
    return data

print(sennkeisort(data))


#二分探索
#データが昇順、こう潤になっているときに使える

def nibutannsaku(data_new, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif value > data[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

    