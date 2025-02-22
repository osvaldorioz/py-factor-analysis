from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
from typing import List
import matplotlib
import matplotlib.pyplot as plt
import fa_module 
import json

matplotlib.use('Agg')  # Usar backend no interactivo
app = FastAPI()

# Definir el modelo para el vector
class VectorF(BaseModel):
    vector: List[float]
    
@app.post("/factor-analysis")
def calculo(num_points: int, num_features: int, num_factors: int):
    output_file_1 = 'fa-dispersion.png'
    output_file_2 = 'fa-varianza.png'
    
    # 🔹 Generar datos de prueba (100 muestras, 5 variables)
    np.random.seed(42)
    n_samples = num_points
    n_features = num_features
    data = np.random.rand(n_samples, n_features) * 10

    # 🔹 Aplicar Factor Analysis en C++
    n_factors = num_factors
    reduced_data = fa_module.factor_analysis(data, n_factors)

    # 🔹 Gráfico de dispersión de los factores
    plt.figure(figsize=(8, 6))
    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='blue', alpha=0.7)
    plt.title('Factor Analysis - Gráfico de Dispersión')
    plt.xlabel('Factor 1')
    plt.ylabel('Factor 2')
    plt.grid(True)
    #plt.show()
    plt.savefig(output_file_1)

    # 🔹 Gráfico de varianza explicada simulada
    explained_variance = np.sort(np.random.rand(n_factors))[::-1]
    explained_variance /= explained_variance.sum()

    plt.figure(figsize=(8, 6))
    plt.bar(range(1, n_factors + 1), explained_variance, color='green', alpha=0.7)
    plt.title('Varianza Explicada por Factor')
    plt.xlabel('Factores')
    plt.ylabel('Proporción de Varianza Explicada')
    plt.xticks(range(1, n_factors + 1))
    #plt.show()

    plt.savefig(output_file_2)
    plt.close()
    
    j1 = {
        "Grafica de dispersion": output_file_1,
        "Grafica de varianza": output_file_2
    }
    jj = json.dumps(str(j1))

    return jj

@app.get("/factor-analysis-graph")
def getGraph(output_file: str):
    return FileResponse(output_file, media_type="image/png", filename=output_file)
