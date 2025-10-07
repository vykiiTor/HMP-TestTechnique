from backend import models, database

'''
Creation of the database with good initial values added and two tables vulnerabilities and incidents
'''
models.database.Base.metadata.create_all(bind=database.engine)
vulnerabilities = [
    {"name": "CVE-2024-0001: SQL Injection", "severity": "Critical", "system": "Database", "status": "Open"},
    {"name": "CVE-2024-0002: XSS in Admin Panel", "severity": "High", "system": "Web App", "status": "Open"},
    {"name": "CVE-2024-0003: SSL/TLS Config Weakness", "severity": "Medium", "system": "Server", "status": "Open"},
    {"name": "CVE-2024-0004: Directory Traversal", "severity": "High", "system": "File Server", "status": "Open"},
    {"name": "CVE-2024-0005: Information Disclosure", "severity": "Low", "system": "API", "status": "Open"},
]
db = database.SessionLocal()
for v in vulnerabilities:
    vulnerabilitiesTable = models.Vulnerability(**v)
    db.add(vulnerabilitiesTable)
db.commit()
db.close()