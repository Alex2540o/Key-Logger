import platform # Get system info (for sys_info)
import socket # Get network info (for sys_info)
import getpass # Get username (for sys_info)

sys_info = "sys_info.txt"

#Function to log system information
def system_information():
    with open(sys_info, "w") as logSys: #recalling the file we made earlier so that it can start writing to it
        logSys.write(f"System: {platform.system()} {platform.release()}\n")
        logSys.write(f"Network Name: {platform.node()}\n")
        logSys.write(f"Machine: {platform.machine()}\n")
        logSys.write(f"Processor: {platform.processor()}\n")
        logSys.write(f"Hostname: {socket.gethostname()}\n")
        logSys.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
        logSys.write(f"Username: {getpass.getuser()}\n") # everything from line 28 to 34 is for system information, look at the name to see what it will capture...