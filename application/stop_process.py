
import os, signal 
   
def stop_process(name): 
    try: 
          
        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):  
            fields = line.split() 
              
            # extracting Process ID from the output 
            pid = fields[0]  
              
            # terminating process  
            os.kill(int(pid), signal.SIGKILL)  
        print("Process Successfully terminated") 
          
    except Exception as e: 
        print(e)
        print("Error Encountered while running script") 
   
if __name__ == "__main__":
    # Ask user for the name of process 
    name = input("Enter process Name: ") 
    stop_process(name) 
