/**
 * Job detail page
 */

import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import Header from '../components/Header';
import Button from '../components/Button';
import { jobService } from '../services/jobService';
import { MapPin, Briefcase, DollarSign, Calendar } from 'lucide-react';
import { formatSalary, formatDate } from '../utils/format';

const JobDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const { data: job, isLoading, error } = useQuery({
    queryKey: ['job', id],
    queryFn: () => jobService.getJob(id!),
    enabled: !!id,
  });

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header />
        <div className="container mx-auto px-4 py-12 text-center">
          Loading...
        </div>
      </div>
    );
  }

  if (error || !job) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header />
        <div className="container mx-auto px-4 py-12 text-center">
          <p className="text-red-500">Job not found</p>
          <Button onClick={() => navigate('/jobs')} className="mt-4">
            Back to Jobs
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />

      <div className="container mx-auto px-4 py-8">
        <Button variant="secondary" onClick={() => navigate('/jobs')} className="mb-6">
          ← Back to Jobs
        </Button>

        <div className="grid md:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="md:col-span-2">
            <div className="bg-white rounded-lg p-8 shadow-sm">
              <h1 className="text-4xl font-bold mb-2">{job.title}</h1>
              <p className="text-gray-600 mb-6">Job ID: {job.id}</p>

              <div className="grid grid-cols-2 gap-4 mb-8 pb-8 border-b">
                <div className="flex items-center gap-2">
                  <Briefcase className="text-orange-600" />
                  <span>{job.job_type}</span>
                </div>
                <div className="flex items-center gap-2">
                  <MapPin className="text-orange-600" />
                  <span>{job.work_location}</span>
                </div>
                <div className="flex items-center gap-2 text-green-600 font-semibold">
                  <DollarSign className="text-green-600" />
                  <span>{formatSalary(job.salary_min)} - {formatSalary(job.salary_max)}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Calendar className="text-orange-600" />
                  <span>Due: {formatDate(job.application_deadline)}</span>
                </div>
              </div>

              <div>
                <h2 className="text-2xl font-bold mb-4">About This Role</h2>
                <p className="text-gray-700 whitespace-pre-wrap mb-6">{job.description}</p>
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div>
            <div className="bg-white rounded-lg p-6 shadow-sm sticky top-20">
              <h3 className="text-lg font-bold mb-4">Apply Now</h3>
              <Button variant="accent" className="w-full mb-3">
                Submit Application
              </Button>
              <Button variant="secondary" className="w-full">
                Save Job
              </Button>
              <hr className="my-4" />
              <div className="text-sm text-gray-600">
                <p className="mb-2">
                  <strong>{job.total_applications}</strong> people have applied
                </p>
                <p>
                  Posted on <strong>{formatDate(job.created_at)}</strong>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobDetail;
