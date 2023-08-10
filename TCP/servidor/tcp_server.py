# -*- coding: utf-8 -*-
__author__ = "Guilherme Araujo", "Dalton Oyama"

import socket, sys, time
from threading import Thread

HOST = '127.0.0.1'  
PORT = 20000        
BUFFER_SIZE = 4000000 


def on_new_client(clientsocket,addr):
    arquivos = ["small.txt", "medium.txt", "large.txt", "surprise.jpg"]  
    try:
        while True:
                clientsocket.send(str(arquivos).encode())  
                arq = clientsocket.recv(BUFFER_SIZE).decode() 

                if arq == 'fim':
                    print("Conexão encerrada pelo cliente!")
                    break

                # checa se o arquivo solicitado está na lista de disponibilidade
                elif arq in arquivos:
                    start = time.time()
                    with open(arq, 'rb') as dg:
                        data = dg.read()
                        clientsocket.send(data)
                        print(f"Arquivo {arq} enviado com sucesso!")

                    end = time.time()

                    final_time = end - start
                    print(f"Tempo total de envio {round(final_time*1000, 3)} milessegundos!\n")
                else:
                    print("Opa, arquivo não encontrado!")
                        
                

        clientsocket.close()  # encerra o socket do cliente            


    except Exception as error:
        print("Erro na conexão com o cliente!!")
        return


def main(argv):
    try:
        # AF_INET: indica o protocolo IPv4. SOCK_STREAM: tipo de socket para TCP,
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            while True:
                server_socket.listen()
                clientsocket, addr = server_socket.accept()
                print('Conectado ao cliente no endereço:', addr)
                t = Thread(target=on_new_client, args=(clientsocket,addr))
                t.start()   
    except Exception as error:
        print("Erro na execução do servidor!!")
        print(error)        
        return             



if __name__ == "__main__":   
    main(sys.argv[1:])