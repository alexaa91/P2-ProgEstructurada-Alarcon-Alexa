# src/operaciones_matriz.py

import torch

print("=== OPERACIONES MATRICIALES CON PYTORCH ===")

# Inicialización manual de tensores numéricos

tensor_a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

tensor_b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Sumar estructuras en memoria

resultado_suma = tensor_a + tensor_b

print("\nResultado de la suma A + B:")

print(resultado_suma)