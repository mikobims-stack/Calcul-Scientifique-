eps =0
a=0
a=int(input("Entrez la valeur de a "))
x_0=a
S=x_0
eps=float(input("Entrez le seuil derreur "))
c_x1=int(input("Entrrz le coefficient de x^2 dans f(x)"))
c_x=int(input("Entrez le coefficient de x dans f(x) "))
c=int(input("Entrez le constant de f(x) "))
 
def f(x):
	global c_x
	global c
	global c_x1
	return c_x1*x*x+c_x*x+c
	
def f_prime(x):
	global c_x
	global c
	global c_x1
	return c_x1*2*x+c_x
	
if f(x_0)==0:
	S=x_0
if f_prime(S)!= 0 :
	S=x_0 - f(x_0)/f_prime(x_0)
	
while( (f_prime(S)!=0) and (abs(S-x_0)>=eps)):
	x_0=S
	S=x_0 - f(x_0)/f_prime(x_0)


print(S)