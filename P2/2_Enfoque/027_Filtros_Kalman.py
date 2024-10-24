import numpy as np
from os import system

def kalman_filter(A, B, H, Q, R, x_est, P_est, u, z):
    """
    Filtro de Kalman para un sistema lineal.

    Parámetros:
    A - Matriz de transición de estado
    B - Matriz de control
    H - Matriz de observación
    Q - Covarianza del proceso
    R - Covarianza de la observación
    x_est - Estado estimado inicial
    P_est - Covarianza del error inicial
    u - Control aplicado
    z - Observación realizada

    Retorna:
    x_est_actualizado - Estado estimado actualizado
    P_est_actualizado - Covarianza de error actualizada
    """

    # PREDICCIÓN
    # Predicción del estado
    x_pred = A @ x_est + B @ u
    
    # Predicción de la covarianza del error
    P_pred = A @ P_est @ A.T + Q

    # ACTUALIZACIÓN
    # Ganancia de Kalman
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)

    # Actualización del estado estimado
    x_est_actualizado = x_pred + K @ (z - H @ x_pred)

    # Actualización de la covarianza del error
    P_est_actualizado = (np.eye(len(A)) - K @ H) @ P_pred

    return x_est_actualizado, P_est_actualizado

# Ejemplo de uso
A = np.array([[1, 1], [0, 1]])  # Matriz de transición de estados
B = np.array([[0.5], [1]])      # Matriz de control
H = np.array([[1, 0]])          # Matriz de observación
Q = np.array([[1, 0], [0, 1]])  # Covarianza del proceso
R = np.array([[1]])             # Covarianza de la observación
x_est = np.array([0, 1])        # Estado inicial
P_est = np.eye(2)               # Covarianza de error inicial
u = np.array([0])               # Control (aceleración)
z = np.array([1])               # Observación realizada

# Ejecutar el filtro de Kalman
x_est_actualizado, P_est_actualizado = kalman_filter(A, B, H, Q, R, x_est, P_est, u, z)

system('cls')
print("Estado estimado actualizado:    ", x_est_actualizado)
print("Covarianza de error actualizada:", P_est_actualizado)