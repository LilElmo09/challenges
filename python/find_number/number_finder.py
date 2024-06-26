def finder(max, list):
    sum_esperada = max*(max+1)//2
    sum_real = sum(list)
    return sum_esperada - sum_real

list = [0,3,4,2,8,7,6,9,5]
max = max(list)
resultado = finder(max, list)
print(f'el numero faltante es: {resultado}')