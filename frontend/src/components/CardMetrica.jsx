import React from 'react';
import './cardMetrica.css';

const CardMetrica = ({ titulo, valor, icone, variacao }) => {
  return (
    <div className="card-metrica">
      <div className="cabecalho-metrica">
        <span className="icone-metrica">{icone}</span>
        <h3>{titulo}</h3>
      </div>
      <p className="valor-metrica">{valor}</p>
      {variacao && (
        <p className={`variacao-metrica ${variacao > 0 ? 'positiva' : 'negativa'}`}>
          {variacao > 0 ? '↑' : '↓'} {Math.abs(variacao)}%
        </p>
      )}
    </div>
  );
};

export default CardMetrica;