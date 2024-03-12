import os
from colorama import init, Fore, Back 


def logo():
    print("""
     _____             _____ _    __ _ 
    |  __ \           / ____| |  /_ | |
    | |__) |_____   _| (___ | |__ | | |
    |  _  // _ \ \ / /\___ \| '_ \| | |
    | | \ \  __/\ V / ____) | | | | | |
    |_|  \_\___| \_/ |_____/|_| |_|_|_|
    """)


def sleep():
    os.system("sleep 1s")
# file = open("types/bash/bash01", "r")
# print(file.readline())
class Shells:
    def __init__(self, n, t):
        self.name = n 
        self.tipo = t
    def info(self):
        string = "Name: {}\nType: {}".format(self.name, self.tipo)
        print(string)
    
    def sintax(self, arquivo):
        print("Printing one line reverse shell for {}:\n".format(self.name))
        file = open(arquivo, 'r')
        init(autoreset=True)
        print("\t" + Back.GREEN + Fore.BLACK + file.readline())
        file.close()



def opts():
    options = { 1:'bash', 2:'go', 3:'java', 4:'netcat', 5:'node', 6:'perl', 7:'php', 8:'python', 9:'ruby', 10:'xterm'}
    for key, value in options.items():
        print(f"{key}: {value}")  
logo()
while True:
    print("\nPrinting options...")
    sleep()
    opts()
    option = int(input('Choose the the type of reverse shell: '))
    match option:
        case 1:
            bash = Shells("Bash", "Shell")
            bash.info()
            bash.sintax("types/bash/bash01")
        case 2:
            go = Shells("Go", "Programming language")
            go.info()
            go.sintax("types/go/go01")
        case 3:
            java = Shells("Java", "Programming language")
            java.info()
            java.sintax("types/java/java01")
        case 4:
            netcat = Shells("Netcat", "Linux program")
            netcat.info()
            netcat.sintax("types/netcat/netcat01")
        case 5:
            node = Shells("Node", "Programming language")
            node.info()
            node.sintax("types/node/node01")
        case 6:
            perl = Shells("Perl", "Programming language")
            perl.info()
            perl.sintax("types/perl/perl01")
        case 7:
            php = Shells("PHP", "Programming language")
            php.info()
            php.sintax("types/php/php01")
        case 8:
            python = Shells("Python", "Programming language")
            python.info()
            python.sintax("types/python/python01")
        case 9:
            ruby = Shells("Ruby", "Programming language")
            ruby.info()
            ruby.sintax("types/ruby/ruby01")
        case 10:
            xterm = Shells("Xterm", "Linux Program")
            xterm.info()
            xterm.sintax("types/xterm/xterm01")
        case _:
            print("Unknown option. Exiting...")
            break