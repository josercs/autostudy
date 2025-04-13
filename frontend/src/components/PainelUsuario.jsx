import React, { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from "../AuthContext";

import { 
  fetchProgresso, 
  fetchCursosAtivos,
  fetchSimuladosRecentes,
  fetchRecomendacoes 
} from '../services/apiService';
import './painel.css';

import { 
  SidebarAcademica,
  HeaderUsuario,
  CardMetrica,
  GraficoDesempenho,
  ListaCursos,
  CalendarioEstudos,
  CardRecomendacao
} from '../components';

const PainelUsuario = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const [carregando, setCarregando] = useState(true);
  const [state, setState] = useState({
    progresso: null,
    cursos: [],
    simulados: [],
    recomendacoes: []
  });

  // Aguarda carregamento do AuthContext
  useEffect(() => {
    const timeout = setTimeout(() => {
      setCarregando(false);
    }, 100);

    return () => clearTimeout(timeout);
  }, []);

  // Redireciona caso não haja usuário
  useEffect(() => {
    if (!carregando && !user) {
      navigate('/login');
    }
  }, [carregando, user, navigate]);
  

  // Carrega dados após confirmar usuário
  useEffect(() => {
    const carregarDados = async () => {
      try {
        const [progresso, cursos, simulados, recomendacoes] = await Promise.all([
          fetchProgresso(user.id),
          fetchCursosAtivos(user.id),
          fetchSimuladosRecentes(user.id),
          fetchRecomendacoes(user.id)
        ]);

        setState({
          progresso: {
            ...progresso,
            // Adiciona progresso para o perfil do sidebar
            nivel: user.nivel,
            progresso: Math.round((user.xp / (user.nivel * 1000)) * 100)
          },
          cursos,
          simulados,
          recomendacoes
        });
      } catch (erro) {
        console.error("Falha ao carregar dados:", erro);
        logout();
      }
    };

    if (user) {
      carregarDados();
    }
  }, [user, logout]);

  if (carregando || !user || !state.progresso) {
    return (
      <div className="tela-carregamento">
        <div className="spinner"></div>
        <p>Carregando seu painel...</p>
      </div>
    );
  }

  return (
    <div className="container-painel">
      <SidebarAcademica
        usuario={{
          nome: user.nome, // Garanta que isso está vindo corretamente
          avatar: user.avatar,
          nivel: user.nivel,
          progresso: state.progresso?.progresso
        }}
        onLogout={logout}
        onNavigate={navigate}
      />

      <main className="conteudo-principal">
        <HeaderUsuario
          nome={user.nome}
          avatar={user.avatar}
          nivel={user.nivel}
          xp={user.xp}
        />

        <section className="secao-metricas">
          <CardMetrica 
            titulo="Progresso Geral"
            valor={`${state.progresso.geral}%`}
            icone="📈"
            variacao={state.progresso.variacao}
            corDestaque="#00dbde"
          />
          <CardMetrica 
            titulo="Cursos Ativos"
            valor={state.cursos.length}
            icone="🎓"
            corDestaque="#fc00ff"
          />
          <CardMetrica 
            titulo="Simulados Realizados"
            valor={state.simulados.length}
            icone="📝"
            corDestaque="#ff6b6b"
          />
        </section>

        <div className="grade-conteudo">
          <section className="card-grande desempenho">
            <h2>Seu Desempenho</h2>
            <GraficoDesempenho dados={state.progresso.detalhado} />
          </section>

          <section className="card-grande cursos">
            <div className="cabecalho-secao">
              <h2>Seus Cursos</h2>
              <Link to="/cursos" className="link-ver-todos">
                Ver todos →
              </Link>
            </div>
            <ListaCursos 
              cursos={state.cursos.slice(0, 3)} 
              onSelecionar={(id) => navigate(`/curso/${id}`)}
            />
          </section>

          <section className="card-grande recomendacoes">
            <div className="cabecalho-secao">
              <h2>Recomendado Para Você</h2>
              <Link to="/recomendacoes" className="link-ver-todos">
                Ver mais →
              </Link>
            </div>
            <div className="grade-recomendacoes">
              {state.recomendacoes.map((item, index) => (
                item && item.titulo && item.descricao && item.link ? (
                  <CardRecomendacao 
                    key={index}
                    tipo={item.tipo}
                    titulo={item.titulo}
                    descricao={item.descricao}
                    acao={() => navigate(item.link)}
                  />
                ) : null
              ))}
            </div>
          </section>

          <section className="card-grande calendario">
            <h2>Seu Calendário</h2>
            <CalendarioEstudos 
              eventos={state.progresso.calendario}
              onEventoClick={(id) => navigate(`/aula/${id}`)}
            />
          </section>
        </div>
      </main>
    </div>
  );
};

export default PainelUsuario;