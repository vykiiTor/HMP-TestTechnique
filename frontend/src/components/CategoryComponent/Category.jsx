import { Grid, Card, CardContent, Typography } from "@mui/material";

export default function Category({ counts }) {
  const colors = {
    Critical: "error.main",
    High: "warning.main",
    Medium: "info.main",
    Low: "success.main",
  };

  return (
    <Grid container spacing={2} sx={{ my: 2 }}>
      {Object.keys(counts).map((key) => (
        <Grid item xs={6} md={3} key={key}>
          <Card sx={{ backgroundColor: "#1E1E1E", color: "#fff" }}>
            <CardContent>
              <Typography variant="h4" sx={{ color: colors[key] }}>
                {counts[key]}
              </Typography>
              <Typography variant="body2">{key}</Typography>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
}
