"""Main module"""
import itertools
import sys

import numpy as np
import scipy.spatial  # type: ignore
from matplotlib import pyplot as plt  # type: ignore

THRESHOLD = 3
MIN_DISTANCE = 2e-4


def one_step(
    k: list[np.complex128], existing_points_tree: scipy.spatial.cKDTree
) -> list[np.complex128]:
    """Expand a list of K_n members into a list of K_n+1 members"""
    ret = []
    for m in k:
        new_ks: list[np.complex128] = list(np.roots([2, -3 * m, 0, 1]))  # type: ignore
        for new_m in new_ks:
            if np.abs(new_m) > THRESHOLD:
                continue
            distance, _closest_point = existing_points_tree.query(
                [new_m.real, new_m.imag]
            )
            if distance < MIN_DISTANCE:
                continue
            ret.append(new_m)
    return ret


def upton(n: int) -> list[tuple[int, list[np.complex128]]]:
    """Returns the union K_0 U K_1 U ... U K_n"""
    tot: list[tuple[int, list[np.complex128]]] = [(0, [np.complex128(0)])]
    k: list[np.complex128] = [np.complex128(0)]

    kdtree_data = np.array(
        [
            [ele.real, ele.imag]
            for ele in itertools.chain.from_iterable(x[1] for x in tot)
        ]
    )
    kdata_tree = scipy.spatial.cKDTree(kdtree_data)

    for i in range(n):
        print(f"Iteration: {i}, active set size: {len(k)}")
        k = one_step(k, kdata_tree)
        tot.append((i + 1, k))

        kdtree_data = np.array(
            [
                [ele.real, ele.imag]
                for ele in itertools.chain.from_iterable(x[1] for x in tot)
            ]
        )
        kdata_tree = scipy.spatial.cKDTree(kdtree_data)
    return tot


def main() -> int:
    """Main entry point"""
    data = upton(int(sys.argv[1]))
    x: list[np.float64] = []
    y: list[np.float64] = []
    sizes: list[float] = []

    for k_num, pts in data:
        for point in pts:
            x.append(point.real)
            y.append(point.imag)
            sizes.append(200 * 0.6 ** k_num)

    plt.scatter(x, y, s=sizes)
    plt.ylabel("Imaginary")
    plt.xlabel("Real")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
