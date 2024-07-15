# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 18:34:14 2024

@author: Elyorbek
"""

# practical tasks given at the end of the lesson

# # a function that can find the biggest number among three given nums

# def max_find(a, b, c):
#     big = a
#     if b >= big:
#         big = b
        
#     if c >= big:
#         big = c
        
#     return big

# print("\nEnter three different integer numbers:")

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# print("max is ", max_find(a, b, c))



# # function that shows prime numbers in a given range

# def find_primes(down, up):
#     primes = []
    
#     for num in range(down, up + 1):
#         prime = True
#         if num == 1:
#             prime = False
#         elif num == 2:
#             prime = True
            
#         else:
#             for x in range(2, num):
#                 if (num % x == 0):
#                     prime = False
#         if prime:
#             primes.append(num)

#     return primes

# down = int(input("Enter the range:\nstar: "))
# up = int(input("finish: "))

# primes = (find_primes(down, up))
# for prime in primes:
#     print(prime)
    
    
# the function that finds Fibonacci sequence

def fib_finder(k): # k = the number of Fibonacci sequences
    nums = [1, 1]
    
    if k == 1:         # cheaching the first 2 sequence
        nums = nums[0:1]
    elif k == 2:
        nums = nums[:]
        
    while k > len(nums):
        nums.append(nums[-1] +nums[-2])
    
    return nums

k = int(input('Enter the number of Fibonacci sequences:\n>>> '))
print(fib_finder(k))


# # 2nd version
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(5))


    





















