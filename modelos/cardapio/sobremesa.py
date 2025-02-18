from modelos.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, descricao, tamanho) -> None:
        super().__init__(nome, preco)
        self._tipo = tipo
        self._descricao = descricao
        self._tamanho = tamanho

    def __str__(self):
        return super().__str__()

    def aplicar_desconto(self):
        self._preco *= 0.98
