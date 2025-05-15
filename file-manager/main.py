import os

def cwd():
    s=os.getcwd()
    print(s)

def ls():
    for item in os.listdir():
        print(item)

def cd(args):
    os.chdir(args)
    print(os.getcwd())

def mkdir(path):
    os.mkdir(path)

def touch(args):
    if len(args) not in (2, 3):
        return 
    filename = args[1]
    content = args[2] if len(args) == 3 else ""
    with open(filename, 'w') as f:
        f.write(content)

def rm(args):
    os.remove(args)

def parse_input(user_input):
    if user_input.startswith("touch"):
        parts = user_input.split('"')
        cmd = parts[0].strip()
        args = [cmd] + [p for p in parts[1:] if p.strip()]
    else:
        args = user_input.strip().split()

    if not args:
        return True

    command = args[0]

    if command == "cwd":
        cwd()
    elif command == "ls":
        ls()
    elif command == "cd":
        if len(args) >= 2:
            cd(args[1])
    elif command == "mkdir":
        if len(args) >= 2:
            mkdir(args[1])
    elif command == "touch":
        if len(args) in (2, 3):
            touch(args)
    elif command == "rm":
        if len(args) >= 2:
            rm(args[1])
    elif command == "exit":
        return False
    return True

# CLI Loop
if __name__ == "__main__":
    while True:
        user_input = input(">>> ")
        if not parse_input(user_input):
            break
