eps =0
a=b=0
a=int(input("Entrez la valeur de a "))
b= int(input("Entrez la valeur de b "))
x=a
y=b
S=x
eps=float(input("Entrez le seuil derreur "))
c_x1=int(input("Entrrz le coefficient de x^2 dans f(x)"))
c_x=int(input("Entrez le coefficient de x dans f(x) "))
c=int(input("Entrez le constant de f(x) "))
 
def f(x):
	global c_x
	global c
	global c_x1
	return c_x1*x*x+c_x*x+c
	
while( (f(x)*f(x+eps)>0)):
	x=x+eps
S=x+eps/2

print(S)