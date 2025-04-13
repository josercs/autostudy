import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import config from "../utils/config";
import { FaUser, FaLock, FaSignInAlt } from 'react-icons/fa';
import './Login.css';
import { Link } from 'react-router-dom';
import { useAuth } from "../AuthContext"; // <-- ADICIONADO

const Login = () => {
  const [credentials, setCredentials] = useState({ username: '', password: '' });
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const { login: loginContext } = useAuth(); // <-- ADICIONADO

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      const response = await axios.post(
        `${config.API_BASE_URL}${config.ENDPOINTS.LOGIN}`,
        credentials
      );

      if (response.status === 200) {
        const { access, refresh, user_id, nome, avatar, nivel, xp } = response.data;
      
        // Salva no localStorage
        localStorage.setItem('access', access);
        localStorage.setItem('refresh', refresh);
        localStorage.setItem('user_id', user_id);
        if (nome) localStorage.setItem('nome', nome);
        if (avatar) localStorage.setItem('avatar', avatar);
        if (nivel) localStorage.setItem('nivel', nivel);
        if (xp) localStorage.setItem('xp', xp);
      
        // Salva no contexto
        loginContext({
          token: access,
          user_id,
          nome: nome || credentials.username, // fallback
          avatar: avatar || '',              // default vazio
          nivel: nivel || 1,                 // padrão inicial
          xp: xp || 0                        // padrão inicial
        });
      
        navigate('/painel');
      }
    } catch (error) {
      setError(error.response?.data?.detail || 'Erro ao fazer login');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">
          <FaSignInAlt className="icon" /> Login
        </h2>
        <form onSubmit={handleSubmit} className="login-form">
          <div className="input-group">
            <FaUser className="input-icon" />
            <input
              type="text"
              name="username"
              placeholder="Nome de usuário"
              value={credentials.username}
              onChange={handleChange}
              required
              minLength={3}
            />
          </div>
          <div className="input-group">
            <FaLock className="input-icon" />
            <input
              type="password"
              name="password"
              placeholder="Senha"
              value={credentials.password}
              onChange={handleChange}
              required
              minLength={6}
            />
          </div>
          {error && <div className="error-message">{error}</div>}
          <button type="submit" className="login-button" disabled={isLoading}>
            {isLoading ? 'Carregando...' : 'Entrar'}
          </button>
        </form>
        <div className="login-footer">
          <p>Não tem uma conta? <Link to="/register">Cadastre-se</Link></p>
          <p><Link to="/forgot-password">Esqueceu sua senha?</Link></p>
        </div>
      </div>
    </div>
  );
};

export default Login;
