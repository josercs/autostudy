import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../utils/api';

const Register = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await registerUser(formData);
      setSuccess(data);
      setError(null);
      navigate('/login'); // Redireciona para o login após registro bem-sucedido
    } catch (error) {
      setError(error.response?.data || 'Erro ao registrar. Verifique os dados e tente novamente.');
      setSuccess(null);
    }
  };

  return (
    <div className="register-container">
      <h2>Registrar</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Nome de usuário"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="E-mail"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Senha"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Registrar</button>
      </form>

      {error && (
        <p style={{ color: 'red', marginTop: '10px' }}>
          {typeof error === 'string' ? error : JSON.stringify(error)}
        </p>
      )}

      {success && (
        <div style={{ color: 'green', marginTop: '10px' }}>
          <p>Registro bem-sucedido!</p>
          <p>Usuário: {success.username}</p>
          <p>Email: {success.email}</p>
        </div>
      )}
    </div>
  );
};

export default Register;
