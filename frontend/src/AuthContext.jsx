import React, { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // ✅ Nome da variável agora é 'user'

  // Verifica localStorage ao iniciar
  useEffect(() => {
    const token = localStorage.getItem('access');
    const user_id = localStorage.getItem('user_id');
    const nome = localStorage.getItem('nome');
    const avatar = localStorage.getItem('avatar');
    const nivel = parseInt(localStorage.getItem('nivel')) || 1;
    const xp = parseInt(localStorage.getItem('xp')) || 0;
  
    if (token && user_id && nome) {
      setUser({ token, id: user_id, nome, avatar, nivel, xp });
    }
  }, []);

  const login = (dados) => {
    setUser(dados);

    // Salva no localStorage
    localStorage.setItem('access', dados.token);
    localStorage.setItem('user_id', dados.user_id);
    if (dados.nome) localStorage.setItem('nome', dados.nome); // se existir
  };

  const logout = () => {
    setUser(null);
    localStorage.clear();
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
