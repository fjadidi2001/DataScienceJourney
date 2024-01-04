# EXERCISE 2.2
def sortarray(xs):
    m = xs[0]
    for i in xs:
        if m > i:
            m = i
    return m 

data = [4, 8, 10, 7, 0]

t = sorted(data)
print(t)