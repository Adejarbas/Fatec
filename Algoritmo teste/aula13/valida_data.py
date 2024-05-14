from datetime import datetime

def valida_data(data):
    try:
        data_nasc = datetime.strptime(data, "%d/%m/%Y")
        hoje = datetime.now().date()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade >= 18
    except ValueError:
        return False

if __name__ == "__main__":
    data = input("Digite a data de nascimento no formato dd/mm/aaaa: ")
    if valida_data(data):
        print("Data válida e pessoa maior de idade.")
    else:
        print("Data inválida ou pessoa menor de idade.")
