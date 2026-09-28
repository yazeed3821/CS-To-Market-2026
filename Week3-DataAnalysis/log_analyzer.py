import pandas as pd
import matplotlib.pyplot as plt

print("Analyzing server logs...")

parsed_data = []

with open("server_logs.txt", "r") as file:
    for line in file:
        parts = line.split()
        parsed_data.append({
            "ip": parts[0],
            "endpoint": parts[5],
            "status": parts[-1]
        })

df = pd.DataFrame(parsed_data)

failed_logins = df[(df['endpoint'] == '/login') & (df['status'] == '401')]
attacker_ips = failed_logins['ip'].value_counts()

print("Potential Attackers (Failed Logins):")
print(attacker_ips.head())

print("Generating chart...")
plt.figure(figsize=(10, 6))
attacker_ips.plot(kind='bar', color='red')
plt.title('Failed Login Attempts per IP')
plt.xlabel('IP Address')
plt.ylabel('Number of Failed Attempts')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('attack_analysis.png')
print("Chart saved as attack_analysis.png")