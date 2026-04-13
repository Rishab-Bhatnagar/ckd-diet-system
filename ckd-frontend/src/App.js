import { useEffect } from "react";
import { getDiet } from "./services/api";

function App() {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getDiet(3, false, false);
        console.log("API Response:", data);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>CKD Diet Recommendation System</h1>
      <p>Check console for API response</p>
    </div>
  );
}

export default App;