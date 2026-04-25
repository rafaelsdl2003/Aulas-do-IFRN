# Entidades
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, base):
        if base >= 0: 
            self.__b = base
        else: 
            raise ValueError("Valor inválido")
    def set_altura(self, altura):
        if altura >= 0: 
            self.__h = altura
        else: 
            raise ValueError("Valor inválido")
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
class Circulo:
    def __init__(self):
        self.__raio = 0.0  
    def set_raio(self, raio):
        if raio >= 0.0: 
            self.__raio = raio
        else: 
            raise ValueError("Valor inválido")   
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return 3.14 * self.__raio**2
    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0  
    def set_distancia(self, distancia):
        if distancia > 0:
            self.__distancia = distancia
        else:
            raise ValueError("Valor inválido")
    def set_tempo(self, tempo):
        if tempo > 0:
            self.__tempo = tempo
        else:
            raise ValueError("Valor inválido")
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo
class Conta:
    def __init__(self):
        self.__nome = ""
        self.__numero = ""
        self.__saldo = 0.0
    def set_nome(self, nome):
        if len(nome) >= 3:
            self.__nome = nome
        else:
            raise ValueError("Valor inválido")
    def get_nome(self):
        return self.__nome
    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            raise ValueError("Valor inválido")
    def get_saldo(self):
        return self.__saldo
    def deposito(self, deposito):
        if deposito > 0:
            self.__saldo += deposito
            return deposito
        else:
            raise ValueError("Valor inválido")
    def saque(self, saque):
        if saque <= 0:
            raise ValueError("Valor inválido")
        elif saque > self.__saldo:
            raise ValueError("Valor inválido")
        else:
            self.__saldo -= saque
class Cinema:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0
    def set_dia(self, dia): 
        if dia in ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]:
            self.__dia = dia
        else:
            raise ValueError("Informe um dia válido, por exemplo, segunda; terça; quarta; quinta; sexta; sábado ou domingo")
    def get_dia(self):
        return self.__dia
    def set_hora(self, hora):
        if 7<= hora <= 23 or hora == 00:
            self.__hora = hora
        elif 1<= hora <=6:
            raise ValueError("Os funcionários do cinema estão dormindo, o cinema abre de 7 às 00")
        else:
            raise ValueError("Informe uma hora válida")
    def get_hora(self):
        return self.__hora
    def entrada_inteira(self):
        if self.__dia in ["segunda", "terça", "quinta"]:
            if 17<= self.__hora <= 23 or self.__hora == 00:
                return 16 * 150 // 100 
            return 16
        elif self.__dia in ["sexta", "sábado", "domingo"]:
            if 17<= self.__hora <= 23 or self.__hora == 00:
                return 20 * 150 // 100
            return 20
    def meia_entrada(self):
        if self.__dia in ["segunda", "terça", "quinta"]:
            if 00<= self.__hora <= 17:
                return (16 * 150 // 100) // 2 
            return 16 // 2
        elif self.__dia in ["quarta"]:
            return 8
        elif self.__dia in ["sexta", "sábado", "domingo"]:
            if 00<= self.__hora <= 17:
                return (20 * 150 // 100) // 2
            return 20 // 2
# Interface com o usuário
class UI:
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta()
            if op == 5: UI.cinema()
    def menu():
        print("1-Área do Triângulo, 2-Área e Circunferencia do Círculo, 3-Velocidade Média da Viagem, 4-Conta Bancária, 5-Conta de Cinema e 6-Fim")
        op = int(input("Escolha uma opção: "))
        return op  
    def triangulo():
        print("Área do Triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área igual {x.calc_area()}")
    def circulo():
        print("Área e Circunferencia do Círculo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor do raio: ")))
        print(f"Um círculo com raio {x.get_raio()} tem área = {x.calc_area()} e circunferência = {x.calc_circunferencia()}")
    def viagem():
        print("Velocidade Média da Viagem")
        x = Viagem()
        x.set_distancia(float(input("Informe o valor da distância: ")))
        x.set_tempo(float(input("Informe o valor do tempo: ")))
        print(f"A velocidade média da viagem foi {x.velocidade_media():.2f}km/h")
    def conta():
        print("Conta Bacária")
        x = Conta()
        x.set_nome(input("Informe o seu nome: "))
        x.set_numero(int(input("Informe o número da conta: ")))
        saldo_inicial = float(input("Informe o saldo da conta: "))
        x.set_saldo(saldo_inicial)
        deposito = float(input("Informe o deposito: ")) 
        x.deposito(deposito)
        print(f"{x.get_nome()} da conta {x.get_numero()} tem um saldo de R${saldo_inicial:.2f} e depositou R${deposito:.2f}, ficando com saldo R${saldo_inicial+deposito:.2f}")
        saque = float(input("Informe o saque: "))
        x.saque(saque)
        print(f"{x.get_nome()} da conta {x.get_numero()} sacou R${saque:.2f} e ficou com saldo R${x.get_saldo():.2f}")
    def cinema():
        print("Conta de Cinema")
        x = Cinema()
        x.set_dia(input("Informe o dia da semana: "))
        x.set_hora(int(input("Informe a hora: ")))
        if x.get_dia() == "quarta":
            print(f"No dia da semana, {x.get_dia()}, todo mundo paga meia, no valor de R${x.meia_entrada():.2f}, marcado às {x.get_hora()} hora")
        else:
            print(f"R${x.entrada_inteira():.2f} valor da inteira, no dia da semana, {x.get_dia()}, marcado às {x.get_hora()} hora")
            print(f"R${x.meia_entrada():.2f} valor da meia, no dia da semana, {x.get_dia()}, marcado às {x.get_hora()} hora")
UI.main()