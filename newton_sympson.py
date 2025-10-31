h=0
somme=0
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
	
def newton_sym(a, b, n):
    if n % 2 == 1: n += 1
    h = (b - a) / n
    somme = f(a) + f(b)
    for i in range(1, n, 2):
        somme += 4 * f(a + i*h)
    for i in range(2, n-1, 2):
        somme += 2 * f(a + i*h)
    return h * somme / 3
    
    
print(newton_sym(a,b,n))

