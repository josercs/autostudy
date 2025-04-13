import React, { useState, useEffect, useRef } from 'react';
import axiosInstance from '../utils/axiosInstance';
import './ChatTutor.css';

const ChatTutor = () => {
  // Estados
  const [mensagem, setMensagem] = useState('');
  const [historico, setHistorico] = useState([]);
  const [loading, setLoading] = useState(false);
  const [mostrarReacao, setMostrarReacao] = useState(false);
  const [emojiReacao, setEmojiReacao] = useState('🎉');
  const chatBoxRef = useRef(null);

  // Mensagens motivacionais
  const mensagensMotivacionais = [
    "🚀 Continue assim! Você está indo muito bem!",
    "🌟 Excelente pergunta! Isso mostra curiosidade.",
    "📚 Cada dúvida resolvida é um passo rumo à maestria.",
    "🧠 Aprender é um superpoder, e você está usando bem o seu!",
    "👏 Mandou bem! O aprendizado acontece um passo por vez."
  ];

  // Reações disponíveis
  const emojisReacao = ['✨', '🔥', '💡', '🎯', '👏', '💪'];

  // Efeito para rolar para baixo automaticamente
  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [historico]);

  // Geradores de conteúdo
  const gerarMensagemMotivacional = () => {
    const indiceAleatorio = Math.floor(Math.random() * mensagensMotivacionais.length);
    return mensagensMotivacionais[indiceAleatorio];
  };

  const gerarReacao = () => {
    const indiceAleatorio = Math.floor(Math.random() * emojisReacao.length);
    return emojisReacao[indiceAleatorio];
  };

  // Processamento de resposta
  const processarResposta = (data, perguntaUsuario) => {
    try {
      let respostaTutor = data?.resposta || data?.message || data;

      if (typeof respostaTutor === 'object') {
        respostaTutor = JSON.stringify(respostaTutor, null, 2);
      }

      if (!respostaTutor || typeof respostaTutor !== 'string') {
        return `Desculpe, não consegui entender a resposta para: "${perguntaUsuario}".`;
      }

      if (respostaTutor.trim() === perguntaUsuario.trim()) {
        return `Parece que houve um erro ao processar sua pergunta sobre "${perguntaUsuario}". Por favor, tente novamente.`;
      }

      if (respostaTutor.length < 10) {
        return `Sua pergunta sobre "${perguntaUsuario}" foi recebida, mas a resposta foi muito breve. Poderia reformular?`;
      }

      return respostaTutor;
    } catch (error) {
      console.error('Erro ao processar resposta:', error);
      return 'Ocorreu um erro ao processar a resposta. Por favor, tente novamente.';
    }
  };

  // Envio de mensagem
  const enviarMensagem = async () => {
    if (!mensagem.trim() || loading) return;

    const perguntaUsuario = mensagem;
    setLoading(true);
    
    try {
      // Adiciona mensagem do usuário ao histórico
      setHistorico(prev => [...prev, {
        emissor: 'usuario',
        texto: perguntaUsuario,
        timestamp: new Date().toISOString(),
      }]);

      setMensagem('');

      // Envia para a API
      const res = await axiosInstance.post('chat-tutor/', {
        mensagem: perguntaUsuario,
      });

      // Processa resposta
      const respostaTutor = processarResposta(res.data, perguntaUsuario);
      const mensagemMotivacional = gerarMensagemMotivacional();

      // Mostra reação visual
      setEmojiReacao(gerarReacao());
      setMostrarReacao(true);
      setTimeout(() => setMostrarReacao(false), 2500);

      // Adiciona respostas ao histórico
      setHistorico(prev => [
        ...prev,
        {
          emissor: 'tutor',
          texto: respostaTutor,
          timestamp: new Date().toISOString(),
        },
        {
          emissor: 'tutor',
          texto: mensagemMotivacional,
          timestamp: new Date().toISOString(),
        }
      ]);
    } catch (error) {
      console.error('Erro na comunicação com o tutor:', error);
      
      // Tratamento de erros específicos
      if (error.response?.status === 401) {
        setHistorico(prev => [...prev, {
          emissor: 'tutor',
          texto: 'Sua sessão expirou. Redirecionando para login...',
          timestamp: new Date().toISOString(),
        }]);
        setTimeout(() => window.location.href = '/login', 2000);
      } else {
        setHistorico(prev => [...prev, {
          emissor: 'tutor',
          texto: '⚠️ Estou tendo problemas técnicos. Por favor, tente novamente mais tarde.',
          timestamp: new Date().toISOString(),
        }]);
      }
    } finally {
      setLoading(false);
    }
  };

  // Renderização
  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Tutor IA</h2>
        <div className="status-indicator online">● Online</div>
      </div>

      <div className="chat-box" ref={chatBoxRef}>
        {historico.length === 0 && (
          <div className="chat-empty-state">
            <p>Digite sua primeira mensagem para começar a conversa!</p>
          </div>
        )}

        {historico.map((item, index) => (
          <div key={`${item.timestamp}-${index}`} className={`chat-message ${item.emissor}`}>
            <div className="message-header">
              <strong>{item.emissor === 'usuario' ? 'Você' : 'Tutor IA'}</strong>
              <span className="message-time">
                {new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </span>
            </div>
            <div className="message-content">
              {item.emissor === 'tutor' ? (
                <div style={{ whiteSpace: 'pre-line' }}>{item.texto}</div>
              ) : (
                item.texto
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="chat-message tutor typing-indicator">
            <div className="typing-dots">
              <span>.</span>
              <span>.</span>
              <span>.</span>
            </div>
          </div>
        )}

        {mostrarReacao && (
          <div className="emoji-reacao animate-pop">{emojiReacao}</div>
        )}
      </div>

      <div className="chat-input-area">
        <textarea
          value={mensagem}
          onChange={(e) => setMensagem(e.target.value)}
          placeholder="Digite sua mensagem para o tutor..."
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              enviarMensagem();
            }
          }}
          disabled={loading}
          rows={3}
        />
        <button
          onClick={enviarMensagem}
          disabled={loading || !mensagem.trim()}
          className={loading ? 'loading' : ''}
          aria-label="Enviar mensagem"
        >
          {loading ? <span className="button-loader"></span> : 'Enviar'}
        </button>
      </div>
    </div>
  );
};

export default ChatTutor;