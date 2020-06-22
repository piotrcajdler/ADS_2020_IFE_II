import numpy

def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


def levenshteinDistance(token1, token2):
        distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2


        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1 - 1] == token2[t2 - 1]):
                    distances[t1][t2] = min(distances[t1][t2 - 1] + 1, distances[t1 - 1][t2] + 1, distances[t1 - 1][t2 - 1])
                else:
                    distances[t1][t2] = min(distances[t1][t2 - 1] + 1,  distances[t1 - 1][t2] + 1, distances[t1 - 1][t2 - 1] +1)

        #printDistances(distances, len(token1), len(token2))
        return distances[len(token1)][len(token2)]


def hamdist(str1, str2):
    diffs = 0
    if len(str1) == len(str2):
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 1
        return diffs
    else:
        print("DIFFERENT LENGTHS")
        return 1

def indel(token1,token2):
    distances = numpy.zeros((len(token1)+1, len(token2)+1))
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1-1][t2-1]
            else:
                distances[t1][t2] = min(distances[t1][t2 - 1] + 1, distances[t1 - 1][t2] + 1)

    #printDistances(distances,len(token1),len(token2))
    return distances[len(token1)][len(token2)]

errors = {
    'q': ['a'],
    'w': ['q','a','s','d','e'],
    'e':['w','s','d','f','r'],
    'r':['e','d','f','g','t'],
    't':['r','y'],
    'y':['t','g','j','h','u'],
    'u':['y','h','j','k','i'],
    'i':['u','k','o'],
    'o':['i','l','p','k'],
    'p':['o','l'],
    'a':['s','z'],
    's':['a','w','d'],
    'd':['x','e'],
    'f':['d','r','v','c'],
    'g':['f','h','t','c'],
    'h':['g','j','n','y','b'],
    'j':['k','n'],
    'k':['j','l','m'],
    'l':['o','p'],
    'z':['x','a','s'],
    'x':['d','s','z'],
    'c':['d','f'],
    'v':['f','c','b'],
    'b':['v','g','n'],
    'n':['m','b','j'],
    'm':['j','n','k']
}

def hamming_imp(str1, str2):
    diffs = 0
    if len(str1) == len(str2):
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 2
                for k in errors[ch1]:
                    if k == ch2:
                        diffs -= 1
                        break
        return diffs
    else:
        return 100


#print(hamming_imp("cst","cat"))


def levenshtein_imp(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                distances[t1][t2] = min(distances[t1][t2 - 1] + 1, distances[t1 - 1][t2] + 1,
                                        distances[t1 - 1][t2 - 1])
            else:
                distances[t1][t2] = min(distances[t1][t2 - 1] + 2, distances[t1 - 1][t2] + 2,
                                        distances[t1 - 1][t2 - 1] + 2)
                for k in errors[token1[t1-1]]:
                    if k == token2[t2-1]:
                        distances[t1][t2] = min(distances[t1][t2 - 1] + 1, distances[t1 - 1][t2] + 1,
                                        distances[t1 - 1][t2 - 1] + 1)
                        break


    #printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]

#print(levenshtein_imp("cst","cat"))
file1 = open("words_alpha.txt","r")
file2 = open("test_words.txt","r")
file3 = open("output.txt","w")


def cut(str):
    for i in str:
        if i == '\n':
            str = str[:-1]
            break
    return str


for word in file2:
    file1.seek(0)
    lev = 100000
    ham = 100000
    word = cut(word)
    out = ""


    for check in file1:
        check = cut(check)
        if len(word) in range(len(check)-2,len(check) +2):
            if word == check:
                out = word
                break
            else:
                k = levenshtein_imp(word,check)
                h = hamming_imp(word,check)
                if h < ham or k < lev:
                    ham = h
                    lev = int(k)
                    out = check

    file3.write(out)
    file3.write("\n")





file3.close()
file1.close()
file2.close()
