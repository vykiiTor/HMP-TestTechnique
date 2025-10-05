from backend import models, database
models.database.Base.metadata.create_all(bind=database.engine)
vulns = [
    {"name": "CVE-2024-0001: SQL Injection", "severity": "Critical", "system": "Database", "status": "Open"},
    {"name": "CVE-2024-0002: XSS in Admin Panel", "severity": "High", "system": "Web App", "status": "Open"},
    {"name": "CVE-2024-0003: SSL/TLS Config Weakness", "severity": "Medium", "system": "Server", "status": "Open"},
    {"name": "CVE-2024-0004: Directory Traversal", "severity": "High", "system": "File Server", "status": "Open"},
    {"name": "CVE-2024-0005: Information Disclosure", "severity": "Low", "system": "API", "status": "Open"},
]
db = database.SessionLocal()
for v in vulns:
    vuln = models.Vulnerability(**v)
    db.add(vuln)
db.commit()
db.close()