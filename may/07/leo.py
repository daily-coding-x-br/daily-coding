def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def id(a,b):
        return a,b
    return f(id)[0]    

def cdr(f):
    def id(a,b):
        return a,b
    return f(id)[1]  