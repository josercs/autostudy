import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";
import Mascote from "../components/Mascote.jsx";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";

const fallbackAnimation = {
  v: "5.9.1",
  fr: 30,
  ip: 0,
  op: 30,
  w: 512,
  h: 512,
  layers: [{
    ty: 4,
    shapes: [{
      ty: "gr",
      it: [
        { ty: "el", p: { a: 0, k: [256,256] }, s: { a: 0, k: [50,50] } },
        { ty: "fl", c: { a: 0, k: [0.35,0.78,0.98,1] } }
      ]
    }]
  }]
};

export default function Onboarding() {
  const { user, completarOnboarding } = useAuth(); // Acessa os dados de autenticação
  const navigate = useNavigate(); // Função para navegação entre páginas

  const [animationData, setAnimationData] = useState(null);
  const [etapa, setEtapa] = useState(0); // Estado para controlar qual etapa do onboarding o usuário está
  const [selectedStyle, setSelectedStyle] = useState(""); // Estilo de aprendizagem selecionado
  const [horasEstudo, setHorasEstudo] = useState("5"); // Horas de estudo por dia
  const [loading, setLoading] = useState(false); // Estado de carregamento
  const [error, setError] = useState(null); // Estado de erro
  const mascoteRef = useRef(null); // Referência para o componente de animação

  const etapas = [
    "Bem-vindo ao seu aprendizado personalizado!",
    "Vamos descobrir seu estilo de aprendizagem",
    "Configure sua rotina de estudos",
    "Tudo pronto! Vamos começar?"
  ];

  // Verifica se o onboarding já foi completado e redireciona para o painel
  useEffect(() => {
    if (user?.onboarding_completo) {
      navigate('/painel');
    }
  }, [user, navigate]);

  // Carrega a animação do mascote
  useEffect(() => {
    const loadAnimation = async () => {
      try {
        const response = await import("../assets/mascote.json");
        setAnimationData(response.default);
      } catch (error) {
        console.error("Erro ao carregar animação:", error);
        setAnimationData(fallbackAnimation); // Usa a animação fallback se houver erro
      }
    };

    loadAnimation();
  }, []);

  // Reproduz a animação sempre que a etapa ou estilo de aprendizagem mudar
  useEffect(() => {
    if (mascoteRef.current) {
      mascoteRef.current.play();
    }
  }, [etapa, selectedStyle]);

  // Função para salvar os dados do onboarding no backend
  const salvarNoBackend = async () => {
    setLoading(true);
    try {
      await completarOnboarding({
        estilo_aprendizado: selectedStyle,
        horas_estudo: parseInt(horasEstudo),
        trilha: "frontend"
      });

      navigate('/painel'); // Redireciona para o painel após o onboarding
    } catch (err) {
      setError(err.response?.data?.message || err.message);
      
      if (err.response?.status === 401) {
        navigate('/login');
      }
    } finally {
      setLoading(false);
    }
  };

  // Função para avançar para a próxima etapa
  const avancar = () => {
    if (etapa === 1) {
      localStorage.setItem("estiloAprendizado", selectedStyle); // Armazena o estilo de aprendizagem
    }
    
    if (etapa < etapas.length - 1) {
      setEtapa(etapa + 1); // Avança para a próxima etapa
    } else {
      salvarNoBackend(); // Salva os dados e conclui o onboarding
    }
  };

  // Função para explorar depois sem completar o onboarding
  const explorarDepois = () => {
    navigate('/painel');
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-blue-100 to-blue-300 p-4">
      <div className="w-48 h-48 mb-6 flex items-center justify-center">
        {animationData && (
          <Mascote ref={mascoteRef} animationData={animationData} size="180px" loop={false} />
        )}
      </div>

      <h1 className="text-3xl font-bold text-center mb-6">{etapas[etapa]}</h1>

      {etapa === 0 && (
        <p className="text-xl mb-6 text-center">
          Para começar, precisamos entender seu estilo de aprendizagem. Vamos lá!
        </p>
      )}

      {etapa === 1 && (
        <div className="w-full text-center">
          <button
            onClick={() => setSelectedStyle("Visual")}
            className={`p-3 m-2 rounded-lg ${selectedStyle === "Visual" ? "bg-blue-500 text-white" : "bg-white text-blue-500 border"}`}
          >
            Estilo Visual
          </button>
          <button
            onClick={() => setSelectedStyle("Auditivo")}
            className={`p-3 m-2 rounded-lg ${selectedStyle === "Auditivo" ? "bg-blue-500 text-white" : "bg-white text-blue-500 border"}`}
          >
            Estilo Auditivo
          </button>
          <button
            onClick={() => setSelectedStyle("Cinestésico")}
            className={`p-3 m-2 rounded-lg ${selectedStyle === "Cinestésico" ? "bg-blue-500 text-white" : "bg-white text-blue-500 border"}`}
          >
            Estilo Cinestésico
          </button>
        </div>
      )}

      {etapa === 2 && (
        <div className="w-full text-center">
          <input
            type="number"
            value={horasEstudo}
            onChange={(e) => setHorasEstudo(e.target.value)}
            className="p-3 rounded-lg border border-blue-500 w-20 text-center"
          />
          <span className="text-xl"> horas de estudo por dia</span>
        </div>
      )}

      {etapa === 3 && (
        <div className="w-full text-center">
          <p className="mb-6 text-xl">Pronto! Agora você está preparado para começar seus estudos!</p>
        </div>
      )}

      <div className="w-full text-center mt-6">
        <button onClick={avancar} className="bg-blue-500 text-white p-4 rounded-lg">
          {etapa === etapas.length - 1 ? (loading ? "Finalizando..." : "Começar agora!") : "Próxima Etapa"}
        </button>
        <button onClick={explorarDepois} className="bg-white text-blue-500 p-4 rounded-lg ml-4">
          Explorar depois
        </button>
      </div>
    </div>
  );
}
