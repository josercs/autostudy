import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1>Bem-vindo ao Sistema de Estudos</h1>
      <p>Explore como podemos ajudar você a alcançar seus objetivos de aprendizado.</p>
      <div className="home-links">
        <Link to="/login">Login</Link>
        <Link to="/register">Cadastro</Link>       
        <Link to="/about">Sobre Nós</Link>
        <Link to="/contact">Contato</Link>

      </div>
    </div>
  );
};

export default Home;