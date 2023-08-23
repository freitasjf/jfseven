import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    try:
        nome_completo = input("Digite seu nome completo: ")
        ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))

        if ano_nascimento < 1922 or ano_nascimento > 2021:
            print("Ano de nascimento fora do intervalo válido.")
            return
        
        idade = calcular_idade(ano_nascimento)
        print(f"Nome: {nome_completo}")
        print(f"Idade em 2022: {idade} anos")

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um ano de nascimento válido.")

if __name__ == "__main__":
    main()
