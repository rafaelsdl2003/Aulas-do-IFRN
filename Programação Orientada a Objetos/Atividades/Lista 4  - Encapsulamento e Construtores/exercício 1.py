class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)
    def set_destino(self, nome):
        if nome == "":
            raise ValueError("Informe um nome válido")
        else:
            self.__destino = nome
    def set_distancia(self, valor):
        if valor >= 0:
            self.__distancia = valor
        else:
            raise ValueError("Informe um valor válido")
    def set_litros(self, valor):
        if valor > 0:
            self.__litros = valor
        else:
            raise ValueError("Informe um valor válido")
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def __str__(self):
        return f"Destino {self.__destino} - Distância {self.__distancia}km - Litros {self.__litros}L - Consumo {self.consumo():.2f}km/L"
class ViagemUI:
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: 
                ViagemUI.viagem()
    def menu():
        print("1-Viagem, 2-Fim")
        return int(input("Escolha uma opção: "))
    def viagem():
        print("Cálculo da Viagem")
        destino = input("Informe o destino: ")
        distancia = float(input("Informe a distância: "))
        litros = float(input("Informe litros: "))
        x = Viagem(destino, distancia, litros)
        print(x)
ViagemUI.main()