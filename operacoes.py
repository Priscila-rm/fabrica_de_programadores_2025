a = 4
b = 10
c = 5.0
d = 1
f = 5

print (a==c) 
print (a<b)
print (d>b)
print (c!=f)
print (a==b)
print (c<d)
print (b>a)
print (c>=f)
print (f>=c)
print (c<=c)
print (c<=f)

s= "The most old"

print(s[1:3]) # intervalo ente 1 e 3
print(s[-3:-1]) #ol
print(s[-3:]) #old 
print(s[-3:0]) #

p = "priscila"


# Aula da profª Yuri

print(p.startswith("prisci"))
print(len(p))
print("cila" in (p))

numero1= int(input("insira o primeiro numero da divisão: "))
numero2= int(input("insira o segundo numero da divisao: "))

#divisao com resultado float
divisao_float = numero1/numero2
print(divisao_float)

#divisao com resultado inteiro 

divisao_int= numero1 // numero2
print(divisao_int)

#divisao com resto
divisao_resto = numero1 % numero2
print(divisao_resto)
 
