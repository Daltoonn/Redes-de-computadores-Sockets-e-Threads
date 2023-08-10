__author__ = "Guilherme Araújo", "Dalton Oyama"

import socket
import sys
import time

HOST = '127.0.0.1'  
PORT = 20001        
BUFFER_SIZE = 40000  


def main(argv):
    try:
        while True:
            # Cria um soquete de datagrama
            UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            # Vincular ao endereço e ip
            UDPServerSocket.bind((HOST, PORT))
            print("Servidor esta UDP funcionando")

            while True:
                bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)
                arquivo = bytesAddressPair[0].decode()
                endereco = bytesAddressPair[1]

                if arquivo == 'fim':
                    print("Conexão encerrada pelo cliente!")
                    break

                # checa se o arquivo solicitado está disponível
                if arquivo in ["small.txt", "medium.txt", "large.txt", "surprise.jpg"]:
                    start = time.time()
                    
                    with open(arquivo, 'rb') as file:
                        while True:
                            data = file.read(BUFFER_SIZE)
                            UDPServerSocket.sendto(data, endereco)
                            time.sleep(0.00001)
                            if not data:
                                break

                    end = time.time()
                    final_time = end - start

                    print(f"Arquivo '{arquivo}' enviado com sucesso!")
                    print(f"Tempo total de envio {round(final_time*1000, 3)} segundos!")

                else:
                    print(f"Arquivo '{arquivo}' não encontrado.")

    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)

if __name__ == "__main__":
    main(sys.argv[1:])
