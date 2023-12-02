def minimum(xs):
    m = xs[0]
    for i in range(xs):
        if m < xs:
            m = i
    return m 

data = [4, 8, 10, 7, 0]
t = minimum(data)
print(t)