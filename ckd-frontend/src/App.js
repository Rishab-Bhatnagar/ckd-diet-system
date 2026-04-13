import { useState } from "react";
import { Container, Typography, Paper } from "@mui/material";
import DietForm from "./components/DietForm";
import DietResult from "./components/DietResult";
import { getDiet } from "./services/api";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (stage, diabetes, hypertension) => {
    try {
      setLoading(true);
      setError(null);

      const result = await getDiet(stage, diabetes, hypertension);
      setData(result);
    } catch (err) {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md"sx={{ mt: 4,}}>

      <Paper elevation={4} sx={{ p: 3, backgroundColor: "#112240", borderRadius: "12px",  }}>
        <Typography variant="h4" align="center" gutterBottom sx={{ fontWeight: "bold", letterSpacing: "1px"}}>
          CKD Diet Recommendation System
        </Typography>

        <DietForm onSubmit={handleSubmit} />

        {loading && <Typography>⏳ Loading...</Typography>}
        {error && <Typography color="error">{error}</Typography>}

        {!loading && !error && <DietResult data={data} />}
      </Paper>
    </Container>
  );
}

export default App;