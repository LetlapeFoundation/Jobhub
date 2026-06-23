/**
 * Register page
 */

import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import Header from '../components/Header';
import Button from '../components/Button';
import toast from 'react-hot-toast';

const Register: React.FC = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    user_type: 'job_seeker',
  });
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // TODO: Call auth service
      toast.success('Account created! Please login.');
      navigate('/login');
    } catch (error) {
      toast.error('Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-md mx-auto bg-white rounded-lg p-8 shadow">
          <h1 className="text-2xl font-bold mb-6 text-center">Create Account</h1>
          <form onSubmit={handleSubmit} className="space-y-4">
            <select
              name="user_type"
              value={formData.user_type}
              onChange={handleChange}
              className="input"
            >
              <option value="job_seeker">Job Seeker</option>
              <option value="employer">Employer</option>
              <option value="recruiter">Recruiter</option>
              <option value="entrepreneur">Entrepreneur</option>
            </select>
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
              className="input"
              required
            />
            <input
              type="password"
              name="password"
              placeholder="Password (min 8 characters)"
              value={formData.password}
              onChange={handleChange}
              className="input"
              required
              minLength={8}
            />
            <Button variant="primary" type="submit" className="w-full" loading={loading}>
              Create Account
            </Button>
          </form>
          <p className="text-center text-gray-600 mt-4 text-sm">
            By signing up, you agree to our Terms of Service and Privacy Policy.
          </p>
          <p className="text-center text-gray-600 mt-4">
            Already have an account?{' '}
            <Link to="/login" className="text-orange-600 hover:underline">
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;
