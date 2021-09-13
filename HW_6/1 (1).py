class SkipThisFile(Exception):
    pass


def read_lines(*files):
    
    
    for file in files:
        yield "dummy line"

def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile)


