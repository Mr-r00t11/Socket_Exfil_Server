# powershell_client.ps1

$server = "192.168.100.10"
$port = 4444
$file = "C:\Users\roman.gomez\Desktop\testing.txt"

try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $tcpClient.Connect($server, $port)
    $stream = $tcpClient.GetStream()

    $bytes = [System.IO.File]::ReadAllBytes($file)
    $stream.Write($bytes, 0, $bytes.Length)

    Write-Host "[*] Archivo enviado correctamente."
    $stream.Close()
    $tcpClient.Close()
} catch {
    Write-Host "[!] Error al enviar el archivo: $_"
}