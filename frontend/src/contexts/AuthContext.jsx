// AuthContext.jsx
import { createContext, useContext, useState, useEffect, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [onboardingCompleto, setOnboardingCompleto] = useState(false);

  // Função de verificação de token
  const verifyToken = async () => {
    try {
      const token = localStorage.getItem('access');
      if (token) {
        const response = await axios.post('http://localhost:8000/api/auth/token/verify/', { token });
        return true; // Token é válido
      }
      return false; // Não há token
    } catch (error) {
      // Tenta renovar o token
      const refreshToken = localStorage.getItem('refresh');
      if (refreshToken) {
        try {
          const response = await axios.post('http://localhost:8000/api/auth/token/refresh/', { refresh: refreshToken });
          const newAccess = response.data.access;
          localStorage.setItem('access', newAccess); // Atualiza o token
          axios.defaults.headers.common['Authorization'] = `Bearer ${newAccess}`;
          return true;
        } catch (refreshError) {
          console.warn("Erro ao renovar o token. Realizando logout.");
          logout(); // Se não conseguir renovar o token, faz logout
          return false;
        }
      }
      return false;
    }
  };

  // Carrega os dados do usuário e verifica o token
  useEffect(() => {
    const loadUserData = async () => {
      try {
        const userData = localStorage.getItem('user');
        const token = localStorage.getItem('access');

        if (userData && token) {
          const parsedUser = JSON.parse(userData);
          const isTokenValid = await verifyToken();
          if (isTokenValid) {
            setUser(parsedUser);
            setOnboardingCompleto(parsedUser.onboarding_completo || false);
          } else {
            console.warn('Token inválido ou expirado. Realizando logout.');
            logout();
          }
        }
      } catch (error) {
        console.error("Erro ao carregar os dados do usuário:", error);
        logout();
      } finally {
        setLoading(false);
      }
    };

    loadUserData();
  }, []);

  const login = useCallback(async (credentialsOrUser) => {
    setLoading(true);
    try {
      let userData;

      if (credentialsOrUser.username && credentialsOrUser.password) {
        const response = await axios.post('http://localhost:8000/api/auth/login/', credentialsOrUser);
        const { access, refresh, user: apiUserData } = response.data;
        userData = { token: access, refreshToken: refresh, ...apiUserData };
      } else {
        userData = credentialsOrUser;
      }

      const userFinal = {
        token: userData.token,
        refreshToken: userData.refreshToken,
        user_id: userData.user_id,
        nome: userData.nome || userData.username || '',
        avatar: userData.avatar || '',
        nivel: userData.nivel || 1,
        xp: userData.xp || 0,
        onboarding_completo: userData.onboarding_completo || false
      };

      setUser(userFinal);
      setOnboardingCompleto(userFinal.onboarding_completo);

      localStorage.setItem('user', JSON.stringify(userFinal));
      localStorage.setItem('access', userFinal.token);
      localStorage.setItem('refresh', userFinal.refreshToken);
      localStorage.setItem('onboardingCompleto', userFinal.onboarding_completo.toString());

      return userFinal;
    } catch (error) {
      console.error('Erro durante o login:', error);
      throw error;
    } finally {
      setLoading(false);
    }
  }, []);

  const logout = useCallback(() => {
    try {
      setUser(null);
      setOnboardingCompleto(false);
      localStorage.removeItem('user');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      localStorage.removeItem('onboardingCompleto');
    } catch (error) {
      console.error('Erro durante o logout:', error);
    }
  }, []);

  // AuthContext.jsx
const completarOnboarding = async (data) => {
  try {
    const token = localStorage.getItem('token');  // Supondo que o token esteja no localStorage
    const response = await axios.post('http://localhost:8000/user/onboarding/', data, {
      headers: {
        'Authorization': `Bearer ${token}`,
      }
    });
    console.log('Onboarding completado com sucesso', response.data);
  } catch (error) {
    console.error('Erro ao completar onboarding:', error);
  }
};


  const contextValue = {
    user,
    loading,
    isAuthenticated: !!user?.token,
    onboardingCompleto,
    login,
    logout,
    completarOnboarding,
    setOnboardingCompleto
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de um AuthProvider');
  }
  return context;
};
