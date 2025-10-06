const API_BASE_URL = "http://0.0.0.0:8000"; // backend FastAPI URL

export async function getVulnerabilities() {
  const res = await fetch(`${API_BASE_URL}/vulnerabilities`);
  if (!res.ok) throw new Error("Failed to fetch vulnerabilities");
  return res.json();
}

export async function createIncident(data) {
  const res = await fetch(`${API_BASE_URL}/incidents`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create incident");
  return res.json();
}

export async function updateVulnerabilityStatus(id, status) {
  const res = await fetch(`${API_BASE_URL}/vulnerabilites/${id}/status`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status }),
  });
  if (!res.ok) throw new Error("Failed to update vulnerability status");
  return res.json();
}
