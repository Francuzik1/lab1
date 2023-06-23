import numexpr as ne


def Meaning(mnogo: str, value: str):
    k = 0
    mnogo = list(mnogo)
    for i in mnogo:
        if i == 'x':
            mnogo[k] = value
        k += 1
    total = ''.join(mnogo)
    int_total = ne.evaluate(total)
    print(int_total)


Meaning('x**2', '2')
