import socket
import time

host = socket.gethostname()  # Pega o hostname
serverPort = 5000  # Porta tem que ser acima de 1024

serverAddressPort = (host, serverPort)

TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
TCPServerSocket.bind(serverAddressPort)

# Quantos clientes o socket vai esperar ao mesmo tempo?
TCPServerSocket.listen(1)
connSocket, address = TCPServerSocket.accept()  # Aceita nova conexão
print('Conectou com: ' + str(address))
while True:
    # Recebe os dados no Stream. Não aceita pacotes menores que 1024
    message = connSocket.recv(1024).decode()
    if not message:
        time.sleep(5)
        print('Nenhuma mensagem recebida... 5 segundos de standby...')
        continue
    print("from connected user: " + str(message))
    capitalmsg = message.upper()
    connSocket.send(capitalmsg.encode())  # Envia dados para cliente

connSocket.close()  # Fecha a conexão