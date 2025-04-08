import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../utils/axiosInstance';

const Dashboard = () => {
  // Adicione estes states
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [progress, setProgress] = useState([]);  // Se for usado
  const [studyPlan, setStudyPlan] = useState([]); // Se for usado

  const fetchData = async () => {
    try {
      const response = await axiosInstance.get('/study/progress/');
      setProgress(response.data.progress || []);
      setStudyPlan(response.data.study_plan || []);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);


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