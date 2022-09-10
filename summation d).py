#import helper
from itertools import count
import math 

#write in your basic variables
fact = int(input('fact = '))
r = int(input('r = '))
r_list = []
fact_r_list = []
counter = 0

#build basic function
factorial_fact = math.factorial(int(fact)) # the variable will not be changed

for i in range(1,fact-r+2):
    factorial_r = math.factorial(r+counter)
    r_list.append(factorial_r)
    counter += 1


counter = 0 #reset counter

for i in range(1,fact-r+2):
    factorial_fact_r = math.factorial(fact - r - counter)
    fact_r_list.append(factorial_fact_r)
    counter +=1


#we have got the two main values lists

C_list = []
counter = 0
#calculate the sum of summation

for i in range(1,fact-r+2):
    C = factorial_fact / (r_list[counter] * fact_r_list[counter])
    C_list.append(C)
    counter += 1
    
C_sum = sum(C_list)
print('the answer is ' + str(C_sum))




