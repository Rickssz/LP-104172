import os

os.system("cls || clear")

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a n1 do aluno: "))
n2 = float(input("Digite a n2 do aluno: "))

soma = n1 + n2
media = soma / 2

# 1. Define APENAS o conceito com base na média
if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

print(f"\nAluno: {nome}")
print(f"Média: {media:.1f}")

# 2. Mostra o conceito separadamente
print(f"Seu conceito é: {conceito}")

# 3. Define e mostra a situação separadamente (A, B, C -> Aprovado | D, E -> Reprovado)
if conceito in ["A", "B", "C"]:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")