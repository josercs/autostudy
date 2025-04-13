// src/services/apiService.js

export const fetchProgresso = async (userId) => {
    // Simulação de uma chamada API
    return {
      geral: 75,
      variacao: "+5%",
      detalhado: [/* dados do gráfico */],
      calendario: [/* eventos de estudo */]
    };
  };
  
  export const fetchCursosAtivos = async (userId) => {
    return [
      { id: 1, titulo: "Matemática", progresso: 60 },
      { id: 2, titulo: "Português", progresso: 80 }
    ];
  };
  
  export const fetchSimuladosRecentes = async (userId) => {
    return [
      { id: 1, titulo: "Simulado ENEM - Março", nota: 720 },
      { id: 2, titulo: "Simulado Redação", nota: 880 }
    ];
  };
  
  export const fetchRecomendacoes = async (userId) => {
    return [
      { tipo: "videoaula", titulo: "Funções Quadráticas", descricao: "Aula recomendada", link: "/aula/funcao-quadratica" },
      { tipo: "artigo", titulo: "Como melhorar sua redação", descricao: "Dicas práticas", link: "/artigos/redacao" }
    ];
  };
  