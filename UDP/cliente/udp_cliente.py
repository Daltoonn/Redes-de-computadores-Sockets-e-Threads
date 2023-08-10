__author__ = "Guilherme Araújo", "Dalton Oyama"

import socket, sys
import time

HOST = '127.0.0.1'  
PORT = 20001        
BUFFER_SIZE = 40000  
arquivos = ["small.txt", "medium.txt", "large.txt", "surprise.jpg"]

def main(argv): 
    try:
        print("-----------------------------BEM VINDO AO PROGRAMA!!!-----------------------------\n")
        # Cria o socket UDP
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as UDPClientSocket:
            while True:
                    
                # Envia opcao para o servidor
                print("Servidor executando!")
                print("Arquivos disponíveis para download:\n")
                print(arquivos)
                opcao = input("\nDigite o nome do arquivo que deseja baixar.\nCaso não queira, digite 'sair:'\n")
                UDPClientSocket.sendto(opcao.encode(), (HOST, PORT))

                if opcao == 'sair':
                    UDPClientSocket.send('fim'.encode())
                    print("Conexão encerrada!!")    

                elif opcao == 'medium.txt':
                        with open('medium.txt', 'wb') as f:
                            while True:
                                data = UDPClientSocket.recv(BUFFER_SIZE)
                                
                                f.write(data)
                            
                                if len(data) == 0:
                                    break
                        print(f"Download do arquivo {opcao} executado com sucesso!")                                             

                elif opcao == 'small.txt':
                        with open('small.txt', 'wb') as f:
                            while True:
                                data = UDPClientSocket.recv(BUFFER_SIZE)

                                f.write(data)

                                if len(data) == 0:
                                    break

                        print(f"Download do arquivo {opcao} executado com sucesso!")

                elif opcao == 'large.txt':
                        with open('large.txt', 'wb') as f:
                            while True:
                                data = UDPClientSocket.recv(BUFFER_SIZE)

                                f.write(data)

                                if len(data) == 0:
                                    break          

                        print(f"Download do arquivo {opcao} executado com sucesso!")

                elif opcao == 'surprise.jpg':
                        with open('surprise.jpg', 'wb') as f:
                            while True:
                                data = UDPClientSocket.recv(BUFFER_SIZE)

                                f.write(data)

                                if len(data) == 0:
                                    break          

                        print(f"Download do arquivo {opcao} executado com sucesso!")    
                        
                else: 
                        print(f"O arquivo {opcao} não foi encontrado!")  
                                                               

                aux = input('\nDeseja baixar mais arquivos? Responda "sim"ou"nao":\n')
                if aux.lower() != 'sim':
                    UDPClientSocket.send('fim'.encode())
                    print("Conexão encerrada!")                

    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return


if __name__ == "__main__":   
    main(sys.argv[1:])