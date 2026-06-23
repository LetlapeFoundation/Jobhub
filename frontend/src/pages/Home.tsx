/**
 * Home page
 */

import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/Header';
import Button from '../components/Button';
import { Briefcase, TrendingUp, Shield } from 'lucide-react';

const Home: React.FC = () => {
  return (
    <div className="min-h-screen bg-white">
      <Header />

      {/* Hero Section */}
      <section className="bg-black text-white py-20 px-4">
        <div className="container mx-auto text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Find Your Next Opportunity
          </h1>
          <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
            JobHub connects talented South Africans with verified employers, funding, and growth
            capital. Built for Africa, by Africans.
          </p>
          <div className="flex gap-4 justify-center">
            <Link to="/jobs">
              <Button variant="accent" size="lg">
                Browse Jobs
              </Button>
            </Link>
            <Link to="/register">
              <Button variant="secondary" size="lg">
                Get Started
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16 px-4">
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Why JobHub?</h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="card">
              <Briefcase className="text-orange-600 mb-4" size={32} />
              <h3 className="text-xl font-bold mb-2">Real Jobs Only</h3>
              <p className="text-gray-600">
                Every employer verified via CIPC. No scams. No ghost postings.
              </p>
            </div>
            <div className="card">
              <Shield className="text-orange-600 mb-4" size={32} />
              <h3 className="text-xl font-bold mb-2">Your Data, Your Rules</h3>
              <p className="text-gray-600">
                Data sovereignty. All PII stored on South African servers.
              </p>
            </div>
            <div className="card">
              <TrendingUp className="text-orange-600 mb-4" size={32} />
              <h3 className="text-xl font-bold mb-2">Fair Matching</h3>
              <p className="text-gray-600">
                Algorithms audited for bias. Your experience counts.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-orange-600 text-white py-12 px-4">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Get Started?</h2>
          <Link to="/register">
            <Button variant="secondary" size="lg">
              Create Your Profile
            </Button>
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-8 px-4">
        <div className="container mx-auto text-center text-sm">
          <p>&copy; 2026 JobHub. South African Employment Platform.</p>
          <p className="mt-2">Build the plane while flying it. 🚀</p>
        </div>
      </footer>
    </div>
  );
};

export default Home;
