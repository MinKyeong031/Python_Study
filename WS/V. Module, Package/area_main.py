import area2

if __name__ == '__main__':
    area2.print_area(10, 20)
    area2.print_area(20, 30)

    for i in range(11, 15):
        area2.print_area(i, 20)

    print(f'가로 30 세로 10인 사각형의 넓이는 {area2.print_area(30, 10)}')
    print(area2.__name__)