import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../utils/axiosInstance';

const Dashboard = () => {
  // Adicione estes states
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [progress, setProgress] = useState([]);  // Se for usado
  const [studyPlan, setStudyPlan] = useState([]); // Se for usado
  const [loading, setLoading] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axiosInstance.get('/study/progress/');
      if (response.status === 200) {
        setProgress(response.data.progress || []);
        setStudyPlan(response.data.study_plan || 'O plano de estudos será gerado com base no seu progresso.');
      } else {
        throw new Error(`Erro inesperado: ${response.status}`);
      }
    } catch (err) {
      console.error('Erro ao carregar os dados:', err);
      const errorMessage = err.response?.data?.detail || 'Erro ao carregar os dados. Tente novamente mais tarde.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  if (error) {
    return (
      <div>
        <p>Erro: {error}</p>
        <button onClick={fetchData}>Tentar novamente</button>
      </div>
    );
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <h2>Seu Progresso</h2>
      <ul>
        {progress.map((item) => (
          <li key={item.id}>
            {item.course_name}: {item.progress_percentage}%
          </li>
        ))}
      </ul>
      <h2>Plano de Estudos</h2>
      <p>{studyPlan || 'O plano de estudos será gerado com base no seu progresso.'}</p>
    </div>
  );
};

export default Dashboard;