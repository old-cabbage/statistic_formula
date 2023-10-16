from math import sqrt

def Ave(x):
    #平均值
    return sum(x)/len(x)

def StanDiv(x):
    #标准偏差
    x0=Ave(x)
    s2=0
    for xi in x:
        s2+=(xi-x0)**2
    sd=sqrt(s2/(len(x)-1))
    return sd

def Sig(x):
    #标准误差Sigma
    x0=Ave(x)
    s2=0
    for xi in x:
        s2+=(xi-x0)**2
    sig=sqrt(s2/len(x))
    return sig

def RegAna(x,y):
    #回归函数系数
    x0=Ave(x)
    y0=Ave(y)
    x1=0
    y1=0
    xy1=0
    for xi in x:
        x1+=xi**2
    for yi in y:
        y1+=yi**2
    for i in range(len(x)):
        xy1+=x[i]*y[i]
    x2=x1/len(x)
    y2=y1/len(y)
    xy0=xy1/len(x)
    r=(xy0-x0*y0)/(sqrt((x2-x0**2)*(y2-y0**2)))
    return r