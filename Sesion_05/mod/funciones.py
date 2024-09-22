def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplica(x, y):
    return x * y


def division(x, y):
    return x / y


def impuesto(x):
    if x > 500:
        imp = x * 0.08
        print('Usted debe pagar: {} soles.'.format(imp))
    else:
        print('Usted no dede pagar impuestos.')
