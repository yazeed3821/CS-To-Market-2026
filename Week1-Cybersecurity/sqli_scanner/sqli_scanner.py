import requests

def check_sqli(url):
    # an SQL Injection payload to test for vulnerabilities
    payload = "'"
    vulnerable_url = f"{url}{payload}"
    
    try:
        # sending the request to the URL with the payload added
        response = requests.get(vulnerable_url)
        
        # keywords that indicate a database error (evidence of a vulnerability)
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
            
    except Exception as e:
        print(f"[-] An error occurred while connecting: {e}")

if __name__ == "__main__":
   
    test_url = "" #put your target URL here
    
    print(f"Checking the URL: {test_url}")
    print("-" * 50)
    check_sqli(test_url)