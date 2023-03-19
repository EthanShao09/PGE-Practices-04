#!/usr/bin/env python3

import time


def task01(aList):
    Max = max(aList)
    minL = []
    MaxL = []
    diss = []
    M = len(aList)
    for i in range(len(aList) - 1):
        if i >= 1 and i <= (len(aList) - 2):
            if aList[i] < aList[i - 1] and aList[i] < aList[i + 1]:
                # print("LocalMinimum:",aList[i])
                minL.append(i)
        if aList[i] == Max:
            MaxL.append(i)
    for k in range(len(minL)):
        min = 10002
        for j in range(len(MaxL)):
            dis = abs(minL[k] - MaxL[j])
            if min > dis:
                min = dis
        diss.append(min)
    print(sum(diss))


'''
(索引，深度， 重要性， 值)
1.深度 2.重要性 3.大小(值越小权越大) 
如果完全一样，按照出现的先后
'''


def task02(aList):
    Max = max(aList)
    minL = []
    MaxL = []
    diss = []
    Q = []
    D = []
    V = []
    for i in range(len(aList) - 1):
        if i >= 1 and i <= (len(aList) - 2):
            if aList[i] < aList[i - 1] and aList[i] < aList[i + 1]:
                # print("LocalMinimum:",aList[i])
                minL.append(i)
                V.append(aList[i])
                if abs(aList[i] - aList[i - 1]) < abs(aList[i] - aList[i + 1]):
                    depth = abs(aList[i] - aList[i - 1])
                else:
                    depth = abs(aList[i] - aList[i + 1])
                D.append(depth)
        if aList[i] == Max:
            MaxL.append(i)
    for k in range(len(minL)):
        min = 10002
        for j in range(len(MaxL)):
            dis = abs(minL[k] - MaxL[j])
            if min > dis:
                min = dis
        diss.append(min)
    # print(sum(diss))
    Q.append(minL)
    Q.append(D)
    Q.append(diss)
    Q.append(V)
    ar2 = list(map(list, zip(*Q)))
    ar2.sort(key=lambda x: (x[1], x[2], x[3]))
    for item in ar2:
        print(*item)
    print("")


def task03(aList):
    arr = []
    hSum = round(sum(aList) / 2)
    for i in range(len(aList)):
        for j in range(len(aList)):
            if sum(aList[j:j + i + 1]) >= hSum:
                if len(arr) == 0:
                    arr.append(j)
                    arr.append(j + i)
                    arr.append(sum(aList[j:j + i + 1]))
                else:
                    if j - i < arr[1] - arr[0]:
                        arr[0] = j
                        arr[1] = j + i
                        arr[2] = sum(aList[j:j + i + 1])

            if len(arr) != 0:
                break
        if len(arr) != 0:
            break

    '''
    =========================超时=========================
    for i in range(len(aList)):
        for j in range(i,len(aList)):
            if sum(aList[i:j+1]) >= hSum:
                if len(arr) == 0:
                    arr.append(i)
                    arr.append(j)
                    arr.append(sum(aList[i:j+1]))
                else:
                    if j-i < arr[1]-arr[0]:
                        arr[0] = i
                        arr[1] = j
                        arr[2] = sum(aList[i:j+1])
    '''
    print(*arr)


def task04(aList):
    P = []
    min = []
    for i in range(len(aList) - 1):
        if i >= 1 and aList[i] < aList[i - 1]:
            min.append(i)
    '找到每一个下降趋势的点，然后寻找三个点能够组成的最长的距离，即为要寻找的S'
    if len(min) == 0:
        print("None")
    elif len(min) == 1:
        P.append(min[0] - 1)
        P.append(len(aList) - 1)
    else:
        for i in range(len(min) - 2):
            if len(P) == 0:
                P.append(min[i])
                P.append(min[i + 2] - 1)
            else:
                if (min[i + 2] - min[i]) > (P[1] + 1 - P[0]):
                    P[0] = min[i]
                    P[1] = min[i + 2] - 1
                else:
                    continue
    print(*P)


def task05(aList):
    pass


if __name__ == '__main__':
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    #               I N P U T    R E A D I N G
    taskNo = int(input())
    Nlists = int(input())
    inputLists = []
    for k in range(Nlists):
        oneList = list(map(int, input().split()))
        inputLists.append(oneList)

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    #             P R O C E S S I N G

    t1 = time.time()
    if taskNo in [1, 2, 3, 4]:
        for aList in inputLists:
            if taskNo == 1:  task01(aList)
            if taskNo == 2:  task02(aList)
            if taskNo == 3:  task03(aList)
            if taskNo == 4:  task04(aList)
    if taskNo == 5:
        for i in range(0, len(inputLists), 2):  # targets and shots
            task05(inputLists[i], inputLists[i + 1])

    t2 = time.time()
    # print( 'time', str(t2-t1)[:5] )
