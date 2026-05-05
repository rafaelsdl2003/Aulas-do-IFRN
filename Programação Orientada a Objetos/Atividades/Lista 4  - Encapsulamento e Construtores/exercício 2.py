class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao) 
        self.set_area(area)
    def set_nome(self, nome):
        if nome == "": 
            raise ValueError("Informe um valor válido")
        else:
            self.__nome = nome
    def set_populacao(self, populacao):
        if populacao > 0: 
            self.__populacao = populacao
        else:
            raise ValueError("Informe um valo válido")
    def set_area(self, area):
        if area > 0: 
            self.__area = area
        else:
            raise ValueError("Informe um valor válido")
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade_demografica(self):
        return self.__populacao / self.__area
    def __str__(self):
        return f"{self.__nome} tem densidade demográfica de {self.densidade_demografica():.2f}"
class PaisUI:
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1:
                PaisUI.pais()
    def menu():
        print("1-Densidade, 2-Fim")
        return int(input("Escolha uma opção: "))
    def pais():
        nome = input("Informe o nome do pais: ")
        populacao = int(input("Informa a quantidade de habitantes: "))
        area = float(input("Informe a área do pais: "))
        x = Pais(nome, populacao, area)
        print(x)
PaisUI.main()