import { useState } from "react";
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  MenuItem,
  FormControl,
  InputLabel,
  Select,
} from "@mui/material";
import { vulnerabilities } from "../../data/vulnerabilities";

export default function CreateIncidentDialog() {
  const [open, setOpen] = useState(false);
  const [form, setForm] = useState({
    vulnerability: "",
    assignedTo: "",
    priority: "High",
    description: "",
  });

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = () => {
    console.log("Incident créé :", form);
    setOpen(false);
  };

  return (
    <>
      <Button variant="contained" onClick={() => setOpen(true)}>
        + Create Incident
      </Button>

      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>Create Security Incident</DialogTitle>
        <DialogContent sx={{ display: "flex", flexDirection: "column", gap: 2, mt: 1 }}>
          <FormControl fullWidth>
            <InputLabel>Vulnerability</InputLabel>
            <Select
              name="vulnerability"
              value={form.vulnerability}
              onChange={handleChange}
              label="Vulnerability"
            >
              {vulnerabilities.map((v) => (
                <MenuItem key={v.id} value={v.name}>
                  {v.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <TextField
            label="Assigned To"
            name="assignedTo"
            value={form.assignedTo}
            onChange={handleChange}
            placeholder="analyst@company.com"
            fullWidth
          />
          <FormControl fullWidth>
            <InputLabel>Priority</InputLabel>
            <Select
              name="priority"
              value={form.priority}
              onChange={handleChange}
              label="Priority"
            >
              {["Critical", "High", "Medium", "Low"].map((p) => (
                <MenuItem key={p} value={p}>
                  {p}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <TextField
            label="Description"
            name="description"
            value={form.description}
            onChange={handleChange}
            multiline
            rows={3}
            placeholder="Investigation required..."
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpen(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleSubmit}>
            Create Incident
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
}
