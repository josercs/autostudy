import React, { useState } from 'react';
import axiosInstance from '../utils/axiosInstance';
import './ChatTutor.css'; // Importa o CSS

const ChatTutor = () => {
  const [mensagem, setMensagem] = useState('');
  const [resposta, setResposta] = useState('');

  const enviarMensagem = async () => {
    try {
      const res = await axiosInstance.post('tutor/chat/', { mensagem });
      setResposta(res.data.resposta);
    } catch (error) {
      setResposta('Erro ao se comunicar com o tutor.');
      console.error(error.response?.data || error.message);
    }
  };

  return (
    <div className="chat-container">
      <h1 className="chat-header">Bot Tutor</h1>
      <textarea
        className="chat-textarea"
        value={mensagem}
        onChange={(e) => setMensagem(e.target.value)}
        placeholder="Digite sua mensagem..."
      />
      <button className="chat-button" onClick={enviarMensagem}>
        Enviar
      </button>
      {resposta && (
        <div className="chat-response">
          <h2>Resposta:</h2>
          <p>{resposta}</p>
        </div>
      )}
    </div>
  );
};

export default ChatTutor;