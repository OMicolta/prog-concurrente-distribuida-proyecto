# src/image_downloader.py

import os
import concurrent.futures
import threading
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse

def download_images_concurrently(image_urls, total_images, output_directory):
    # Divide las URLs en 10 grupos
    image_url_groups = [image_urls[i:i + total_images // 10] for i in range(0, total_images, total_images // 10)]

    # Descarga imágenes concurrentemente en 10 hilos
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i, group in enumerate(image_url_groups):
            executor.submit(download_images_thread, group, output_directory, i)

def download_images_thread(image_urls, output_directory, thread_id):
    thread_output_directory = os.path.join(output_directory, f'thread_{thread_id}')
    os.makedirs(thread_output_directory, exist_ok=True)

    for url in image_urls:
        try:
            download_single_image(url, thread_output_directory)
        except Exception as e:
            print(f"Error downloading image {url}: {e}")

def download_single_image(url, output_directory):
    try:
        # Send a GET request to download the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Open the image using PIL
        image = Image.open(BytesIO(response.content))

        # Save the image to the output directory
        image_path = os.path.join(output_directory, os.path.basename(urlparse(url).path))
        image.save(image_path)

        print(f"Downloaded: {image_path}")

    except Exception as e:
        print(f"Error downloading image: {e}")
