/**
 * Global state management with Zustand
 */

import { create } from 'zustand';
import { User } from '../services/authService';

interface AuthStore {
  user: User | null;
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  setAuthenticated: (isAuthenticated: boolean) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  isAuthenticated: false,
  setUser: (user) => set({ user, isAuthenticated: !!user }),
  setAuthenticated: (isAuthenticated) => set({ isAuthenticated }),
  logout: () => set({ user: null, isAuthenticated: false }),
}));

interface JobFilters {
  search?: string;
  location?: string;
  job_type?: string;
  salary_min?: number;
  salary_max?: number;
  skip?: number;
  limit?: number;
}

interface JobStore {
  filters: JobFilters;
  setFilters: (filters: JobFilters) => void;
  clearFilters: () => void;
}

export const useJobStore = create<JobStore>((set) => ({
  filters: {},
  setFilters: (filters) => set({ filters }),
  clearFilters: () => set({ filters: {} }),
}));
