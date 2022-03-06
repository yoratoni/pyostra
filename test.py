from pyostra import LogTypes, pyprint, set_short

set_short(True)

def main():
    pyprint(LogTypes.CRITICAL, 'THIS IS A TEST')
    pyprint(LogTypes.ERROR, 'THIS IS A TEST')
    pyprint(LogTypes.WARN, 'THIS IS A TEST')
    pyprint(LogTypes.SUCCESS, 'THIS IS A TEST')
    pyprint(LogTypes.SILENT, 'THIS IS A TEST')
    pyprint(LogTypes.READY, 'THIS IS A TEST')
    pyprint(LogTypes.DATA, 'THIS IS A TEST')
    pyprint(LogTypes.INFO, 'THIS IS A TEST')
    
main()