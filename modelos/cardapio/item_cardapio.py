from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome: str, preco: float) -> None:
        self._preco = preco
        self._nome = nome

    def __str__(self):
        return self._nome

    @abstractmethod
    def aplicar_desconto(self):
        pass
