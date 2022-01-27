from pathlib import Path
import requests, zipfile, io


def download_data() -> Path:
    zip_file_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"

    local_data_dir = Path(__file__).parent / "data"
    local_data_dir.mkdir(exist_ok=True)

    zipfile.ZipFile(io.BytesIO(requests.get(zip_file_url).content)).extractall(local_data_dir)
    return local_data_dir
