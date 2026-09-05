import socket
import time

def scan_port(target_ip, port):
    try: 
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #made a socket object for the connection
        sock.settimeout(1)
        
        result = sock.connect_ex((target_ip, port)) # attempt to connect to the target IP and port
        
        if result == 0:
            print(f"[+] Port {port} is OPEN on {target_ip}")
        
        sock.close()
    except Exception as e:
        pass

if __name__ == "__main__":
    # here you can change the target IP address to scan different hosts
    target = "127.0.0.1" 
    
    print(f"Starting scan on target: {target}")
    start_time = time.time()
    
    #[21 FTP, 22 SSH, 53 DNS, 80 HTTP, 443 HTTPS, 3306 MySQL, 8080 HTTP-alt]
    ports_to_scan = [21, 22, 53, 80, 443, 3306, 8080]
    
    for port in ports_to_scan:
        scan_port(target, port)
        
    end_time = time.time()
    print(f"Scan completed in {round(end_time - start_time, 2)} seconds") 