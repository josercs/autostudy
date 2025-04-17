// src/components/auth/RequireAuth.jsx
import { useAuth } from "../../contexts/AuthContext";
import { Navigate, Outlet } from "react-router-dom";

export default function RequireAuth({ redirectTo = '/login', requireOnboarding = false }) {
  const { user, loading, onboardingCompleto } = useAuth();

  if (loading) return <div>Carregando...</div>;

  if (!user) return <Navigate to={redirectTo} replace />;

  if (requireOnboarding && !onboardingCompleto) {
    return <Navigate to="/onboarding" replace />;
  }

  return <Outlet />;
}

// src/components/auth/RequireAuth.jsx