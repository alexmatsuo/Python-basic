def fatorial(number):
    fat = 1
    for i in range (1,number+1):
        fat = fat * i
    return fat

def recursivefatorial(number): 
    if number == 1:
        return 1
    else:
        return number * recursivefatorial(number-1)

numero = int(input("Digite um número: "))

print(fatorial(numero))
print(recursivefatorial(numero))