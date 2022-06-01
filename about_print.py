texto = "Probando print"
numero = 152022
fin = 'fin'

print(f"{'{ Título 1 }':=^80}")
print('')
for i in [1,2,3]:
    print(f"{'Iteración '+str(i):.>80}")

print('')
print(f"{'{ Título 2 }':=^80}")
print(f"{'Texto 1':-<80}")
print(f"{'Texto 2: '+texto:-<80}")
print(f"{'Número: ' + str(numero):-<80}")
print('')
print('Otra forma'.ljust(80,'-'))
print('Otra forma'.rjust(80,'-'))
print('Otra forma'.center(80,'-'))
print('')
print("{: >80}".format(f'Otra forma, {fin}'))
