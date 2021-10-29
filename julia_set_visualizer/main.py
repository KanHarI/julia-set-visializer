
import sys

import numpy as np

from matplotlib import pyplot as plt

THRESHOLD = 3

def one_step(k): 
    ret = [] 
    for m in k: 
        new_ks = list(np.roots([2, -3*m, 0, 1]))
        for new_m in new_ks:
            if np.abs(new_m) < THRESHOLD:
                ret.append(new_m)
    return ret

def upton(n):
    tot = [0]
    k = [0]
    for i in range(n):
       k = one_step(k) 
       tot += k
    return tot

def main():
    data = upton(int(sys.argv[1]))
    # extract real part
    x = [ele.real for ele in data]
    # extract imaginary part
    y = [ele.imag for ele in data]
    # plot the complex numbers
    plt.scatter(x, y)
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

if __name__ == "__main__":
    main()
