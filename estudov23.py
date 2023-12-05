global a 
a = 10

def b():
    B = a + 1
    return B


def c():
    C = a + 2
    return C

def d():
    D = a + 3
    return D


b()
c()
d()


result_b = b()
result_c = c()
result_d =d()

print(result_b,result_c, result_d)