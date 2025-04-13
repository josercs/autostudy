import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

const SidebarAcademica = ({ usuario, onLogout, onNavigate }) => {
  const menuItems = [
    { label: 'Dashboard', path: '/dashboard' },
    { label: 'Meus Cursos', path: '/cursos' },
    { label: 'Desempenho', path: '/desempenho' },
    { label: 'Calendário', path: '/calendario' },
    { label: 'Conquistas', path: '/conquistas' }
  ];

  // Extrai os dados do usuário com fallbacks seguros
  const nome = usuario?.nome || 'Usuário';
  const avatar = usuario?.avatar || 'https://i.pravatar.cc/159?img=40';
  const nivel = usuario?.nivel || 1;
  const progresso = usuario?.progresso ?? 65; // Usando ?? para considerar apenas null/undefined

  return (
    <div className="sidebar">
      {/* Cabeçalho com logo e nome resumido */}
      <div className="sidebar-header">
        <div className="sidebar-logo">
          {nome.charAt(0).toUpperCase()}
        </div>
        <h1 className="sidebar-title">
          {nome.split(' ')[0]}
        </h1>
      </div>

      {/* Seção de perfil do usuário */}
      <div className="perfil-usuario">
        <img 
          src={avatar} 
          alt={nome} 
          className="avatar" 
          onError={(e) => {
            e.target.src = 'https://i.pravatar.cc/150?img=3';
          }}
        />
        <h3>{nome}</h3>
        <div className="nivel-usuario">
          <span className="nivel-tag">Nível {nivel}</span>
          <div className="progresso-nivel">
            <div 
              className="barra-progresso" 
              style={{ width: `${progresso}%` }}
            ></div>
          </div>
        </div>
      </div>


      {/* Menu de navegação */}
      <nav className="menu-navegacao">
        <ul>
          {menuItems.map((item, index) => (
            <li key={`${item.path}-${index}`}>
              <NavLink 
                to={item.path}
                className={({ isActive }) => 
                  isActive ? 'active' : ''
                }
                onClick={() => onNavigate && onNavigate(item.path)}
              >
                <span className="menu-item-content">
                  {item.label}
                </span>
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>

      {/* Rodapé com botão de sair */}
      <div className="sidebar-footer">
        <button onClick={onLogout} className="botao-sair">
          <span className="icone-sair">⎋</span>
          <span className="texto-sair">Sair</span>
        </button>
      </div>
    </div>
  );
};

export default SidebarAcademica;