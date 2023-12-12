# image_processing.py

import os
import cv2
import numpy as np

# Lista de kernels según los requerimientos
kernels = [
    np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),  # Kernel “El primero de los Class 1”
    np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),  # Kernel “El primero de los Class 2”
    np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]]),  # Kernel “El primero de los Class 3”
    np.ones((3, 3), np.float32) / 9.0,  # Kernel “Square 3x3”
    np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]),  # Kernel “El primero de los Edge 3x3”
    np.ones((5, 5), np.float32) / 25.0,  # Kernel “Square 5x5”
    np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]),  # Kernel “El primero de los Edge 5x5”
    cv2.getDerivKernels(1, 0, 3, normalize=True),  # Kernel de sobel vertical
    cv2.getDerivKernels(0, 1, 3, normalize=True),  # Kernel de sobel horizontal
    np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),  # Kernel de Laplace
    cv2.getDerivKernels(1, 0, 1, normalize=True),  # Kernel de prewitt vertical
    cv2.getDerivKernels(0, 1, 1, normalize=True)  # Kernel de prewitt horizontal
]

def apply_filter(image, kernel):
    # Función para aplicar un filtro a una imagen
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

def image_statistics(image):
    # Función para calcular estadísticas de una imagen
    dimensions = image.shape[:2]
    min_value = np.min(image)
    max_value = np.max(image)
    mean_value = np.mean(image)
    std_deviation = np.std(image)
    return dimensions, min_value, max_value, mean_value, std_deviation

def apply_filters_and_statistics(img_paths, selected_kernel):
    processed_images = []

    for img_path in img_paths:
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if image is not None:
            filtered_image = apply_filter(image, kernels[selected_kernel])

            dimensions, min_value, max_value, mean_value, std_deviation = image_statistics(filtered_image)
            result = {
                'dimensions': dimensions,
                'min_value': min_value,
                'max_value': max_value,
                'mean_value': mean_value,
                'std_deviation': std_deviation
            }
            processed_images.append(result)

            # Guardar la imagen filtrada (opcional)
            cv2.imwrite(f'filtered_image_{os.path.basename(img_path)}', filtered_image)

        else:
            print(f"Error: No se pudo leer la imagen en {img_path}")

    return processed_images