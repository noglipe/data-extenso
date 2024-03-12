from datetime import date
import sys

#dicionários para conversção
meses = [" janeiro", " fevereiro", " março", " abril", " maio", " junho",
          " julho", " agosto", " setembro", " outubro", " novembro", " dezembro"]

ext = [
    {1:" primeiro", 2:" dois", 3:" três", 4:" quatro", 5:" cinco", 6:" seis", 7:" sete", 8:" oito", 9:" nove", 10:" dez", 11:" onze", 12:" doze",13:" treze", 14:" quatorze", 15:" quinze", 16:" dezesseis", 17:" dezessete", 18:" dezoito", 19:" dezenove"}, 
    {2:" vinte", 3:" trinta", 4:" quarenta", 5:" cinquenta", 6:" sessenta", 7:" setenta", 8:" oitenta", 9:" noventa"}, 
    {1:" cento", 2:" duzentos", 3:" trezentos", 4:" quatrocentos", 5:" quinhentos", 6:" seissentos", 7:" setessentos", 8:" oitocentos", 9:" novecentos"}
]

unidade = ['', ' mil', (' milhão', ' milhões'), (' bilhão', ' bilhões'), (' trilhão', ' trilhões')]

def converter_ano(valor):
    retorno = ''

    if valor[0]=='1':
        retorno = unidade[1]
    else:
        retorno = ext[0].get(int(valor[0])) + unidade[1]
    
    retorno = retorno + ext[2].get(int(valor[1])) + ' e'

    if int(valor[2]) > 1:
        retorno = retorno +  ext[1].get(int(valor[2]))
        retorno = retorno +  ext[0].get(int(valor[3]))
    else:
        retorno = retorno + ext[0].get(int(valor[2]))
            
    return retorno

def converter_data_extenso(dia, mes, ano):
    """
    Converte uma data para extenso.

    Args:
    dia: O dia da data.
    mes: O mês da data.
    ano: O ano da data.

    Returns:
    Uma string com a data em extenso.
    """

    por_extenso = ''

    if int(dia) > 19:
        por_extenso = ext[1].get(int(dia[0]))
        por_extenso = por_extenso +' e'+ ext[0].get(int(dia[1]))
    else:
        por_extenso = ext[0].get(int(dia[0]))

    mes= int(mes) - 1

    por_extenso = por_extenso + ' de'+ meses[mes] + ' de'+ converter_ano(ano)

    return por_extenso

def converte_data(data):
    """
    Converte uma data para extenso.

    Args:
    data: Data no formato date de DateTime.

    Returns:
    Uma string com a data em extenso.
    """
    data = str(data)
    try:
        ano, mes, dia = data.split('-')
    except:
        print ('Erro ao parsear o numero informado!')
        sys.exit(1)
    return converter_data_extenso(dia,mes,ano)


d = date(1987, 11, 18)
print(converte_data(d)[1:])
