import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/predict';

export const sendThreatRequest = async (payload) => {
  try {
    const response = await axios.post(API_URL, payload);
    return response.data;
  } catch (error) {
    return { error: error.message || "Unknown error" };
  }
};
