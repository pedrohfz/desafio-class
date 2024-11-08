# Define a classe 'Heroi' que representa o herói usado na aventura.
class Heroi:
    # Método __init__ é o construtor, sempre será chamado ao criar um novo herói.
    def __init__(self, nome, idade, tipo):
        # Atributos dos Heróis
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # Define a função que simula o ataque do herói, com descrição do ataque baseado no tipo.
    def realizar_ataque(self):
        # Verifica o tipo do herói e define o tipo de ataque.
        if self.tipo== 'Mago':
            ataque = "Magia: Bola de Fogo"
        elif self.tipo == 'Guerreiro':
            ataque = "Espada: Esgrima Mortal"
        elif self.tipo == 'Ladino':
            ataque = "Adaga: Ataque Furtivo"
        elif self.tipo == 'Bardo':
            ataque = "Flauta Mística: Música de Bardo"
        else:
            # Caso o tipo do herói seja desconhecido, exibe mensagem padrão.
            ataque = "Realizou um Ataque Desconhecido!"

        # Exibe a mensagem de ataque com o tipo de herói e descrição do ataque.
        print(f"O {self.tipo} atacou usando {ataque}")

# Exemplos de uso da classe 'Heroi'.

heroi1 = Heroi("Gandalf", 2000, "Mago")
heroi1.realizar_ataque()

heroi2 = Heroi("Alexandre", 32, "Guerreiro")
heroi2.realizar_ataque()

heroi3 = Heroi("John", 31, "Ladino")
heroi3.realizar_ataque()

heroi4 = Heroi("William", 52, "Bardo")
heroi4.realizar_ataque()