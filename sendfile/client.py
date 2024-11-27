import requests
import os

def download_file(ip, port, file_name):
    """Download a file from the server."""
    url = f"http://{ip}:{port}/{file_name}"
    dest_dir = os.path.expanduser("~/.sendfile/downloads")
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, file_name)

    print(f"Downloading {file_name} from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(dest_path, "wb") as file:
            file.write(response.content)
        print(f"File saved to {dest_path}")
    except requests.RequestException as e:
        print(f"Failed to download file: {e}")
