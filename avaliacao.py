

class Carro:
    def __init__(self, nome, placa, cor, modelo):
        self.nome = nome
        self.placa = placa
        self.cor = cor
        self.modelo = modelo


if __name__ == "__main__":
    carro1 = Carro("Pálio", "PCG0731", "preto", "M2018") 
    carro2 = Carro("Fiesta", "PEA1C95", "branco", "M2015") 
    carro3 = Carro("Corolla", "IAN2007", "cinza", "M2020") 
    print(carro1.nome) 
    print(carro1.placa) 
    print(carro1.cor) 
    print(carro1.modelo) 
    print("\n")
    print(carro2.nome) 
    print(carro2.placa) 
    print(carro2.cor) 
    print(carro2.modelo) 
    print("\n")
    print(carro3.nome) 
    print(carro3.placa) 
    print(carro3.cor) 
    print(carro3.modelo) 