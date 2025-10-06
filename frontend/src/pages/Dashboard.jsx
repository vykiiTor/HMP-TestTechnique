import {useEffect, useState} from "react";
import { Container, Typography, Stack, Button } from "@mui/material";
//import { vulnerabilities } from "../data/vulnerabilities"; removed bc it was had coded info
import VulnerabilityCard from "../components/VulnerabilityComponent/VulnerabilityCard";
import Category from "../components/CategoryComponent/Category";
import IncidentCreate from "../components/IncidentCreateComponent/IncidentCreate";
import { getVulnerabilities } from "../apiConnection/connection";

export default function Dashboard() {
  const [filter, setFilter] = useState("All");
  const [vulnerabilities, setVulnerabilities] = useState([]);

  useEffect(() => {
    getVulnerabilities()
      .then((data) => setVulnerabilities(data))
      .catch((err) => console.error("API error:", err));
  }, []);

  const filtered =
    filter === "All"
      ? vulnerabilities
      : vulnerabilities.filter((v) => v.severity === filter);

  const counts = {
    Critical: vulnerabilities.filter((v) => v.severity === "Critical").length,
    High: vulnerabilities.filter((v) => v.severity === "High").length,
    Medium: vulnerabilities.filter((v) => v.severity === "Medium").length,
    Low: vulnerabilities.filter((v) => v.severity === "Low").length,
  };

  return (
    <Container sx={{ py: 4 }}>
      <Typography variant="h4" color="primary" gutterBottom>
        SOC Dashboard
      </Typography>
      <Typography color="text.secondary" gutterBottom>
        Security Operations Center - Vulnerability Management
      </Typography>

      <Category counts={counts} />

      <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 2 }}>
        <Stack direction="row" spacing={1}>
          {["All", "Critical", "High", "Medium", "Low"].map((lvl) => (
            <Button
              key={lvl}
              variant={filter === lvl ? "contained" : "outlined"}
              onClick={() => setFilter(lvl)}
            >
              {lvl}
            </Button>
          ))}
        </Stack>
        <IncidentCreate />
      </Stack>

      <Stack spacing={2}>
        {filtered.map((v) => (
          <VulnerabilityCard key={v.id} vuln={v} />
        ))}
      </Stack>
    </Container>
  );
}
