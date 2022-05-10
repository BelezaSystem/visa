import json
import requests


def valida_cnpj(cnpj):
    'Recebe um CNPJ e retorna True se formato válido ou False se inválido'

    cnpj = parse_input(cnpj)
    if len(cnpj) != 14 or not cnpj.isnumeric():
        return False

    verificadores = cnpj[-2:]
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    'Calcular o primeiro digito verificador'
    soma = 0
    for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-2]))):
        soma += int(numero) * int(lista_validacao_um[ind])

    soma = soma % 11
    digito_um = 0 if soma < 2 else 11 - soma

    'Calcular o segundo digito verificador'
    soma = 0
    for numero, ind in zip(cnpj[:-1], range(len(cnpj[:-1]))):
        soma += int(numero) * int(lista_validacao_dois[ind])

    soma = soma % 11
    digito_dois = 0 if soma < 2 else 11 - soma

    return verificadores == str(digito_um) + str(digito_dois)


def parse_input(i):
    'Retira caracteres de separação do CNPJ'

    i = str(i)
    i = i.replace('.', '')
    i = i.replace(',', '')
    i = i.replace('/', '')
    i = i.replace('-', '')
    i = i.replace('\\', '')

    return i


def busca_cnpj(cnpj):
    url = 'https://receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
    response = requests.request("GET", url)
    dic = json.loads(response.text)
    cnaes = []

    if dic['status'] == "ERROR":
        return 'CNPJ {0} rejeitado pela receita federal\n\n'.format(cnpj)
    else:
        try:
            # Atividade Principal
            cnaes.append(dic['atividade_principal'][0]['code'])

            # Atividades secundárias
            for elem in dic['atividades_secundarias']:
                cnaes.append(elem['code'])

            return cnaes
        except KeyError:
            pass


def pega_resultado(cnpj):
    if not valida_cnpj(cnpj):
        return 'CNPJ "{0}" tem formato inválido'.format(cnpj)
    else:
        return busca_cnpj(parse_input(cnpj))
