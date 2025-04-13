export default {
    API_BASE_URL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
    ENDPOINTS: {
      LOGIN: '/api/auth/login/',
      REGISTER: '/api/auth/register/',
      CHAT: '/api/tutor/chat/',
      PROGRESS: '/api/study/progress/'
    }
    
  };