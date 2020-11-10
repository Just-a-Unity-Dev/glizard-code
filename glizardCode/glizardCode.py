from rich import print

# This is the interpeter for any .gc files

# Read's the glizard file, which opens code.gc
f = open("read.glizard", "r")
fName = f.read()

# Memory array, used to store variables
mem = []

def main():

    # Defined Glizard Code commands

    def writeToMem(write):
        mem.append(write)

    def disposeFromMem(dispose: int):
        try:
            mem.remove(dispose)
        except:
            print(f'{bcolors.FAIL}Error GC0001 | Unable to remove {dispose} from memory because {dispose} does not exist!')
            x = input()
            exit()

    def checkInput(x : str):
        y = input()
        if y==x:
            writeToMem()

    def memoryCheck(x : str):
        if x==mem:
            writeToMem('True')

    def execFile(fileName=None):
        exec(compile(open(fileName, "rb").read(), fileName, 'exec'))

    def write(x):
        print(f'{x}')

    # The Interpreter start's here

    with open(fName) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    # This is the main code, this actually runs everything

    for x in content:
        read = x

        if not x.startswith('$ '):
            if x.startswith('writeToMem'):
                y = x[x.find("(") + 1:x.find(")")]
                if "'" in y:
                    z = x[x.find("('") + 2:x.find("')")]
                    writeToMem(z)

            elif x.startswith('disposeFromMem'):
                z = x[x.find("(") + 1:x.find(")")]
                disposeFromMem(z)

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
                        z = x[x.find("([") + 2:x.find("])")]
                        print(mem[z])
                except:
                    print(f'[bold red]Error GC0002 | Unable to write text[/bold red]')
                    x = input()
                    exit()
            else:
                print(f'{bcolors.FAIL}Error GC0003 | Unexpected Error Occurred')
                x = input()
                exit()

    # length = write(len(content))
    # disposeFromMem(1)

if __name__ == '__main__':
    main()
