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
	
if f(y)==0:
	S=y
while( (abs(y-x)>=eps) and (f(x)*f(y)<0)):
	S=(x+y)/2
	if f(x)*f(S)<0:
		y=S
	else:
		x=S

print(S)