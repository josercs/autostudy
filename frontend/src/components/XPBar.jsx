// src/components/XPBar.jsx
import React from 'react';
import './XPBar.css'; // Crie este arquivo se necessário

const XPBar = ({ xpAtual, xpTotal }) => {
  const porcentagem = Math.min(100, (xpAtual / xpTotal) * 100);
  
  return (
    <div className="xp-bar-container">
      <div className="xp-bar" style={{ width: `${porcentagem}%` }}></div>
      <span className="xp-text">{xpAtual}/{xpTotal} XP</span>
    </div>
  );
};

export default XPBar;