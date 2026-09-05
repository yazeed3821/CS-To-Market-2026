#  Automated SQL Injection (SQLi) Detection Engine

A defensive automation script that audits dynamic URL endpoints for SQL syntax error leaks and connection-level security controls.

##  Overview
Improper database input sanitization frequently surfaces through verbose database engine error signatures. This tool appends break-out payloads (`'`) to URL parameters and inspects server responses for diagnostic leakage across multiple DBMS engines (MySQL, SQLite, Oracle).

##  Key Implementation Details
* **Pattern Matching:** Scans response payloads for critical engine signatures (`syntax error`, `mysql fetch`, `sqlite3`, `ora-`).
* **Header Spoofing:** Employs explicit desktop `User-Agent` headers to bypass automated scraping restrictions.
* **Fault-Tolerant Networking:** Implements strict connection timeouts and graceful exception handling for unreachable hosts.

##  Usage

```bash
# Install dependencies
pip install requests

# Execute scan
python sqli_scanner.py

```
## Sample Output
Scanning URL: http://demo.testfire.net/search.aspx?txtSearch=test
--------------------------------------------------
[+] The URL appears to be safe from basic SQLi vulnerabilities.