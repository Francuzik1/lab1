class Polynomial:
    def __init__(self, koef):
        self.koef = koef

    def __call__(self, x):
        s = 0
        for i in range(len(self.koef)):
            s += self.koef[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        k = Polynomial(st)
        if len(self.koef) < len(other.koef):
            m = len(self.koef)
        else:
            m = len(other.koef)
        for i in range(m):
            st.append(self.koef[i] + other.koef[i])
        if len(self.koef) > m:
            st += self.koef[m::]
        else:
            st += other.koef[m::]
        k.koef = st
        return k
poly_1 = Polynomial([10, -1])
poly_1_test = poly_1(1)
poly_2 = Polynomial([11, -1])
polu_2_test = poly_2(2)
print(poly_1_test+polu_2_test)
