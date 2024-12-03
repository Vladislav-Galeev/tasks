# Данная функция использует логичсекое умножение. Битовые операции работают быстро, поэтому данная
# функция будет работать быстрее чем операция взятие остатка, это заметно при больших числах.
def isEven(number):
    return not (number & 1)


def TestIsEven():
    print(isEven(1))
    print(isEven(4))
    print(isEven(0))
    print(isEven(-5))
    print(isEven(-8))


if __name__ == "__main__":
    TestIsEven()