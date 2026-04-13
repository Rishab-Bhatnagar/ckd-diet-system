import { Card, CardContent, Typography, Grid } from "@mui/material";

function SectionCard({ title, items }) {
  return (
    <Card sx={{ mb: 2 }}>
      <CardContent>
        <Typography variant="h6">{title}</Typography>
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              {item.name} ({item.calories} kcal)
            </li>
          ))}
        </ul>
      </CardContent>
    </Card>
  );
}

function DietResult({ data }) {
  if (!data) return null;

  return (
    <div>
      <Typography variant="h5" gutterBottom>
        Diet Plan
      </Typography>

      <Grid container spacing={2}>
        <Grid item xs={12} md={4}>
          <SectionCard title="Breakfast" items={data.diet_plan.breakfast} />
        </Grid>
        <Grid item xs={12} md={4}>
          <SectionCard title="Lunch" items={data.diet_plan.lunch} />
        </Grid>
        <Grid item xs={12} md={4}>
          <SectionCard title="Dinner" items={data.diet_plan.dinner} />
        </Grid>
      </Grid>

      <Typography variant="h5" sx={{ mt: 3 }}>
        Nutrition Summary
      </Typography>

      <Typography>
        Calories: {data.nutrition_summary.calories}
      </Typography>
      <Typography>Protein: {data.nutrition_summary.protein}</Typography>
      <Typography>Sodium: {data.nutrition_summary.sodium}</Typography>
      <Typography>Potassium: {data.nutrition_summary.potassium}</Typography>
    </div>
  );
}

export default DietResult;