# Imports
import setproctitle
import os
import signal 
import sys 

def start_process(ps_name):
    setproctitle.setproctitle(ps_name)
    i = 1000000
    j = 0
    while j<=i:
        print(j)
        j+=1

def stop_process(ps_name): 
    try: 
        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep " + ps_name + " | grep -v grep"):  
            fields = line.split() 

            pid = fields[0]  
              
            # terminating process  
            os.kill(int(pid), signal.SIGKILL)  
        return "Process Successfully terminated"
          
    except Exception as e: 
        return e
        # print("Error Encountered while running script") 

if __name__ == "__main__":
    start_process("111")
    stop_process("111")