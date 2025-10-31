h=0
a=b=0
a=int(input("Entrez la valeur de a "))
b= int(input("Entrez la valeur de b "))
x=a
y=b
S=x
n=1000

c_x1=int(input("Entrrz le coefficient de x^2 dans f(x)"))
c_x=int(input("Entrez le coefficient de x dans f(x) "))
c=int(input("Entrez le constant de f(x) "))
 
def f(x):
	global c_x
	global c
	global c_x1
	return c_x1*x*x+c_x*x+c
	
def newton_cotes(a, b, n):
    h = (b - a) / n
    return h * (f(a) + f(b)) / 2 + h * sum(f(a + i*h) for i in range(1, n))
     
print(newton_cotes(a,b,n))

