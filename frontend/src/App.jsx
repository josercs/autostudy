import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import PainelUsuario from './components/PainelUsuario';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/painel" element={<PainelUsuario />} />
    </Routes>
  );
}

export default App;
