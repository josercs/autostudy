import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.module.css'; // Ou use CSS Modules: import styles from './Home.module.css'

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Bem-vindo ao Sistema de Estudos</h1>
        <p className="home-subtitle">Explore como podemos ajudar você a alcançar seus objetivos de aprendizado.</p>
      </header>

      <nav className="home-navigation">
        <Link to="/login" className="home-link">
          <div className="link-card">
            <span>Login</span>
            <p>Acesse sua conta</p>
          </div>
        </Link>
        
        <Link to="/register" className="home-link">
          <div className="link-card">
            <span>Cadastro</span>
            <p>Crie sua conta</p>
          </div>
        </Link>       
        
        <Link to="/about" className="home-link">
          <div className="link-card">
            <span>Sobre Nós</span>
            <p>Conheça nossa plataforma</p>
          </div>
        </Link>
        
        <Link to="/chat" className="home-link">
          <div className="link-card">
            <span>Contato</span>
            <p>Fale conosco</p>
          </div>
        </Link>
        
      </nav>
    </div>
  );
};

export default Home;