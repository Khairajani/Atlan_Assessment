# Bash
import setproctitle
import os

def start_process(ps_name):
    setproctitle.setproctitle(ps_name)
    # print('Child Process ID ',  os.getpid())
    i = 100000
    j = 0
    while j<=i:
        print(j)
        j+=1

if __name__ == "__main__":
    start_process() 

