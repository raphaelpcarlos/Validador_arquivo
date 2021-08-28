

class Fatiamento():

    def __init__(self):
        self.dici = []
        self.conversao = []

    def cad_valores(self, nome='codigo',  inicio=0, fim=1):

        self.dici.append({'nome': nome,
            'inicio': inicio,
            'fim': fim})

    def retorno_fatiamento(self, arq):

        for e,a in enumerate(arq):

            self.conversao.append('-' * 20)
            for linha in self.dici:

                self.conversao.append(f"{e+1}:{linha['nome']}: {a[linha['inicio']:linha['fim']]}")

        self.conversao.append('-'*20)

    def listar_valores(self):

        lista = []
        for valor in self.dici:
            lista.append(f"{valor['nome']}: {valor['inicio']}/{valor['fim']}")

        return lista

    def apagar_lista_valores(self):


        self.dici.clear()



"""v = Fatiamento()

arquivo = list(open('arquivos/teste.txt', 'r'))


v.cad_valores(nome= 'codigo',inicio=0,fim=9)
v.cad_valores(nome= 'cep',inicio=78,fim=87)
v.cad_valores(nome= 'endereco',inicio=31,fim=56)

print(v.listar_valores())

v.retorno_fatiamento(arquivo)

for v in v.conversao:
    print(v)
"""












