from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurate_japa = Restaurante("Ni hao", "Japones")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")

restaurante_praca.receber_avaliacao('João', 8)
restaurante_praca.receber_avaliacao('Marcello', 9)
restaurante_praca.receber_avaliacao('Joana', 5)
restaurante_praca.receber_avaliacao('Daniela', 10)
restaurante_praca.receber_avaliacao('Felipe', 2)

def main():
    Restaurante.listar_restaurantes()
    print("")

if __name__ == "__main__":
    main()
