#!/usr/bin/python3
def pascal_triangle(n):
    arr = [1]
    if n:
        for i in range(n):
            for j in range(arr.length - 1):
                new_arr = []
                if j == 0:
                    new_arr[j] = arr[j] + 0
                elif 