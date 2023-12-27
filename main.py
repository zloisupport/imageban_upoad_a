# This is a sample Python script.
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("SECRET_KEY")
URL = "https://api.imageban.ru/v1"
ALBUM = os.getenv("ALBUM")
SLEEP_TIME = 5
WORK_DIR = os.getenv("WORK_DIR")


def upload_image(filename: str):
    files = {
        'image': (f"{filename}", open(os.path.join(WORK_DIR, filename), 'rb'))
    }
    headers = {
        'Authorization': f'Bearer {SECRET_KEY}'
    }
    payload = {
        'album': ALBUM
    }

    response = requests.post(URL, headers=headers, files=files, data=payload)
    if response.status_code == 200:
        print(f'Success!')


def batch_upload():
    files_list = [f for f in os.listdir(WORK_DIR) if
                  os.path.isfile(os.path.join(WORK_DIR, f))]
    for index, file in enumerate(files_list):
        upload_image(file)
        if index % 10 == 0:
            time.sleep(SLEEP_TIME)


def main():
    file = "c:\\Users\\mercy\\Downloads\\images\\4pm7gv85pht51.jpg"
    upload_image(file)


if __name__ == '__main__':
    main()
