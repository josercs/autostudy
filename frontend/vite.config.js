import { defineConfig } from 'vite';
import path from 'path';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@assets': path.resolve(__dirname, './src/assets'),
      '@utils': path.resolve(__dirname, './src/utils'), 
      '@auth': path.resolve(__dirname, './src/auth'),
    }
  },
  css: {
    devSourcemap: true, // Para melhor debugging do CSS
    modules: {
      localsConvention: 'camelCase' // Converte classes para camelCase
    }
  },
  server: {
    port: 5173,
    open: true // Abre o navegador automaticamente
  }
});