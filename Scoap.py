# format used - cc0/cc1/sc

#--------------------------------------------------functions for different gates-----------------------------------------------------#
# controllability functions for different gates
def fanout_controllability(input):
    op1 = input.copy()
    op2 = input.copy()
    return op1, op2


def andgate_controllability(ip1, ip2):
    op = [0, 0, 0]
    op[0] = min(ip1[0], ip2[0]) + 1
    op[1] = ip1[1] + ip2[1] + 1
    return op


def orgate_controllability(ip1, ip2):
    op = [0, 0, 0]
    op[0] = ip1[0] + ip2[0] + 1
    op[1] = min(ip1[1], ip2[1]) + 1
    return op


def xorgate_controllability(ip1, ip2):
    op = [0, 0, 0]
    op[0] = min((ip1[0]+ip2[0]), (ip1[1]+ip2[1])) + 1
    op[1] = min((ip1[1]+ip2[0]), (ip1[0]+ip2[1])) + 1
    return op

# observablity for different gates


def fanout_observability(input, op1, op2):
    input[2] = min(op1[2], op2[2])
    return input


def andgate_observability(ip1, ip2, op):
    ip1[2] = op[2] + ip2[1] + 1
    ip2[2] = op[2] + ip1[1] + 1
    return ip1, ip2


def orgate_observablitiy(ip1, ip2, op):
    ip1[2] = op[2] + ip2[0] + 1
    ip2[2] = op[2] + ip1[0] + 1
    return ip1, ip2


def xorgate_observability(ip1, ip2, op):
    ip1[2] = op[2] + min(ip2[0], ip2[1]) + 1
    ip2[2] = op[2] + min(ip1[0], ip1[1]) + 1
    return ip1, ip2

#----------------------------------------------------circuit modelling----------------------------------------------------------------#


a = [1, 1, 0]
b = [1, 1, 0]
x = [1, 1, 0]

c, e = fanout_controllability(a)
d, f = fanout_controllability(b)
h = xorgate_controllability(c, d)
i = andgate_controllability(e, f)
j, l = fanout_controllability(h)
k, m = fanout_controllability(x)
o = andgate_controllability(l, m)
n = xorgate_controllability(j, k)  # sum
p = orgate_controllability(o, i)  # carry

o1, i1 = orgate_observablitiy(o, i, p)
j1, k1 = xorgate_observability(j, k, n)
l1, m1 = andgate_observability(l, m, o)
x = fanout_observability(x, k, m)
h = fanout_observability(h, j, l)
e, f = andgate_observability(e, f, i)
c, d = xorgate_observability(c, d, h)
a = fanout_observability(a, c, e)
b = fanout_observability(b, d, f)

output = [a, b, x, c, d, e, f, h, i, j, k, l, m, n, o, p]

for i in range(16):
    if (i == 2):
        print("x", " - ", output[i])
    elif i > 6:
        print(chr(97+i), " - ", output[i])
    elif i > 2:
        print(chr(96+i), " - ", output[i])
    else:
        print(chr(97+i), " - ", output[i])
