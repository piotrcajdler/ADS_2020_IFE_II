import numpy
from PIL import Image


BLACK = 0
WHITE = 255
histogram = []
cdf_table = []

def single_threshold(threshold,pic):

    yoda = Image.open(pic)
    array = numpy.array(yoda)
    for y in range(yoda.width):
        for x in range(yoda.height):
            avg = 0
            for z in range(3):
                avg += array[x][y][z]
            avg /= 3
            for z in range(3):
                if avg < threshold:
                    array[x][y][z] = BLACK
                else:
                    array[x][y][z] = WHITE


    yoda2 = Image.fromarray(array)
    yoda2.save("single.jpeg")
    return 0

def double_threshold(pic):
    yoda = Image.open(pic)
    array1 = numpy.array(yoda)
    t1 = (2*255/3)
    t2 = (255/3)

    for y in range(yoda.width):
        for x in range(yoda.height):
            avg = 0
            for z in range(3):
                avg += array1[x][y][z]
            avg /= 3
            for z in range(3):
                if t1 >= avg >= t2:
                    array1[x][y][z] = WHITE
                else:
                    array1[x][y][z] = BLACK

    yoda3 = Image.fromarray(array1)
    yoda3.save('double.jpeg')

def cdf(x,arr):
    counter = 0
    for i in arr:
        if i == x:
            counter += 1
    return counter

def count_cdf(table):
    if len(table) == 0:
        table.append(cdf(0,histogram))

    for i in range(1,256):
        table.append((cdf(i,histogram)) + table[i-1])

    return table

def cdf_val(x,pic):
    return round(((cdf_table[x] - min(cdf_table))/(pic.height * pic.width - min(cdf_table))) * 255)

def EQ(picture):
    global cdf_table,histogram

    yoda = Image.open(picture)
    yoda_gray = yoda.convert("L")
    yoda_gray.save("yoda_greyscale.png")

    grey_arr = numpy.array(yoda_gray)

    for i in range(yoda_gray.height):
        for j in range(yoda_gray.width):
            histogram.append(yoda_gray.getpixel((j,i)))

    cdf_table = count_cdf(cdf_table)

    for i in range(yoda_gray.height):
        for j in range(yoda_gray.width):
            grey_arr[i][j] = cdf_val(grey_arr[i][j], yoda_gray)

    pic = Image.fromarray(grey_arr)
    pic.save("EQ.jpg")
    return 0

def summed_area_table(pic):
    road = Image.open(pic)
    array = numpy.array(road)
    table=numpy.zeros([road.height,road.width,3])
    avg = 0
    for z in range(3):
        avg += array[0][0][z]
    avg //= 3
    for z in range(3):
        table[0][0][z]=avg

    for y in range(1,road.width):
        avg = 0
        for z in range(3):
            avg += array[0][y][z]
        avg //= 3
        for z in range(3):
            table[0][y][z]=avg+table[0][y-1][z]
    for x in range(1,road.height):
        avg = 0
        for z in range(3):
            avg += array[x][0][z]
        avg //= 3
        for z in range(3):
            table[x][0][z]=avg+table[x-1][0][z]
    for y in range(1,road.width):
        for x in range(1,road.height):
            avg = 0
            for z in range(3):
                avg += array[x][y][z]
            avg //= 3
            for z in range(3):
                table[x][y][z]=avg+table[x-1][y][z]+table[x][y-1][z]-table[x-1][y-1][z]
    return table

def mean_mask_helper(array):

    mean=numpy.zeros([len(array)-70,len(array[0])-70,3])

    for z in range(3):
        mean[0][0][z]=array[70][70][z]/(71*71)

    for y in range(1,len(array)-70):
        for z in range(3):
            mean[y][0][z]=round((array[y+70][70][z]-array[y-1][70][z])/(71*71))

    for x in range(1,len(array[0])-70):
        for z in range(3):
            mean[0][x][z]=round((array[70][x+70][z]-array[70][x-1][z])/(71*71))

    for y in range(1,len(array)-70):
        for x in range(1,len(array[0])-70):
            for z in range(3):
                mean[y][x][z]=round((array[y+70][x+70][z]-array[y-1][x+70][z]-array[y+70][x-1][z]+array[y-1][x-1][z])/(71*71))
    return mean

def mean_mask(pic):
    array=summed_area_table(pic)
    mean=mean_mask_helper(array)
    road=Image.fromarray(mean.astype('uint8'))
    road.save("mean.jpg")

