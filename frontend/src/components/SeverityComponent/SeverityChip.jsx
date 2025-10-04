import Chip from "@mui/material/Chip";

export default function SeverityChip({ level }) {
  const colorMap = {
    Critical: "error",
    High: "warning",
    Medium: "info",
    Low: "success",
  };
  return <Chip label={level} color={colorMap[level]} size="small" />;
}
