# Converço de moedas
# Com a utlização da função DEF 'def() para chamar a função e inicia automaticamente
# Utilizei tambêm a biblíoteca'os' que é o operacional system,
# que serve para utilizar funçôes do sistema dentro do código!
import requests  # usei essa biblioteca que serve para fazer uma interligação com outros sistemas e aplicações web
import os  # biblioteca que utilizei.
# De onde é puxado os dados vindos da web.
url = requests.get(
    'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL,GBP-BRL,JPY-BRL')
# é um formato aberto usado como alternativa ao XML para a transferência de
url_format = url.json()
# dados estruturados entre um servidor de Web e uma aplicação.
# DOALR onde puxo a informação do dolar.
dolar_hoje = url_format['USDBRL']['bid']
# A informação vem como string por isso eu faço a conversão de tipo.
dolar_hoje = float(dolar_hoje)
# EURO onde puxo a informação do euro.
euro_hj = url_format['EURBRL']['bid']
euro_hj = float(euro_hj)
# PESO...
peso_hj = url_format['ARSBRL']['bid']
peso_hj = float(peso_hj)
# LIBRA...
libra_hj = url_format['GBPBRL']['bid']
libra_hj = float(libra_hj)
# IENE...
iene_hoje = url_format['JPYBRL']['bid']
iene_hoje = float(iene_hoje)


def conve():

    # Menu de escolha

    print(' CONVERÇO DE MOEDAS ')
    print(20*'=')
    print('[1] DOLAS ')
    print('[2] PESSO')
    print('[3] EURO')
    print('[4] LIBRA ESTERLINA')
    print('[5] IENE ')
    # Onde iremos informa a escolha e o valor do usuario.
    escolha = input('Ecolha a moeda :')
    moeda = input('Informe o valor em reais:')
    print(20*'=')
    print("")

    # Onde eu chamo a função da biblioteca para apagar a lista de escolha.
    os.system('cls')
    try:  # vai tenta execulta a parte de baixo desse codigo

        # Onde eu faço a coerção de tipo.
        escolha_int = int(escolha)
        moeda_flo = float(moeda)
        # Onde faço os calculos para dar o resultados.
        resp_dolar = round(moeda_flo/dolar_hoje, 2)
        resp_euro = (moeda_flo/euro_hj)
        resp_peso = (moeda_flo/peso_hj)
        resp_libra = (moeda_flo/libra_hj)
        resp_iene = (moeda_flo/iene_hoje)
        # Onde começa operações condicionais.
        if escolha_int == 1: # Resultado do dolar.
            print('Você tem em reais: {}'.format(moeda_flo))
            print('O dolar tar: {}'.format(dolar_hoje))
            print('Em doloras [EUA] você tera: {}'.format(resp_dolar))
            print(20*'=')
            print("")

        elif escolha_int == 2: # Resultado do PESO.
            print('Você tem em reais: {}'.format(moeda_flo))
            print('O (PESO) hoje ta:  {}'.format(peso_hj))
            print('Em peso argetino você tera: {}'.format(resp_peso))
            print('')

        elif escolha_int == 3: # Resultado do EURO.
            print('Você tem em reais: {}'.format(moeda_flo))
            print('O (EURO) hoje ta {}'.format(euro_hj))
            print('Em EURO você tera: {}'.format(resp_euro))
            print(20*'=')
            print("")

        elif escolha_int == 4: # Resultado do LIBRA.
            print('Você tem em reais: {}'.format(moeda_flo))
            print('A (libra) hoje ta {}'.format(libra_hj))
            print('Em libra você tera:{}'.format(resp_libra))
            print(20*'=')
            print("")

        elif escolha_int == 5: # Resultado do IENE.
            print('você tem em reais:{}'.format(moeda_flo))
            print('O iene hoje ta {}'.format(iene_hoje))
            print('Em iene vc tera:{:.4}'.format(resp_iene))
            print(20*'==')
            print("")                               #vl

        else: # Se não digita nada.
            print('Você não digitou um numero') # Exibi isso.

    except:  # Se ocorre um erro no try ele entra no except e execulta esse print.
        print('Escolha um nuemro valido')

    conve()  # Chamei a função para inicia que der o resultado.


conve()  # Chamei novamente para iniciar o looping.
