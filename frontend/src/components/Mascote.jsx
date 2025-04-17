import React, { forwardRef } from 'react';
import Lottie from 'lottie-react';

const Mascote = forwardRef(({ animationData, size = '180px' }, ref) => {
  // Verificação robusta da animação
  if (!animationData?.layers?.length) {
    return (
      <div style={{
        width: size,
        height: size,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#f0f0f0',
        borderRadius: '50%',
        border: '2px dashed #ccc',
        color: '#666'
      }}>
        Animação inválida
      </div>
    );
  }

  return (
    <div style={{ 
      width: size, 
      height: size,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      <Lottie
        lottieRef={ref}
        animationData={animationData}
        loop={false}
        autoplay={true}
        rendererSettings={{
          preserveAspectRatio: 'xMidYMid meet'
        }}
      />
    </div>
  );
});

export default Mascote;