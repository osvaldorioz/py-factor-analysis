from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension

#python3.12 setup.py build_ext --inplace

ext_modules = [
    Pybind11Extension(
        "fa_module",
        ["factor_analysis.cpp"],
        include_dirs=["/usr/include/eigen3"],  # Asegurar que se incluya Eigen
        extra_compile_args=["-O3"],  # Optimización
    )
]

setup(
    name="fa_module",
    version="1.0",
    ext_modules=ext_modules,
    zip_safe=False,
)
