import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#0d47a1", // navy blue
    },
    background: {
      default: "#0a192f", // dark navy
      paper: "#112240",   // lighter navy
    },
    text: {
      primary: "#e6f1ff",
    },
  },
  typography: {
    fontFamily: "Arial, sans-serif",
  },
});

export default theme;