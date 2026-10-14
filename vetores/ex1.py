import os
os.system('cls')

notas = []

for i in range(3):
    
    nt = int(input(f'Digite sua {i+1} notas: '))
    notas.append(nt)
    media = sum(notas) / len(notas)

print(notas)
print(media)

