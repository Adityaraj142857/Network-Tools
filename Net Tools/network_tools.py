#!/usr/bin/python
import random
import os
import sys
import subprocess
import time, requests, threading, platform
try:
    from colorama import Fore
except:
    os.system("py -m pip install colorama")
    from colorama import Fore


class tools():
    def __init__(self , host):
        self.host = host

############################## For ping command #####################################
    def ping(host):

        # Ping parameters as function of OS
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        args = "ping " + " " + ping_str + " " + host
        need_sh = False if platform.system().lower() == "windows" else True

        response = subprocess.call(args, shell=need_sh) == 0

        if response == 0:
            print(host, 'is down!')
            return response
        else:
            print(host, 'is up!')
            return response


################################# For Tracerouote command ########################################


    def traceroute(host):

        import platform

        # traceroute parameters as function of OS
        traceroute_str = "trecert" if platform.system(
        ).lower() == "windows" else "traceroute"
        args = traceroute_str + " " + host + " " + "--back" + " " + "-A"
        need_sh = False if platform.system().lower() == "windows" else True

        # traceroute
        return subprocess.call(args, shell=need_sh) == 0

# **********************************************************************************************


################################# For ENUMERATING IP_ADDRESS ########################################

    def ip_add():
        import socket

        host = input(Menu.white + "\nEnter the website address: ")
        print(" ")
        print(f'The {host} IP address is: {socket.gethostbyname(host)}')
        print(" ")

# **********************************************************************************************


class Menu():
    
    white = Fore.WHITE
    yellow = Fore.YELLOW
    green = Fore.GREEN
    red = Fore.LIGHTRED_EX
    cyan = Fore.CYAN
    lb = Fore.LIGHTBLUE_EX

    colors = [white, yellow, cyan, lb , Fore.LIGHTRED_EX]
    color = random.choice(colors)

    openBracket = white + " ["
    closeBracket = white + "] "

    def __init__(self):
        self.title()

    def Help(self):
        print(Menu.white + "\t\t-------------------------------------------\n\t\t\t\tHELP SECTION\n\t\t-------------------------------------------")
        content = ''' 
                
                Hello Users I hope You have a Good understanding of The commands PING and TRACEROUTE 
                
                If not Click on the link to get Rediected to the Official Document and learn about these commands

                PING -- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping
                
                TRACEROUTE --

                            WINDOWS -- https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tracert
                            
                            LINUX / MAC OS -- https://linux.die.net/man/8/traceroute

                

                IN THIS TOOL THE FOLLOWING ARGUMENTS ARE USED :
                
                PING :
                        -n / -c  	Specifies the number of echo Request messages be sent. The default is 4.

                TRACEROUTE :
                        -A   --as-path-lookups       
                            Perform AS path lookups in routing registries and
                            print results directly after the corresponding
                            addresses
                        
                        --back   
                            Guess the number of hops in the backward path and print if it differs
                            
        
        '''
        print(Menu.white + content)
    
    def title(self):
        os.system('cls && title IP Scanner' if os.name == 'nt' else 'clear')

        banner = """ 

                ███╗   ██╗███████╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                ████╗  ██║██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                ██╔██╗ ██║█████╗     ██║          ██║   ██║   ██║██║   ██║██║     ███████╗
                ██║╚██╗██║██╔══╝     ██║          ██║   ██║   ██║██║   ██║██║     ╚════██║
                ██║ ╚████║███████╗   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                ╚═╝  ╚═══╝╚══════╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                                        
                                                                            # By AR and Ayush
                                                                            
                # Objective -- TO develope an application to stimulate PING and TRACEROUTE commands

                """
        return print(Menu.color + banner)

    def menu(self):
        print(Menu.openBracket + Menu.color + "1" + Menu.closeBracket + Menu.green + "Ping")
        print(Menu.openBracket + Menu.color + "2" + Menu.closeBracket + Menu.green + "Traceroute the Packet")
        print(Menu.openBracket + Menu.color + "3" + Menu.closeBracket + Menu.green + "Enumerate IP_ADDRESS")
        print(Menu.openBracket + Menu.color + "4" + Menu.closeBracket + Menu.green + "Help")
        print("")

    def choice(self):
        isExit = False

        while isExit != True:
            try:
                choice = int(input(Menu.openBracket + Menu.green + "+" +
                            Menu.closeBracket + Menu.color + "Enter an option to continue: "))
                if choice == 1:
                    host = input(Menu.white + "Enter the IPv4 / IPv6 / hostname to ping : ")
                    print(Menu.white + "--------------------------------------\nPing Result\n--------------------------------------")
                    print(tools.ping(host))
                    isExit = True
                elif choice == 2:
                    host = input(Menu.white + "Enter the IPv4 / IPv6 / hostname to ping : ")
                    print(Menu.white + "-----------------------------------\nTraceroute Result\n-----------------------------------")
                    print(Menu.green + str(tools.traceroute(host)))
                    isExit = True
                elif choice == 3:
                    tools.ip_add()
                    isExit = True
                elif choice == 4:
                    Menu.Help(self)
                    isExit = True
                else:
                    print(Menu.red + "\n***** Dude Please Clean Your lens and Enter the Right Choice *****\n")
                    isExit = True
            except IndexError as e:
                print(color + "There is an index error")
                isExit = True
        print(" ")


        

    def start(self):
        self.title()
        self.menu()
        self.choice()

Menu().start()