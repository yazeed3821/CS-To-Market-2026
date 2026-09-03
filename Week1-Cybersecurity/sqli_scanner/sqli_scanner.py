import requests

def check_sqli(url):
    payload = "'"
    vulnerable_url = f"{url}{payload}"
    
    try:
        # for requests.get, we can set a User-Agent header to mimic a real browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        
        # setting a timeout of 5 seconds to avoid indefinite waiting if the server is down
        response = requests.get(vulnerable_url, headers=headers, timeout=5)
        
        errors = ["syntax error", "mysql fetch", "sqlite3", "ora-", "sql syntax"]
        
        is_vulnerable = False
        for error in errors:
            if error in response.text.lower():
                print(f"[!] Warning: The URL is vulnerable to SQL Injection!")
                print(f"[!] Vulnerable URL: {vulnerable_url}")
                is_vulnerable = True
                break
                
        if not is_vulnerable:
            print(f"[+] The URL appears to be safe from basic SQLi vulnerabilities.")
            
    except requests.exceptions.Timeout:
        print("[-] Connection timeout. The target server is either offline or blocked by your network provider.")
    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred while connecting: {e}")

if __name__ == "__main__":
    test_url = "http://demo.testfire.net/search.aspx?txtSearch=test" #put your target URL here // I used a demo website for testing purposes
    
    print(f"Scanning URL: {test_url}")
    print("-" * 50)
    check_sqli(test_url)