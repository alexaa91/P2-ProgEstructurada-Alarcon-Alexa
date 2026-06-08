# src/inicializacion_tensores.py

import torch

print("=== VERIFICACIÓN DE ENTORNO PYTORCH ===")

print(f"Versión de PyTorch: {torch.__version__}")

# Creación de una matriz de 3x3 inicializada en ceros

matriz_ceros = torch.zeros(3, 3)

print("\nTensor de Ceros (3x3):")

print(matriz_ceros)