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

def converter_ano(ano):
    por_extenso = ''

    if ano[0]=='1':
        por_extenso = unidade[1]
    else:
        por_extenso = ext[0].get(int(ano[0])) + unidade[1]
    
    por_extenso = por_extenso + ext[2].get(int(ano[1])) + ' e'

    if int(ano[2]) > 1:
        por_extenso = por_extenso +  ext[1].get(int(ano[2]))
        por_extenso = por_extenso +  ext[0].get(int(ano[3]))
    else:
        por_extenso = por_extenso + ext[0].get(int(ano[2]))
            
    return por_extenso

def converter_dia(dia):
    por_extenso = ''

    if int(dia) > 19:
        por_extenso = ext[1].get(int(dia[0]))
        por_extenso = por_extenso +' e'+ ext[0].get(int(dia[1]))
        return por_extenso[1:]
    else:
        return ext[0].get(int(dia[0]))[1:]

def converter_mes(mes):

    mes= int(mes) - 1

    return meses[mes]


def converter_data_extenso(dia, mes, ano):

    por_extenso = converter_dia(dia)
    por_extenso = por_extenso + ' de'+ converter_mes(mes)
    por_extenso = por_extenso + ' de' +converter_ano(ano)

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


class DataPorExtenso:
    """
    Classe que converte uma data para extenso.

    Atributos:

        data_por_extenso: A data em extenso.

    Métodos:

        __init__(self, data): Construtor da classe.
        _converter_dia(self): Converte o dia para extenso.
        _converter_mes(self): Converte o mês para extenso.
        _converter_ano(self): Converte o ano para extenso.
    """

    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
          "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    ext = [
        {1:"primeiro", 2:" ois", 3:"três", 4:"quatro", 5:"cinco", 6:"seis", 7:"sete", 8:"oito", 9:"nove", 10:"dez", 11:"onze", 12:"doze",13:"treze", 14:"quatorze", 15:"quinze", 16:"dezesseis", 17:"dezessete", 18:"dezoito", 19:"dezenove"}, 
        {2:"vinte", 3:"trinta", 4:"quarenta", 5:"cinquenta", 6:"sessenta", 7:"setenta", 8:"oitenta", 9:"noventa"}, 
        {1:"cento", 2:"duzentos", 3:"trezentos", 4:"quatrocentos", 5:"quinhentos", 6:"seissentos", 7:"setessentos", 8:"oitocentos", 9:"novecentos"}
    ]

    unidade = ['', 'mil', (' milhão', ' milhões'), (' bilhão', ' bilhões'), (' trilhão', ' trilhões')]

    def __init__(self, data):

        

        self.data = str(data)

        self.ano, self.mes, self.dia = self.data.split('-')
        
        self.ano_por_extenso =''
        self.mes_por_extenso= ''
        self.dia_por_extenso = ''
        self.data_por_extenso = ''
        
        print(self.dia)
        self._converter_dia()
        self._converter_mes()
        self._converter_ano()

        self.data_por_extenso= self.dia_por_extenso +' de '+ self.mes_por_extenso + ' de ' + self.ano_por_extenso
   
    def _converter_dia(self):

        if int(self.dia) > 19:
            self.dia_por_extenso = self.ext[1].get(int(self.dia[0]))
            self.dia_por_extenso = self.dia_por_extenso +' e'+ self.ext[0].get(int(self.dia[1]))
        else:
            self.dia_por_extenso = self.ext[0].get(int(self.dia))

    def _converter_mes(self):

        mes= int(self.mes) - 1
        self.mes_por_extenso = self.meses[mes]

    def _converter_ano(self):

        if self.ano[0]=='1':
            self.ano_por_extenso = self.unidade[1] + ' '
        else:
            self.ano_por_extenso = self.ext[0].get(int(self.ano[0])) + self.unidade[1]
        
        self.ano_por_extenso = self.ano_por_extenso + self.ext[2].get(int(self.ano[1])) + ' e '

        if int(self.ano[2]) > 1:
            self.ano_por_extenso = self.ano_por_extenso +  self.ext[1].get(int(self.ano[2]))
            self.ano_por_extenso = self.ano_por_extenso + ' e ' + self.ext[0].get(int(self.ano[3]))
        else:
            self.ano_por_extenso = self.ano_por_extenso + self.ext[0].get(int(self.ano[2]))

d = date(1987, 11, 18)
x = DataPorExtenso(d)
x = DataPorExtenso(d)
print(x.data_por_extenso)
