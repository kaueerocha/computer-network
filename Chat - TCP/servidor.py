import socket
                                                                # pergunta IP e PORT
HOST = socket.gethostbyname(socket.gethostname())               # pegar IP 
PORT = int(input('PORTA: '))


dest = (HOST, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# função do servidor
tcp.bind(dest)                                                  # vincular o endereço e porta

while True:
    tcp.listen(1)                                               # escutar as conexões ; dentro do While para poder fechar e abrir novamente a conexão
    cliente, con = tcp.accept()
    print('Conectado por', cliente)

    while True:
        msg = cliente.recv(1024).decode('utf-8')

        if not msg:
            break
        print(cliente, msg)

    print('Finalizando conexão do cliente', cliente)
    cliente.close()
    