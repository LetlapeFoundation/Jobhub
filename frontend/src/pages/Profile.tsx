/**
 * Profile page (placeholder)
 */

import React from 'react';
import Header from '../components/Header';
import Button from '../components/Button';

const Profile: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <div className="container mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold mb-6">My Profile</h1>
        <div className="card p-8">
          <p className="text-gray-600">Profile feature coming soon...</p>
          <Button className="mt-4">Edit Profile</Button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
