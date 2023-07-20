import socket
import uuid

def get_hwid():
    return str(uuid.uuid4())

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to server at localhost:12345")

    # Client HWID'sini oluşturalım ve server'a gönderelim
    hwid = get_hwid()
    print(f"Client HWID: {hwid}")
    client_socket.sendall(hwid.encode())

    # Server'dan gelen verileri okuyalım ve ekrana yazdıralım
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")

    # İşlem tamamlandıktan sonra soketi kapat
    client_socket.close()

if __name__ == "__main__":
    main()
