# -*- coding: utf-8 -*-
__author__ = "Guilherme Araujo", "Dalton Oyama"

import socket, sys
import time


HOST = '127.0.0.1'
PORT = 20000
BUFFER_SIZE = 4000000


def main(argv): 
    try: 
        print("-----------------------------BEM VINDO AO PROGRAMA!!!-----------------------------\n")
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print("Servidor executando!")
                start = time.time()
 
                arquivos = s.recv(BUFFER_SIZE).decode()
                print("Arquivos disponíveis para download:\n")
                print(arquivos)

                opcao = input("Digite o NOME do arquivo que deseja baixar!!!\n")
                    
                s.send(opcao.encode())


                if opcao == 'small.txt':
                        with open('small.txt', 'wb') as f:
                            while True:
                                data = s.recv(BUFFER_SIZE)
                                if not data:
                                    break
                                else:
                                    f.write(data)
                                    break
                        print(f"Download do arquivo {opcao} executado com sucesso!")    
                     
                                             

                elif opcao == 'medium.txt':
                        with open('medium.txt', 'wb') as f:
                            while True:
                                data = s.recv(BUFFER_SIZE)
                                if not data:
                                    break
                                else: 
                                    f.write(data)                                                             
                                    break
                        print(f"Download do arquivo {opcao} executado com sucesso!")

                elif opcao == 'large.txt':
                        with open('large.txt', 'wb') as f:
                            while True:
                                data = s.recv(BUFFER_SIZE)
                                if not data:
                                    break
                                else: 
                                    f.write(data)                                   
                                    break
                        print(f"Download do arquivo {opcao} executado com sucesso!")
                        
                elif opcao == 'surprise.jpg':
                        with open('surprise.jpg', 'wb') as f:
                            while True:
                                data = s.recv(BUFFER_SIZE)
                                if not data:
                                    break
                                else: 
                                    f.write(data)                                    
                                    break
                        print(f"Download do arquivo {opcao} executado com sucesso!")

                else: 
                        print(f"O arquivo {opcao} não foi encontrado!")        

            
                
            aux = input('\nDeseja baixar mais arquivos? Responda "sim"ou"nao":\n')
            if aux.lower() != 'sim':
                s.send('fim'.encode())
                print("Conexão encerrada!")

    except Exception as error:
        print("Exceção - Programa será encerrado!")
        print(error)
        return

if __name__ == "__main__":   
    main(sys.argv[1:])