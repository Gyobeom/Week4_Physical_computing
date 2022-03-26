#module

# built in module 내장 표준 모듈

import math
import random


# print(math.ceil(3.1))  #올림
# print(math.floor(4.9)) #내림
#
# print(math.sqrt(16))
# print(random.randint(1,6))

#사용자 정의 모듈
#import my_math
# print(my_math.power(2,3))
# print(my_math.factorial_loop(5))
# print(my_math.square(5))
# print(my_math.power(2,3))

# from my_math import power,fibo_recursion,factorial_loop,square
#from 모듈이름 import 가져오고 싶은 함수 또는 변수
# print(power(2,3))
# print(factorial_loop(5))
# print(square(5))
# print(power(2,10))

#from my_math import *
#모든 모듈 함수 전부 사용

import my_math as mm
#import 모듈이름 as 원하는 이름

print(mm.power(2,3))
print(mm.factorial_loop(5))
print(mm.square(5))
print(mm.power(2,10))

