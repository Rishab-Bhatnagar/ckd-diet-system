const BASE_URL = "https://ckd-diet-system.onrender.com";

export const getDiet = async (stage, diabetes, hypertension) => {
  const url = `${BASE_URL}/recommend?stage=${stage}&diabetes=${diabetes}&hypertension=${hypertension}`;

  const response = await fetch(url);
  return response.json();
};