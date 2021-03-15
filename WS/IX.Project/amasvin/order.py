from coffee import Coffee
from bubbletea import Bubbletea

class Order:
    def __init__(self):
        self.menu = []
        self.order_menu = []
        self.set_menu()

    def set_menu(self):
        self.menu.append(Coffee('아메리카노', 1800))
        self.menu.append(Bubbletea('타로버블티', 3200))

    def show_menu(self):
        for i, drink in enumerate(self.menu):
            print(f'{i+1}. {drink}')

    def add_order_menu(self):
        while True:
            self.show_menu()

            numer = input('메뉴를 선택하세요: ')

            if numer == '1':
                new_drink = Coffee('아메리카노', 1800)
            elif numer == '2':
                new_drink = Bubbletea('타로버블티', 3200)

            new_drink.order()

            self.order_menu.append(new_drink)

            is_add = input('더 주문하시겠습니까? (y/n) ')

            if is_add == 'n' or is_add == '':
                break

    def sum_price(self):
        total_price = 0
        for drink in self.order_menu:
            total_price += drink.price
        return total_price

    def __str__(self):
        s = '-'*20+'주문 내역'+'-'*20+'\n'
        for drink in self.order_menu:
            s += str(drink) + '\n'
        s += f'총 금액은 {self.sum_price()}원 입니다.'
        return s

if __name__ =='__main__':
    order = Order()
    order.add_order_menu()
    print(order)