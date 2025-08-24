# Socket Exfiltration

Este laboratorio demuestra cómo se pueden **transferir archivos de manera controlada vía TCP** usando un servidor Python y un cliente PowerShell.

> ⚠️ Solo usar en entornos propios o laboratorios. No atacar sistemas ajenos.

---
## Componentes

### 1. Servidor TCP (Python)
- Escucha en un puerto TCP configurado (`PORT = 4444`).
- Recibe datos en chunks de 1024 bytes.
- Guarda los datos en `data_exfiltrada.txt`.
- Ejecutar:
```bash
python3 tcp_exfil_server.py
```

### 2. Cliente TCP (PowerShell)

- Envía un archivo al servidor TCP.
- Configura la IP del servidor y el archivo a enviar:
```bash
$server = "192.168.100.10"
$port = 4444
$file = "C:\Users\roman.gomez\Desktop\testing.txt"
```
- Ejecutar:
```bash
.\powershell_client.ps1
```
___
## Flujo

1. El servidor espera conexiones entrantes.
2. El cliente PowerShell se conecta y envía el archivo.
3. El servidor recibe los datos y los guarda en `data_exfiltrada.txt`.
4. Se imprime en consola confirmación de recepción.
---
## Requisitos

- Python 3.x
- PowerShell 5.1+ (Windows)
- Red interna o laboratorio controlado
