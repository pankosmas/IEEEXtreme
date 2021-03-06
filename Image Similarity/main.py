# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()
#------------------------------------------------------------------------------------
def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
#------------------------------------------------------------------------------------
def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
#------------------------------------------------------------------------------------
def moveV(img):
    img = numpy.roll(img, -1, axis=0)
    return img
#------------------------------------------------------------------------------------
def moveH(img):
    img = numpy.roll(img, 2, axis=1)
    return img
#------------------------------------------------------------------------------------
# x, y are single rows or you can pass whole list and then choose respective rows
def eval(img1, img2):
    counter = 0
    i = min(len(img1), len(img2))
    j = min(len(img1[0]), len(img2[0]))
    
    for row in range(i):
        for col in range(j):
            if (img1[row][col] == img2[row][col]) and img1[row][col] == '1':
                counter += 1
    return counter
#-------------------------------------------------------------------------------------
def count_blacks(img):
    counter = 0
    for row in range(len(img)):
        for col in range(len(img[0])):
            if img[row][col] == '1':
                counter += 1
    return counter

#-----------------------------------------------------------------------------

# numpy and scipy are available for use
import numpy
import scipy

T = get_number()

for i in range(T):
    
    R1 = get_number()
    C1 = get_number()
    
    image1 = []
    image2 = []
    
    for row in range(R1):
        x = list(get_word())
        image1.append(x)
    
    for row in range(R1):
        for col in range(C1):
            if image1[row][col] == "#":
                image1[row][col] = '1'
            else:
                image1[row][col] = '0'
    
    R2 = get_number()
    C2 = get_number()
    
    for row in range(R2):
        x = list(get_word())
        image2.append(x)
    
    for row in range(R2):
        for col in range(C2):
            if image2[row][col] == "#":
                image2[row][col] = '1'
            else:
                image2[row][col] = '0'
                
#-------------------fill in necessary blanks ------------------------
    if ((R1 == C2 and R2 == C1) and (R1 != R2 or C1 != C2)):
        image2 = numpy.transpose(image2)
        image2 = image2.tolist()
    else:
        if R1 != R2:
            factor = abs(C1 - C2)
            k = ['0'] 
            
            if R1 > R2:
                for times in range(R1 - R2):
                    image2.append(k * (max(C1,C2) - factor))
            else:
                for times in range(R2 - R1):
                    image1.append(k* (max(C1,C2) - factor))
                    
        if C1 != C2:
            factor = abs(C1 - C2)
            k = ['0'] * factor
            
            if C1 > C2:
                for row in range(len(image2)):
                    image2[row].extend(k)
            else:
                for row in range(len(image1)):
                    image1[row].extend(k)
    
    #print(image1)
    #print(image2)
#----------------------------------------------------------------------
#-------------------how many blacks max?------------------------------

    blacks1 = count_blacks(image1)
    blacks2 = count_blacks(image2)
    blacks = min(blacks1, blacks2)
    
#---------------------make all possible moves and return evals------------
    results = []
    
    for number in range(4):
        for number in range(2):
            image1 = numpy.flipud(image1)
            for number in range(2):
                image1 = numpy.fliplr(image1)
                for k in range(len(image1)):
                    image1 = moveV(image1)
                    for k in range(len(image1[0])):
                        image1 = moveH(image1)
                        res = eval(image1, image2)
                        results.append(res)
                        if res == blacks:
                            break
        image1 = rotate_matrix(image1)

    if res == blacks:
        print(res)
    else:
        print(max(results))
