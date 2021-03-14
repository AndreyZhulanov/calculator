def sum_nums(a, b):
    return a + b


def main():
    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    operator = input('Введите операцию: ')

    if operator == '+':
        print(sum_nums(num1, num2))


if __name__ == '__main__':
    main()


