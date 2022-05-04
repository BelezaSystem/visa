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
    url = 'http://receitaws.com.br/v1/cnpj/{0}'.format(cnpj)
    response = requests.request("GET", url)
    dic = json.loads(response.text)

    if dic['status'] == "ERROR":
        print('CNPJ {0} rejeitado pela receita federal\n\n'.format(cnpj))
    else:
        try:
            print('Nome: {0}'.format(dic['nome']))
            print('Nome fantasia: {0}'.format(dic['fantasia']))
            print('CNPJ: {0}   Data de abertura: {1}'.format(dic['cnpj'], dic['abertura']))
            print('Natureza: {0}'.format(dic['natureza_juridica']))
            print('Situação: {0}  Situação especial: {1}  Tipo: {2}'.format(dic['situacao'],
                                                                            dic['situacao_especial'],
                                                                            dic['tipo']))
            print('Motivo Situação especial: {0}'.format(dic['motivo_situacao']))
            print('Data da situação: {0}'.format(dic['data_situacao']))
            print('Atividade principal:')
            print(' ' * 10 + '{0} - {1}'.format(dic['atividade_principal'][0]['code'],
                                                dic['atividade_principal'][0]['text']))
            print('Atividades secundárias:')
            for elem in dic['atividades_secundarias']:
                print(' ' * 10 + '{0} - {1}'.format(elem['code'], elem['text']))

            print('Endereço:')
            print(' ' * 10 + '{0}, {1}'.format(dic['logradouro'],
                                               dic['numero']))
            print(' ' * 10 + '{0}'.format(dic['complemento']))
            print(' ' * 10 + '{0}, {1}'.format(dic['municipio'],
                                               dic['uf']))
            print('Telefone: {0}'.format(dic['telefone']))
            print('Email: {0}\n\n'.format(dic['email']))
        except KeyError:
            pass


def pega_resultado(cnpj):
    # cnpj = input('Digite o CNPJ\n')
    if not valida_cnpj(cnpj):
        print('CNPJ "{0}" tem formato inválido'.format(cnpj))
    else:
        busca_cnpj(parse_input(cnpj))
