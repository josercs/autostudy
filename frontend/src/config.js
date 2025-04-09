// Forma correta de exportar (usando export default)
const config = {
  API_BASE_URL: process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000',
  ENDPOINTS: {
    LOGIN: '/api/token/',
    REFRESH_TOKEN: '/api/token/refresh/',
    REGISTER: '/register/',
  },
};

export default config; // Esta linha estava faltando ou estava incorreta