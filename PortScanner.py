import socket 
import sys
import requests


response = requests.get("https://ifconfig.me")                       #Send GET request for public ip
target_ip = sys.argv[1]                                              #First Command line argument passed after calling python file
local_ip = socket.gethostbyname(socket.gethostname())                #Fetch local machine ip


print("[+]Port scanner started...")
print(f"[+]Local Machine IP: {local_ip}")
print(f"[+]Public IP:{response.content}")
response.close()
 
for port in range(65536):                                            #For each port creates a socket,then attempts connection to the target ip (sys.argv[0](first argument) in Command Prompt)
   try:
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client_socket.settimeout(0.2)                                   #Socket timeout to prevent socket hanging 
     client_socket.connect((target_ip, port))

     print(f"Port {port} is open and awaiting connection")
     client_socket.close()

   except: 
    pass                                                             #if port is not open move on to the next



 
     
  




 






