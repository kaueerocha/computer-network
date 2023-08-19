import socket

HOST = input('IP: ')                                        # Endereco IP do Servidor
PORT = int(input('PORT: '))                                 # Porta que o Servidor esta (servidor e cliente devem estar na mesma porta)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Criando um socket de protocolo TCP

dest = (HOST, PORT)
tcp.connect(dest)

print('\nPara sair use x')

msg = input('Mensagem: ').encode('utf-8')
while msg.decode('utf-8') != 'x':
    tcp.send (msg)
    msg = input('Mensagem while: ').encode('utf-8')
tcp.close()
