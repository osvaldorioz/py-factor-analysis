El **Análisis Factorial (FA)** es una técnica de reducción de dimensionalidad utilizada para descubrir **factores latentes** que explican la correlación entre variables observadas.  

### **📌 Pasos del Algoritmo FA**  
1. **Entrada:** Matriz de datos \( X \) con \( n \) muestras y \( p \) variables.  
2. **Centrado de datos:** Se resta la media de cada variable para que tengan **media cero**.  
3. **Cálculo de la matriz de covarianza:** Se obtiene la matriz de covarianza de los datos.  
4. **Descomposición en valores propios:** Se calculan los **valores propios** y **vectores propios** de la matriz de covarianza.  
5. **Selección de factores principales:** Se eligen los \( k \) factores con los **valores propios más grandes**.  
6. **Transformación de los datos:** Los datos originales se proyectan sobre los factores seleccionados.  
7. **Salida:** Matriz de datos transformados en un espacio de menor dimensión.  

---

## 🔷 **📌 Implementación en el Programa C++**  

🔹 **C++ con Pybind11:**  
✅ **Convierte datos NumPy a Eigen** para cálculos rápidos.  
✅ **Centra los datos** restando la media de cada columna.  
✅ **Calcula la matriz de covarianza** y realiza una **descomposición en valores propios**.  
✅ **Extrae los factores principales** y los devuelve a Python como un array NumPy.  

🔹 **Python:**  
✅ **Genera datos de prueba** 
✅ **Llama a la función C++** `factor_analysis()` para reducir las dimensiones a n factores.  
✅ **Grafica:**  
   - Un **gráfico de dispersión** de los factores.  
   - Un **gráfico de varianza explicada** para ver la importancia de cada factor.  

---

🚀 **Resultado:** Este programa implementa FA de manera eficiente en C++, acelerando el cálculo y permitiendo una visualización clara en Python. 😊
