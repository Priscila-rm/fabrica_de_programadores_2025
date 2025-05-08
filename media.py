# Voce foi contratado para criar um programa de calculo de media de notas escolares
# Esse programa recebera duas notas e calculara a media
#1. Solicitar o input das notas numericas [int ou float]

nota1= int(input("insira a primeira nota da divisao: "))
nota2= int(input("insira a segunda nota da divisao: "))

#2. Realizar o calculo de media = (nota1 +nota2)/2

media = (nota1 + nota2) / 2
print(media)

#3. Verificar se o aluno foi aprovado ou reprovado, para isso vamos fazer uma comparação.
if media >= 5:
    print("aprovado")
else: 
    print("reprovado")
