import React, { useState } from 'react';
import axios from 'axios';

const ChatTutor = () => {
  const [mensagem, setMensagem] = useState('');
  const [resposta, setResposta] = useState('');

  const enviarMensagem = async () => {
    try {
      const res = await axios.post('/api/tutor/chat/', { mensagem });
      setResposta(res.data.resposta);
    } catch (error) {
      setResposta('Erro ao se comunicar com o tutor.');
      console.error(error.response?.data || error.message);
    }
  };

  return (
    <div>
      <h1>Bot Tutor</h1>
      <textarea
        value={mensagem}
        onChange={(e) => setMensagem(e.target.value)}
        placeholder="Digite sua mensagem..."
      />
      <button onClick={enviarMensagem}>Enviar</button>
      <div>
        <h2>Resposta:</h2>
        <p>{resposta}</p>
      </div>
    </div>
  );
};

export default ChatTutor;