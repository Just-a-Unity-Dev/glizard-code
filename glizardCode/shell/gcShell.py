import time
import os
from rich import print


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

mem = []


def writeToMem(write):
    mem.append(write)


def disposeFromMem(dispose: int):
    try:
        mem.remove(dispose)
    except:
        print(f'[bold red]Error GC0001 | Unable to remove {dispose} from memory because {dispose} does not exist![/bold red]')
        x = input()
        exit()

def execute(x : str):
    if x.startswith('writeToMem'):
        y = x[x.find("(") + 1:x.find(")")]
        if "'" in y:
            z = x[x.find("('") + 2:x.find("')")]
            writeToMem(z)



    elif x.startswith('write'):
        try:
            y = x[x.find("(") + 1:x.find(")")]
            if "'" in y:
                z = x[x.find("('") + 2:x.find("')")]
                print(z)
            elif "'" not in y:
                z = eval(y)
                print(z)
            else:
                z = x[x.find("([") + 2: x.find("])")]
                print(mem[z])
        except:
            print(f'[bold red]Error GC0002 | Unable to write text [/bold red]')
    elif x == 'listMem()':
        print(mem)
    elif x == 'cls':
        os.system('cls')
        print('')
    elif x == 'listFiles':
        a = os.listdir('.')
        print(a)
    elif x.startswith('mkdir'):
        try:
            y = x[x.find("(") + 1:x.find(")")]
            os.makedirs(y)
            print(f'{bcolors.OKBLUE} Task ran sucessfully {bcolors.ENDC}')
        except Exception:
            print(f'[bold red]Error GC0005 | Unable to make directory [/bold red]')


    elif x.startswith('disposeFromMem'):
        z = x[x.find("s(") + 1:x.find(")")]
        disposeFromMem(z)

    elif x == 'memList':
        print(mem)

    else:
        print(f'[bold red][#] command {x} is not listed [/bold red]')



def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
        print(os.getcwd())
    except Exception:
        print(f"[bold red]cd: no such file or directory: {path} [/bold red]")

while True:
    os.system('title GlizardCode Shell')
    inp = input('# ')
    if inp == "exit":
        break
    elif inp[:3] == "cd ":
        psh_cd(inp[3:])
    else:
        execute(inp)
