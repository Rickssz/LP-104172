morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

print("1. Texto para Morse")
print("2. Morse para texto")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    texto = input("Digite o texto: ").upper()

    resultado = ""

    for letra in texto:
        if letra == " ":
            resultado += "/ "
        elif letra in morse:
            resultado += morse[letra] + " "

    print("Morse:", resultado)

elif opcao == "2":
    codigo = input("Digite o código Morse: ")

    inverso = {valor: chave for chave, valor in morse.items()}

    palavras = codigo.split(" / ")
    resultado = ""

    for palavra in palavras:
        letras = palavra.split()
        for letra in letras:
            if letra in inverso:
                resultado += inverso[letra]
        resultado += " "

    print("Texto:", resultado)

else:
    print("Opção inválida!")
