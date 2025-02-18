from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurate_japa = Restaurante("Ni hao", "Japones")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")

bebida_suco = Bebida("Suco Melancia", 5.00, "grande")
prato_pao = Prato("Paozinho", 2.00, "O melhor pãozinho da cidade")

restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_pao)

prato_pao.aplicar_desconto()


def main():
    print(restaurante_praca.listar_cardapio)
    print("")


if __name__ == "__main__":
    main()
