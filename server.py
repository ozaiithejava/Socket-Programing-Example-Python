import socket

def get_hwid(conn):
    return conn.recv(1024).decode()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Server started. Listening on port 12345...")

    conn, addr = server_socket.accept()
    print(f"Client connected from: {addr[0]}")

    # Client'in HWID'sini alalım
    client_hwid = get_hwid(conn)
    print(f"Client HWID: {client_hwid}")

    # Client'tan gelen verileri okuyalım ve ekrana yazdıralım
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

    # Client'a hoşgeldin mesajı gönderelim
    conn.sendall("Merhaba, bağlantı başarılı!".encode())

    # İşlem tamamlandıktan sonra soketleri kapat
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
