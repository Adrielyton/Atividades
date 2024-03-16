class Radio:
    id = 0
    def __init__(self,marca,modelo,volume_maximo = 100):
        Radio.id += 1
        self.cod = Radio.id
        self.marca = marca
        self.modelo = modelo
        self.volume_maximo = volume_maximo
        self.volume_atual = 0 
        self.estado = 'desligado'

    def __str__(self):
        return f' Codigo: {self.cod} \n Marca: {self.marca} \n Modelo: {self.modelo} \n Volume-max: {self.volume_maximo}'
                

    def ligar(self):
        if self.estado == 'ligado':
            print(f' O Rádio Já encontra-se {self.estado} !')
        else:
            self.estado = 'ligado'
            print(f' O Rádio foi {self.estado}!')

    def desligar(self):
        if self.estado == 'desligado':
            print(f' O Rádio já encontra-se {self.estado}!')
        else:
            self.estado = 'desligado'
            print(f' O Rádio foi {self.estado}!')


    def aumentar_volume(self,quantidade = 1):
        if self.estado == 'ligado':
            if self.volume_atual + quantidade > self.volume_maximo:
                print(f' O volume máximo é de {self.volume_maximo}db.')
            
            elif self.volume_atual > quantidade:
                print(' Não é possível diminuir o volume, use a função correta!')
                
            elif self.volume_atual + quantidade <= self.volume_maximo:
                self.volume_atual += quantidade
                print(f" O volume foi aumentado para {self.volume_atual}db.")
            
            elif  quantidade == 1:
                self.volume_atual += quantidade
                print(f'O volume foi aumentado para {self.volume_atual}db') 
        else:
            print(" O rádio está desligado. Não é possivel aumentar!")

    def diminuir__volume(self,quantidade = 1):
        if self.estado == 'ligado':
            if self.volume_atual - quantidade < 0:
                print(f' Não é possível diminuir volume abaixo de 0')
            
            elif self.volume_atual <  quantidade:
                print(' Não é possível aumentar o volume, use a função correta!')
            
            elif  quantidade == 1:
                self.volume_atual -= quantidade
                print(f' O volume foi diminuido para {self.volume_atual}db')
        else:
            print(' O rádio está desligado. Não é possivel Diminuir!')


radio1 = Radio('motorola','xy350',60)
print(radio1)

radio1.aumentar_volume(12)
radio1.diminuir__volume(12)
radio1.ligar()
radio1.aumentar_volume(45)
radio1.aumentar_volume(5)
radio1.diminuir__volume(7)
radio1.diminuir__volume(10)
radio1.desligar()

print('--------------------------------------')

radio2 = Radio('samsung','sag55',80)
radio2.estado = 'ligado'
print(radio2)

radio2.ligar()
radio2.aumentar_volume(57)
radio2.desligar()
radio2.desligar()
radio2.diminuir__volume(30)

print('---------------------------------------')

radio3 = Radio('multilaser', 'ml005')
print(radio3)
radio3.aumentar_volume(20)
radio3.ligar()
radio3.aumentar_volume()
radio3.diminuir__volume()
