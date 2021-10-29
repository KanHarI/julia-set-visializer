"""Package setup file"""

from setuptools import find_packages, setup  # type: ignore

__version__ = "0.1.0"

setup(
    name="JuliaSetVisualizer",
    version=__version__,
    packages=find_packages(exclude=["test"]),
    package_data={
        package: ["py.typed"] for package in find_packages(exclude=["tests"])
    },
    install_requires=["matplotlib", "numpy", "scipy"],
    entry_points={
        "console_scripts": ["julia_set_visualizer=julia_set_visualizer.main:main"]
    },
)
