from drink import Drink

class Coffee(Drink):
    pass

if __name__ == '__main__':
    mk = Coffee('모카라떼', 3000)
    mk.set_size()
    print(mk)