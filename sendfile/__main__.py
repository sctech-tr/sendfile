import argparse
from .server import start_server
from .client import download_file
from .utils import get_local_ip # i may need it later

def main():
    parser = argparse.ArgumentParser(description="Send and receive files across the local network.")
    subparsers = parser.add_subparsers(dest="command")

    # Server mode
    server_parser = subparsers.add_parser("serve", help="Start the sendfile server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host to bind the server (default: 0.0.0.0)")
    server_parser.add_argument("--port", type=int, default=8000, help="Port to bind the server (default: 8000)")

    # Client mode
    client_parser = subparsers.add_parser("download", help="Download a file from a sendfile server")
    client_parser.add_argument("ip", help="IP address of the server")
    client_parser.add_argument("file_name", help="Name of the file to download")
    client_parser.add_argument("--port", type=int, default=8000, help="Port of the server (default: 8000)")

    args = parser.parse_args()

    if args.command == "serve":
        print(f"Starting server at {args.host}:{args.port}")
        start_server(host=args.host, port=args.port)
    elif args.command == "download":
        print(f"Downloading file from {args.ip}:{args.port}")
        download_file(ip=args.ip, port=args.port, file_name=args.file_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
