/**
 * Header component
 */

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store';
import Button from './Button';

const Header: React.FC = () => {
  const navigate = useNavigate();
  const { isAuthenticated, logout } = useAuthStore();

  return (
    <header className="bg-black text-white sticky top-0 z-50 shadow-md">
      <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">
          💼 JobHub
        </Link>

        <nav className="hidden md:flex gap-6 items-center">
          <Link to="/jobs" className="hover:text-orange-600 transition">
            Jobs
          </Link>
          {isAuthenticated ? (
            <>
              <Link to="/profile" className="hover:text-orange-600 transition">
                Profile
              </Link>
              <Button
                variant="secondary"
                size="sm"
                onClick={() => {
                  logout();
                  navigate('/');
                }}
              >
                Logout
              </Button>
            </>
          ) : (
            <>
              <Link to="/login">
                <Button variant="secondary" size="sm">
                  Login
                </Button>
              </Link>
              <Link to="/register">
                <Button variant="accent" size="sm">
                  Sign Up
                </Button>
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Header;
