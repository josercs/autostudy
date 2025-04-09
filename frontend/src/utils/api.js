import axios from 'axios';
import config from '../config';

export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${config.API_BASE_URL}${config.ENDPOINTS.REGISTER}`, {
      username: userData.username,
      email: userData.email,
      password: userData.password,
    });
    return response.data;
  } catch (error) {
    console.error('Erro no registro:', error.response.data);
    throw error;
  }
};