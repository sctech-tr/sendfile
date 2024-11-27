# 📦 SendFile: File Sharing Across Local Network
SendFile is a Python-based tool that allows you to **send** and **receive files** across your local network. It serves files from the `~/.sendfile/uploads` directory on the server and saves downloaded files in the `~/.sendfile/downloads` directory on the client.
## 🎉 Features
- **Host a File Server**: Easily start a server to share files within your local network.
- **Download Files**: Retrieve files from another device using its local IP address.
- **Lightweight**: Built using Python's standard library (no external dependencies! (except for requests)).
- **Modular**: The app is split into multiple files for maintainability and clarity.

## 🛠 Installation
1. Ensure Python 3.9 or newer is installed.
2. Install via pip:
```bash
pip install sendfile
```
## 🚀 Usage
### Start the Server
Host the server to share files from `~/.sendfile/uploads`:
```bash
python -m sendfile serve --host 0.0.0.0 --port 8000
```
#### Options:
- `--host`: Host to bind the server (default: `0.0.0.0`).
- `--port`: Port to bind the server (default: `8000`).
### Download a File
Download a file from a server:
```bash
python -m sendfile download <SERVER_IP> <FILE_NAME> --port 8000
```
#### Example:
```bash
python -m sendfile download 192.168.1.114 my_file.txt --port 8000
```
#### Options:
- `<SERVER_IP>`: Local IP address of the server.
- `<FILE_NAME>`: Name of the file to download.
- `--port`: Port of the server (default: `8000`).
## 📜 Using as an HTTP server
### DEPRECATED: This feature is deprecated. The sibling project [pyserver](https://github.com/sctech-tr/pyserver) is recommended for serving files over HTTP. It is built on top of SendFile and provides additional features.
You can also use SendFile as an HTTP server to serve files from a specific directory. To do this, run the following command:
```bash
python -m sendfile serve --host 0.0.0.0 --port 80
```
## 📂 File Structure
```plaintext
sendfile/
├── __main__.py       # Entry point for the application
├── server.py         # Server-side implementation
├── client.py         # Client-side implementation
├── utils.py          # Utility functions (e.g., get local IP)
```
## 🌟 Example Workflow
### Server:
Run the server on one machine:
```bash
python -m sendfile serve
```
Place the file to share in the `~/.sendfile/uploads` directory.

### Client:
Download the file from another machine:
```bash
python -m sendfile download 192.168.1.114 my_file.txt
```
## 🔧 Requirements

- Python 3.9 or newer.
- Both devices must be connected to the same local network.

## 🛡 Security Note
This tool is intended for local network use. Do not expose the server to the public internet without proper security measures.