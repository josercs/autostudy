// src/components/CardRecomendacao.jsx
const CardRecomendacao = ({ titulo, descricao, tipo, acao }) => {
    return (
      <div onClick={acao} className="card-recomendacao">
        <h3>{titulo}</h3>
        <p>{descricao}</p>
      </div>
    );
  };
  
  export default CardRecomendacao;
  