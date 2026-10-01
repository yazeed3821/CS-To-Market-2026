import random
from datetime import datetime, timedelta

print("Generating server logs...")

normal_ips = ["192.168.1.15", "10.0.0.5", "172.16.0.8", "198.51.100.23", "203.0.113.50"]
attacker_ip = "192.168.1.99"
endpoints = ["/home", "/dashboard", "/api/data", "/images/logo.png", "/login"]

logs = []
base_time = datetime.now()

# Generate normal traffic
for i in range(400):
    ip = random.choice(normal_ips)
    endpoint = random.choice(endpoints)
    # Assume normal logins mostly succeed (200) or occasionally fail (401)
    status = random.choice([200, 200, 200, 401, 404])
    method = "GET" if endpoint != "/login" else random.choice(["GET", "POST"])
    
    timestamp = (base_time + timedelta(minutes=i)).strftime('%d/%b/%Y:%H:%M:%S')
    log_line = f'{ip} - - [{timestamp}] "{method} {endpoint} HTTP/1.1" {status}'
    logs.append(log_line)

# Inject brute-force attack from a single IP
for i in range(150):
    timestamp = (base_time + timedelta(minutes=200, seconds=i*3)).strftime('%d/%b/%Y:%H:%M:%S')
    log_line = f'{attacker_ip} - - [{timestamp}] "POST /login HTTP/1.1" 401'
    logs.append(log_line)

# Save to text file
with open("server_logs.txt", "w") as file:
    for log in logs:
        file.write(log + "\n")

print("Done. Saved to server_logs.txt")