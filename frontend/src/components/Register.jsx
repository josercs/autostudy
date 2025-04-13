import React, { useState } from 'react';
import { registerUser } from '../utils/api';

const Register = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await registerUser(formData);
      setSuccess(data); // Armazena a resposta de sucesso
      setError(null);
    } catch (error) {
      setError(error.response?.data || 'Erro ao registrar.');
      setSuccess(null);
    }
  };

  return (
    <div>
      <h2>Registrar</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
        />
        <button type="submit">Registrar</button>
      </form>
      {error && <p style={{ color: 'red' }}>{JSON.stringify(error)}</p>}
      {success && (
        <div style={{ color: 'green' }}>
          <p>Registro bem-sucedido!</p>
          <p>Usuário: {success.username}</p>
          <p>Email: {success.email}</p>
        </div>
      )}
    </div>
  );
};

export default Register;