/**
 * 404 Not Found page
 */

import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../components/Header';
import Button from '../components/Button';

const NotFound: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <div className="container mx-auto px-4 py-12 text-center">
        <h1 className="text-6xl font-bold text-gray-900 mb-4">404</h1>
        <p className="text-2xl text-gray-600 mb-8">Page not found</p>
        <Link to="/">
          <Button variant="primary">Go Home</Button>
        </Link>
      </div>
    </div>
  );
};

export default NotFound;
