import { useState } from "react";
import {
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Checkbox,
  FormControlLabel,
  Box,
} from "@mui/material";

function DietForm({ onSubmit }) {
  const [stage, setStage] = useState(1);
  const [diabetes, setDiabetes] = useState(false);
  const [hypertension, setHypertension] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(stage, diabetes, hypertension);
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mb: 3 }}>
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel>CKD Stage</InputLabel>
        <Select
          value={stage}
          label="CKD Stage"
          onChange={(e) => setStage(e.target.value)}
        >
          {[1, 2, 3, 4, 5].map((s) => (
            <MenuItem key={s} value={s}>
              Stage {s}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControlLabel
        control={
          <Checkbox
            checked={diabetes}
            onChange={(e) => setDiabetes(e.target.checked)}
          />
        }
        label="Diabetes"
      />

      <FormControlLabel
        control={
          <Checkbox
            checked={hypertension}
            onChange={(e) => setHypertension(e.target.checked)}
          />
        }
        label="Hypertension"
      />

      <Button
  variant="contained"
  fullWidth
  type="submit"
  sx={{
    mt: 2,
    backgroundColor: "#0d47a1",
    "&:hover": {
      backgroundColor: "#1565c0",
      transform: "scale(1.02)",
    },
    transition: "0.3s",
  }}
>
  Get Diet Plan
</Button>
    </Box>
  );
}

export default DietForm;