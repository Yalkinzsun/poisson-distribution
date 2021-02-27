import math
import random
import collections
import matplotlib.pyplot as plt


def getPoisson(lam, n):
    m, new_res_y = [], []
    def getM(lam):
        p = math.exp(-lam)
        q = 1.0
        m = 0
        while True:
            m += 1
            q = q * random.random()
            if q < p:
                break
        return m-1

    for i in range(1, n):
        _m = getM(lam)
        m.append(_m)
    m.sort()
    counter = collections.Counter(m)
    res_x, res_y = counter.keys(), counter.values()

    for j in res_y:
        new_res_y.append(j / n)
    return res_x, new_res_y


if __name__ == '__main__':
    lam = 5
    res_x, new_res_y = getPoisson(lam, 1000)
    plt.step(res_x, new_res_y, label=f'λ = {lam}')
    plt.title('Poisson Distribution')
    plt.legend()
    plt.ylabel('p (x | λ)')
    plt.xlabel('x')
    plt.show()
