# AppSec Hands-on Lab: Authentication Bypass & Secure Coding

A vulnerable-by-design local web application demonstrating real-world exploitation of CWE-89 (SQL Injection) and its end-to-end engineering remediation.

## Overview
This lab contrasts an unsafe dynamic SQL implementation with an enterprise-grade defense using Parameterized Queries (Prepared Statements).

---

## The Vulnerability: Authentication Bypass

The login logic initially concatenated raw user input directly into the dynamic database query string:

```python
# Unsafe concatenation
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

### Exploit Payload
By injecting `admin' OR '1'='1` into the username field, the logical query evaluation changes:

```sql
SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = ''
```

The condition `'1'='1'` evaluates to true across the database engine, bypassing password validation and authenticating as the first returned record (`admin`).

---

## Remediation: Parameterized Queries

The vulnerability is remediated by enforcing prepared statements with placeholder binding:

```python
# Secure implementation
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

The database engine treats the supplied string purely as literal data, rendering malicious SQL control tokens inert.

---

## Usage

1. Install requirements:
```bash
pip install flask
```

2. Start the local server:
```bash
python app_sec_lab.py
```

3. Open `http://127.0.0.1:5000` in your browser.