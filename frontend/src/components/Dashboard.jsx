import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../utils/axiosInstance';
import { 
  FaChartLine, 
  FaBook, 
  FaSync, 
  FaExclamationTriangle,
  FaCalendarAlt
} from 'react-icons/fa';
import './Dashboard.css';

const Dashboard = () => {
  const [progressData, setProgressData] = useState([]);
  const [studyPlan, setStudyPlan] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const [lastUpdated, setLastUpdated] = useState('');
  const navigate = useNavigate();

  const fetchDashboardData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [progressRes, planRes] = await Promise.all([
        axiosInstance.get('/study/progress/'),
        axiosInstance.get('/study/plan/')
      ]);

      if (progressRes.status === 200 && planRes.status === 200) {
        setProgressData(progressRes.data.progress || []);
        setStudyPlan(planRes.data.plan || 'Nenhum plano de estudos disponível.');
        setLastUpdated(new Date().toLocaleTimeString());
      } else {
        throw new Error('Erro ao carregar dados do dashboard');
      }
    } catch (err) {
      console.error('Erro:', err);
      setError(err.response?.data?.detail || 
              'Não foi possível carregar os dados. Verifique sua conexão.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const renderProgressChart = () => {
    if (progressData.length === 0) {
      return <div className="empty-state">Nenhum dado de progresso disponível</div>;
    }

    return (
      <div className="progress-grid">
        {progressData.map((item) => (
          <div key={item.id} className="progress-card">
            <div className="progress-header">
              <FaBook className="progress-icon" />
              <h3>{item.course_name}</h3>
            </div>
            <div className="progress-bar-container">
              <div 
                className="progress-bar"
                style={{ width: `${item.progress_percentage}%` }}
              >
                <span>{item.progress_percentage}%</span>
              </div>
            </div>
            <div className="progress-meta">
              <span>Último estudo: {item.last_studied || 'N/A'}</span>
            </div>
          </div>
        ))}
      </div>
    );
  };

  if (loading) {
    return (
      <div className="dashboard-loading">
        <div className="spinner"></div>
        <p>Carregando seu dashboard...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="dashboard-error">
        <FaExclamationTriangle className="error-icon" />
        <h3>Ocorreu um erro</h3>
        <p>{error}</p>
        <button 
          onClick={fetchDashboardData}
          className="retry-button"
        >
          <FaSync /> Tentar novamente
        </button>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1><FaChartLine /> Meu Dashboard</h1>
        <div className="last-updated">
          <FaCalendarAlt /> Atualizado em: {lastUpdated}
        </div>
      </header>

      <section className="dashboard-section">
        <h2>Seu Progresso</h2>
        {renderProgressChart()}
      </section>

      <section className="dashboard-section">
        <h2>Plano de Estudos</h2>
        <div className="study-plan">
          {studyPlan ? (
            <ul className="plan-items">
              {studyPlan.split('\n').map((item, index) => (
                item.trim() && <li key={index}>{item}</li>
              ))}
            </ul>
          ) : (
            <p className="empty-plan">Seu plano de estudos será gerado em breve.</p>
          )}
        </div>
      </section>

      <div className="dashboard-actions">
        <button 
          onClick={fetchDashboardData}
          className="refresh-button"
        >
          <FaSync /> Atualizar Dados
        </button>
      </div>
    </div>
  );
};

export default Dashboard;