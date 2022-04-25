"""Shira Cohen 211777834
   Eli Ben Aharon 311614853
   Ilan Shklover  206753550

"""
def diagonal(x11,x22,x33,y11,y22,y33,z11,z22,z33):
    if (x11>=y11 and x11>=z11 and y22>=x22 and y22>=z22 and z33>=x33 and z33>=y33):
        return True
    return False

def gauss_seidel(f1,f2,f3,e):
    #Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1
    #Implementation of Gauss Seidel Iteration
    print('\nCount\tx\ty\tz\n')
    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%d\t%0.10f\t%0.10f\t%0.10f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)
        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        condition = e1 > e and e2 > e and e3 > e

    print('\nSolution: x=%0.10f, y=%0.10f and z = %0.10f\n' % (x1, y1, z1))

    e=1
    x0 = 0
    y0 = 0
    z0 = 0
    c = 0
    while e>0.0000001 and c < 100:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%0.5f\t%0.5f\t%0.5f\t' %(x1, y1, z1))
        e= abs(x0 - x1)
        x0 = x1
        y0 = y1
        z0 = z1
        c += 1

    print('\nSolution: x=%0.5f, y=%0.5f and z = %0.5f\n' % (x1, y1, z1))

def Jacobi(x11,x22,x33,y11,y22,y33,z11,z22,z33,b11,b22,b33):
    if diagonal(x11, x22, x33, y11, y22, y33, z11, z22, z33) == False:
        print("no dominant diagonal -cant do Jacobi")
        return
    f1 = lambda x, y, z: (b11 - y * y11 - z * z11) / x11
    f2 = lambda x, y, z: (b22 - x * x22 - z * z22) / y22
    f3 = lambda x, y, z: (b33 - x * x33 - y * y33) / z33

    e=1
    x0 = 0
    y0 = 0
    z0 = 0
    c = 0
    while e>0.00001 and c < 100:
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        print('%0.5f\t%0.5f\t%0.5f\t' %(x1, y1, z1))
        e= abs(x0 - x1)
        x0 = x1
        y0 = y1
        z0 = z1
        c += 1

    print('\nSolution: x=%0.5f, y=%0.5f and z = %0.5f\n' % (x1, y1, z1))

f1 = lambda x, y, z: (2 - 2 * y) / 4
f2 = lambda x, y, z: (6 - 2 * x + -4 * z) / 10
f3 = lambda x, y, z: (5 - 4 * y) / 5

print("Enter the factors of the equations")
x=[0,0,0]
y=[0,0,0]
z=[0,0,0]
b=[0,0,0]
for i in range(4):
    for j in range(3):
        if i==0:
            print("enter x" + str(j + 1))
            x[j] =float(input())
        if i ==1:
            print("enter y"+str(j+1))
            y[j] = float(input())
        if i ==2:
            print("enter z" + str(j+1))
            z[j] = float(input())
        if i == 3:
            print("enter b" + str(j + 1))
            b[j] = float(input())
print("solution by gauss")
gauss_seidel(f1,f2,f3,e)

print("solution by Jacobi")
Jacobi(x[0],x[1],x[2],y[0],y[1],y[2],z[0],z[1],z[2],b[0],b[1],b[2])



'''print("solution by gauss")
gauss(4,2,0,2,10,4,0,4,5,2,6,5)
print("solution by Jacobi")
Jacobi(4,2,0,2,10,4,0,4,5,2,6,5)
'''

