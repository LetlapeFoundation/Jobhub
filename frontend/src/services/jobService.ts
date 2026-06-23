/**
 * Job-related API calls
 */

import apiClient from './api';

export interface Job {
  id: string;
  employer_id: string;
  title: string;
  description: string;
  job_type: string;
  work_location: string;
  salary_min: number;
  salary_max: number;
  status: string;
  total_applications: number;
  application_deadline: string;
  created_at: string;
}

export const jobService = {
  // Get all jobs with filters and pagination
  getJobs: async (params?: Record<string, any>) => {
    const response = await apiClient.get<Job[]>('/jobs', { params });
    return response.data;
  },

  // Get single job details
  getJob: async (jobId: string) => {
    const response = await apiClient.get<Job>(`/jobs/${jobId}`);
    return response.data;
  },

  // Create job posting (employer only)
  createJob: async (data: Partial<Job>) => {
    const response = await apiClient.post<Job>('/jobs', data);
    return response.data;
  },

  // Update job posting
  updateJob: async (jobId: string, data: Partial<Job>) => {
    const response = await apiClient.put<Job>(`/jobs/${jobId}`, data);
    return response.data;
  },

  // Close/archive job
  closeJob: async (jobId: string) => {
    const response = await apiClient.put(`/jobs/${jobId}`, { status: 'closed' });
    return response.data;
  },
};
