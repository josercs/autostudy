// src/App.jsx
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import PainelUsuario from './components/PainelUsuario';
import Onboarding from './pages/Onboarding';
import Register from './components/Register'; // <- Importa o componente
import RequireAuth from './components/auth/RequireAuth';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} /> {/* <- Adiciona a rota aqui */}

      {/* Rotas protegidas */}
      <Route element={<RequireAuth />}>
        <Route path="/onboarding" element={<Onboarding />} />
      </Route>
      <Route element={<RequireAuth requireOnboarding={true} />}>
        <Route path="/painel" element={<PainelUsuario />} />
      </Route>
    </Routes>
  );
}

export default App;
