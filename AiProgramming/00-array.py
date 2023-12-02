def maximum(xs):
    m = xs[0]
    for x in xs:
        if m < x:
            m = x
    return m

data = [0,1,2,3,4,5,6,7]

t = maximum(data)
print(t)