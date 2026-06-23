/**
 * JobCard component for displaying job listings
 */

import React from 'react';
import { Link } from 'react-router-dom';
import { MapPin, Briefcase, DollarSign } from 'lucide-react';
import { formatSalary } from '../utils/format';
import { Job } from '../services/jobService';

interface JobCardProps {
  job: Job;
}

const JobCard: React.FC<JobCardProps> = ({ job }) => {
  return (
    <Link to={`/jobs/${job.id}`}>
      <div className="card hover:shadow-lg">
        <div className="flex justify-between items-start mb-2">
          <div className="flex-1">
            <h3 className="text-lg font-bold text-black">{job.title}</h3>
            <p className="text-sm text-gray-600">Job ID: {job.id.slice(0, 8)}</p>
          </div>
          <span className="badge badge-verified text-xs">Verified</span>
        </div>

        <p className="text-gray-700 text-sm mb-3 line-clamp-2">{job.description}</p>

        <div className="grid grid-cols-2 gap-2 mb-3 text-sm">
          <div className="flex items-center gap-1 text-gray-600">
            <Briefcase size={16} />
            <span>{job.job_type}</span>
          </div>
          <div className="flex items-center gap-1 text-gray-600">
            <MapPin size={16} />
            <span>{job.work_location}</span>
          </div>
          <div className="flex items-center gap-1 text-green-600 font-semibold col-span-2">
            <DollarSign size={16} />
            <span>
              {formatSalary(job.salary_min)} - {formatSalary(job.salary_max)}
            </span>
          </div>
        </div>

        <div className="flex justify-between items-center text-xs text-gray-500">
          <span>{job.total_applications} applications</span>
          <span>Posted {new Date(job.created_at).toLocaleDateString()}</span>
        </div>
      </div>
    </Link>
  );
};

export default JobCard;
