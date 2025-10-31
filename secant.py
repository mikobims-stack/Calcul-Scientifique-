eps =0
a=b=0
a=int(input("Entrez la valeur de a "))
b= int(input("Entrez la valeur de b "))
x_0=a
x_1=b
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
	
if f(x_1)==0:
	S=x_1
while( (f(x_0)*f(x_1)<0) and (abs(x_0-x_1)>=eps)):
	S=(x_0*f(x_1) - x_1*f(x_0))/(f(x_1)-f(x_0))
	if f(S)*f(x_1)<0:
		x_0=S
	else:
		x_1=S

print(S)