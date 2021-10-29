"""Main module"""

import sys

import numpy as np
from matplotlib import pyplot as plt  # type: ignore

THRESHOLD = 3


def one_step(k: list[np.complex128]) -> list[np.complex128]:
    """Expand a list of K_n members into a list of K_n+1 members"""
    ret = []
    for m in k:
        new_ks: list[np.complex128] = list(np.roots([2, -3 * m, 0, 1]))  # type: ignore
        for new_m in new_ks:
            if np.abs(new_m) < THRESHOLD:
                ret.append(new_m)
    return ret


def upton(n: int) -> list[np.complex128]:
    """Returns the union K_0 U K_1 U ... U K_n"""
    tot: list[np.complex128] = [np.complex128(0)]
    k: list[np.complex128] = [np.complex128(0)]
    for _ in range(n):
        k = one_step(k)
        tot += k
    return tot


def main() -> int:
    """Main entry point"""
    data = upton(int(sys.argv[1]))
    # extract real part
    x = [ele.real for ele in data]
    # extract imaginary part
    y = [ele.imag for ele in data]
    # plot the complex numbers
    plt.scatter(x, y)
    plt.ylabel("Imaginary")
    plt.xlabel("Real")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
