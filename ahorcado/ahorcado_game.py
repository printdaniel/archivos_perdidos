import  time

name = input("Cómo te llamas?")

print(f'Hola: {name} ¡Es hora de jugar!')

time.sleep(1)
print("Comienza a adivinar")
time.sleep((0.5))

word = 'patranias'
your_word = ''
life = 5

while life > 0:
    fails = 0

    for char in word:
        if char in your_word:
            print(char,end='')
        else:
            print('*',end='')
            fails +=1
    if fails == 0:
        print("Felicidades, ganaste")
        break
            
    your_char =  input("Ingresa una letra: ")
    your_word += your_char

    if your_char not in word:
        life -= 1
        print("Esa letra no se encuentra en la palabra")
        print(f"Te quedan {life} intentos")

    if life == 0:
        print("Perdiste el juego")
else:
    print("Gracias por jugar")
