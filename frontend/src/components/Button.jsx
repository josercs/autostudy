import React from 'react';

const Button = ({ type, color, size, children, onClick }) => {
  const className = `btn btn-${color} btn-${size} ${type ? `btn-${type}` : ''}`;
  
  return (
    <button className={className} onClick={onClick}>
      {children}
    </button>
  );
};

export default Button;
