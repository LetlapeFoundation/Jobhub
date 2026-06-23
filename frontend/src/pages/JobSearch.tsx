/**
 * Job search page
 */

import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import Header from '../components/Header';
import JobCard from '../components/JobCard';
import Button from '../components/Button';
import { jobService } from '../services/jobService';
import { Search, Filter } from 'lucide-react';

const JobSearch: React.FC = () => {
  const [search, setSearch] = useState('');
  const [skip, setSkip] = useState(0);
  const limit = 20;

  const { data: jobs, isLoading, error } = useQuery({
    queryKey: ['jobs', skip, search],
    queryFn: () => jobService.getJobs({ search, skip, limit }),
  });

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />

      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-6">Find Jobs</h1>

        {/* Search Bar */}
        <div className="mb-8 flex gap-2">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-3 text-gray-400" size={20} />
            <input
              type="text"
              placeholder="Search jobs, skills, companies..."
              value={search}
              onChange={(e) => {
                setSearch(e.target.value);
                setSkip(0);
              }}
              className="input pl-10"
            />
          </div>
          <Button variant="secondary" className="flex items-center gap-2">
            <Filter size={20} />
            Filters
          </Button>
        </div>

        {/* Job Listings */}
        {isLoading ? (
          <div className="text-center py-12">
            <p className="text-gray-500">Loading jobs...</p>
          </div>
        ) : error ? (
          <div className="text-center py-12">
            <p className="text-red-500">Error loading jobs</p>
          </div>
        ) : !jobs || jobs.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500">No jobs found</p>
          </div>
        ) : (
          <>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
              {jobs.map((job) => (
                <JobCard key={job.id} job={job} />
              ))}
            </div>

            {/* Pagination */}
            <div className="flex justify-center gap-4">
              <Button
                variant="secondary"
                onClick={() => setSkip(Math.max(0, skip - limit))}
                disabled={skip === 0}
              >
                Previous
              </Button>
              <span className="flex items-center text-gray-600">
                Page {Math.floor(skip / limit) + 1}
              </span>
              <Button
                variant="secondary"
                onClick={() => setSkip(skip + limit)}
                disabled={!jobs || jobs.length < limit}
              >
                Next
              </Button>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default JobSearch;
