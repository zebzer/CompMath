

def P(x): #интерполяционный многочлен в форме Ньютона
    xl = [0.5236, 0.87267, 1.22173, 1.57080, 1.91986, 2.26893, 2.61799]
    y = [[0.00010, 0.00112, 0.00687, 0.03018, 0.10659, 0.3207, 0.85128]]
    b = []
    N = 7
    i = 1
    j = 1
    y1 = []

    while j <= N:
        y.append([])
        while i <= N-j:
            y[j].append(0)
            y[j][i-1] = (y[j-1][i]-y[j-1][i-1])/(xl[i+j-1]-xl[i-1])
            i = i + 1
        
        i = 1
        j = j + 1

    j = 0
    i = 0
    #print("P = ", end='')
    while j <= N-1:
        b.append(y[j][0])
        """print(y[j][0], end ='')
        while i < j:
            print("(x - ", xl[i], ")", end='')
            i = i+1
        i = 0"""
        j = j+1
        #print ("+", end='')

    x1 = (x - xl[0])
    x2 = x1*(x - xl[1])
    x3 = x2*(x - xl[2])
    x4 = x3*(x - xl[3])
    x5 = x4*(x - xl[4])
    x6 = x5*(x - xl[5])
    c1 = b[0] + b[1]*x1 + b[2]*x2 + b[3]*x3 + b[4]*x4 + b[5]*x5 + b[6]*x6

    return c1

def dP(x): #производная многочлена
    h = 0.00001
    c2 = (P(x+h)-P(x))/h
    return c2

def Spline(x): #Сплайны и значения
    xl = [0.5236, 0.87267, 1.22173, 1.57080, 1.91986, 2.26893, 2.61799]
    y = [0.00010, 0.00112, 0.00687, 0.03018, 0.10659, 0.3207, 0.85128]
    i = 0
    a = []
    N = 6

    while i < N:
        a.append([0, 0, 0, 0])
        a[i][3] = (dP(xl[i+1])*(xl[i+1] - xl[i])-2*(y[i+1]-y[i])+dP(xl[i])*(xl[i+1]-xl[i]))/((xl[i+1]-xl[i])*(xl[i+1]-xl[i])*(xl[i+1]-xl[i]))
        a[i][2] = (-dP(xl[i+1])*(xl[i+1] - xl[i])*(xl[i+1] + 2*xl[i]) + 3*(y[i+1]-y[i])*(xl[i+1]+xl[i]) - dP(xl[i])*(xl[i+1]-xl[i])*(xl[i]+2*xl[i+1]))/((xl[i+1]-xl[i])*(xl[i+1]-xl[i])*(xl[i+1]-xl[i]))
        a[i][1] = (dP(xl[i+1])*xl[i]*(2*xl[i+1]+xl[i])*(xl[i+1]-xl[i]) - 6*(y[i+1]-y[i])*xl[i]*xl[i+1]+dP(xl[i])*xl[i+1]*(xl[i+1]+2*xl[i])*(xl[i+1]-xl[i]))/((xl[i+1]-xl[i])*(xl[i+1]-xl[i])*(xl[i+1]-xl[i]))
        a[i][0] = (-dP(xl[i+1])*xl[i]*xl[i]*xl[i+1]*(xl[i+1]-xl[i])+y[i+1]*xl[i]*xl[i]*(3*xl[i+1]-xl[i])+y[i]*xl[i+1]*xl[i+1]*(xl[i+1]-3*xl[i])-dP(xl[i])*xl[i]*xl[i+1]*xl[i+1]*(xl[i+1]-xl[i]))/((xl[i+1]-xl[i])*(xl[i+1]-xl[i])*(xl[i+1]-xl[i]))
        i = i + 1
    print(a)

    i = 0
    while i < N:
        S = a[i][0] + a[i][1]*x + a[i][2]*x*x + a[i][3]*x*x*x
        print("S[", i, "] = ", S)
        i = i+1
