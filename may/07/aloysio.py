# Sol aloysio


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda x, y: x)


def cdr(pair):
    return pair(lambda x, y: y)


if __name__ == "__main__":
    pair = cons(2, 3)
    print(car(pair), cdr(pair))
