from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        espaco = 20
        espaco_status = espaco - 12
        print(f'{'Nome do restaurante'.ljust(espaco)} | {'Categoria'.ljust(espaco)} | {'Status'.ljust(espaco_status)} | {'Avaliação'}')
        print("")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(espaco)} | {restaurante._categoria.ljust(espaco)} | {restaurante.ativo.ljust(espaco_status)} | {str(restaurante.media_avaliacao) if restaurante.media_avaliacao else "Sem avaliações" }')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        nota = nota / 2
        nova_avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(nova_avaliacao)


    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return False
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
