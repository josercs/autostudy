import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { AuthProvider } from "./contexts/AuthContext";
import './index.css';
import './styles/main.scss';
import 'bootstrap/dist/css/bootstrap.min.css';

// Solução para o erro de message channel
if (typeof window !== 'undefined' && window.BroadcastChannel) {
  window.BroadcastChannel.prototype.postMessage = function(data) {
    try {
      if (!this._closed) {
        this.dispatchEvent(new MessageEvent('message', { data }));
      }
    } catch (e) {
      console.warn('BroadcastChannel postMessage failed:', e);
    }
  };
}
// Limpeza de service workers
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(registrations => {
    registrations.forEach(registration => registration.unregister());
  });
}

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);