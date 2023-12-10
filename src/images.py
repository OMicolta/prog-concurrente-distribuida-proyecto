import os
import threading
from queue import Queue
from google_images_download import google_images_download

def download_images(query, num_images):
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords":query,"limit":num_images,"print_urls":True}
    paths = response.download(arguments)
    print(paths)

    return paths[0][query]

def download_images_concurrent(query, num_images):
    if not os.path.exists(query):
        os.makedirs(query)

    def worker():
        while True:
            start, end = q.get()
            for i in range(start, end):
                item_name = '{}-{}'.format(query, i)
                print('Item no.: {} --> Item name = {}'.format(i + 1, item_name))
                print('Evaluating...')
                download_images(query, 1)
                print('Completed Image ====> {}.jpg'.format(i + 1))
            q.task_done()

    q = Queue()
    num_threads = 10
    num_images_per_thread = num_images // num_threads
    for i in range(num_threads):
        start = i * num_images_per_thread
        end = (i + 1) * num_images_per_thread
        if i == num_threads - 1:
            end = num_images
        q.put((start, end))

    for i in range(num_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    q.join()
