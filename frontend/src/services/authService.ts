/**
 * User authentication service
 */

import apiClient from './api';

export interface User {
  id: string;
  email: string;
  user_type: string;
  verification_status: string;
  is_active: boolean;
  created_at: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  password: string;
  user_type: string;
  phone?: string;
}

export const authService = {
  // Register new user
  register: async (data: RegisterData) => {
    const response = await apiClient.post<User>('/users/register', data);
    return response.data;
  },

  // Login
  login: async (credentials: LoginCredentials) => {
    const response = await apiClient.post<{ access_token: string; token_type: string }>(
      '/users/login',
      credentials
    );
    if (response.data.access_token) {
      localStorage.setItem('access_token', response.data.access_token);
    }
    return response.data;
  },

  // Get current user
  getCurrentUser: async () => {
    const response = await apiClient.get<User>('/users/me');
    return response.data;
  },

  // Logout
  logout: () => {
    localStorage.removeItem('access_token');
    window.location.href = '/login';
  },
};
