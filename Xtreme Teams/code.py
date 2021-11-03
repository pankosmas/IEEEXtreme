# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
            
# numpy and scipy are available for use
import numpy
import scipy
from itertools import combinations

T = get_number()

for i in range(T):
    
    N = get_number()
    M = get_number()

    sum = 0
    counter = 0
    students = []
    prefix = []
    query = []
    
    for student in range(N):
        x = list(get_word())
        for char in range(len(x)):
            if x[char] == 'y':
                x[char] = '1'
            else:
                x[char] = '0'
        x = int("".join(x), 2)
        students.append(x)
    
    for i in range(M):
        query.append('1')
    
    query = int("".join(query), 2)
    
    #print(f"query = {query}")
    comb = combinations(students, 3)
    
    for elem in list(comb):
        sum = 0
        for i in elem:
            sum = sum | i
        if sum == query:
            counter += 1
    print(counter)
    

    
    
    
    
    
    
