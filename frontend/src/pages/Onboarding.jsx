import React, { useState } from 'react';
import Button from '../components/Button';

const Onboarding = () => {
  const [step, setStep] = useState(1);
  const totalSteps = 3;

  const nextStep = () => {
    if (step < totalSteps) setStep(step + 1);
  };

  return (
    <div className="container mt-5">
      <h2>Bem-vindo ao {step === 1 ? 'Começo da Jornada' : 'Seu Progresso'}</h2>
      <p>{step === 1 ? 'Primeiro, vamos entender seus objetivos.' : 'Agora, vamos configurar seu painel!'}</p>
      <Button color="primary" size="lg" onClick={nextStep}>Próximo</Button>
      <p className="mt-2">Etapa {step} de {totalSteps}</p>
    </div>
  );
};

export default Onboarding;
