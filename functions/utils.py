from datetime import datetime


def is_float(num: str):
    try:
        num = num.replace(',', '.')
        float(num)
        return True
    except ValueError:
        return False
    

def is_date(date: str):
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    

def is_string_com_mesmos_caracteres(texto: str):
    for letra in texto:
        if letra != texto[0]:
            return False
    return True
    

def is_cpf(cpf: str):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) == 11 and cpf.isdigit() and not is_string_com_mesmos_caracteres(cpf):
        digitos_cpf = [int(n) for n in cpf[:9]]
        multiplicadores = range(10, 1, -1)
        soma = sum([multiplicadores[i] * digitos_cpf[i] for i in range(9)])
        primeiro_digito = 0 if soma % 11 < 2 else 11 - soma % 11

        if primeiro_digito != int(cpf[9]):
            return False
        
        digitos_cpf.append(primeiro_digito)
        multiplicadores = range(11, 1, -1)
        soma = sum([multiplicadores[i] * digitos_cpf[i] for i in range(10)])
        segundo_digito = 0 if soma % 11 < 2 else 11 - soma % 11

        return segundo_digito == int(cpf[10])
    else:
        return False
