#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <Eigen/Dense>
#include <iostream>

namespace py = pybind11;
using namespace Eigen;

// Función de Análisis Factorial
py::array_t<double> factor_analysis(const py::array_t<double>& input_array, int n_factors) {
    auto buf = input_array.request();
    int n_samples = buf.shape[0];
    int n_features = buf.shape[1];

    // Convertir NumPy a Eigen
    MatrixXd data(n_samples, n_features);
    memcpy(data.data(), buf.ptr, sizeof(double) * n_samples * n_features);

    // Centrar los datos (media cero)
    VectorXd mean = data.colwise().mean();
    MatrixXd centered_data = data.rowwise() - mean.transpose();

    // Calcular la matriz de covarianza
    MatrixXd covariance = (centered_data.transpose() * centered_data) / double(n_samples - 1);

    // Descomposición en valores propios
    SelfAdjointEigenSolver<MatrixXd> solver(covariance);
    VectorXd eigenvalues = solver.eigenvalues().reverse();
    MatrixXd eigenvectors = solver.eigenvectors().rowwise().reverse();

    // Selección de factores principales
    VectorXd sqrt_eigenvalues = eigenvalues.head(n_factors).cwiseSqrt();
    MatrixXd factors = centered_data * eigenvectors.leftCols(n_factors) * sqrt_eigenvalues.asDiagonal().inverse();

    // Convertir a NumPy
    std::vector<double> result_data(factors.size());
    memcpy(result_data.data(), factors.data(), sizeof(double) * factors.size());

    return py::array_t<double>({n_samples, n_factors}, result_data.data());
}

// Exportar a Python
PYBIND11_MODULE(fa_module, m) {
    m.def("factor_analysis", &factor_analysis, "Factor Analysis",
          py::arg("data"), py::arg("n_factors") = 2);
}
