import socket
host = socket.gethostname() # servidor e cliente rodam na mesma maquina
serverPort = 5000 # porta do servidor
server = (host, serverPort) # IP e porta do servidor
TCPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
TCPClientSocket.connect(server) # conecta ao servidor
message = input("Mensagem: ") # pega a mensagem
while message.lower().strip() != 'bye':
    TCPClientSocket.send(message.encode()) # envia a mensagem
    message = TCPClientSocket.recv(1024).decode() # recebe a resposta
    print('Received from server: ' + message)
    message = input("Mensagem: ") # pega a mensagem
TCPClientSocket.close() # fecha o soquete