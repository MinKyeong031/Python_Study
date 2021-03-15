class Drink:
    _SIZES = ['레귤러', '점보']# 0 : 레귤러, 1 : 점보
    _SUGAR = ['0%', '50%', '기본', '150%']# 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%
    _ICE = ['0%', '50%', '기본', '150%']# 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.size = 0 #0 : 레귤러, 1 : 점보
        self.sugar = 2  # 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%
        self.ice = 2  # 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%

    def set_size(self):
        size = input('사이즈를 고르세요. 0 : 레귤러, 1 : 점보\n')
        if size == '':
            size = 0
        else:
            self.size = int(size)

        if self.size == 1:
            self.price += 1000

    def set_sugar(self):
        sugar = input('당도를 고르세요. 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%\n')
        if sugar == '':
            sugar = 2
        else:
            self.sugar = int(sugar)

    def set_ice(self):
        ice = input('얼음량을 고르세요. 0 : 0%, 1 : 50%, 2 : 기본, 3 : 150%\n')
        if ice == '':
            ice = 2
        else:
            self.ice = int(ice)

    def order(self):
        self.set_size()
        self.set_sugar()
        self.set_ice()

    def __str__(self):
        return f'이름 : {self.name},\t가격 : {self.price},\t사이즈 : {Drink._SIZES[self.size]},\t당도 : {Drink._SUGAR[self.sugar]},\t얼음 : {Drink._ICE[self.ice]}'

if __name__ == '__main__':
    mk = Drink('하동녹차오레오', 3900)
    mk.set_size()
    mk.set_sugar()
    mk.set_ice()
    print(mk)