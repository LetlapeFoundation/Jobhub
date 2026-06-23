/**
 * Reusable Button component
 */

import React from 'react';
import clsx from 'clsx';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'accent' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  children: React.ReactNode;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', loading = false, className, ...props }, ref) => {
    const baseClass = 'font-medium rounded-lg transition-colors duration-200';

    const variantClass = {
      primary: 'bg-black text-white hover:bg-gray-800',
      secondary: 'bg-gray-200 text-black hover:bg-gray-300',
      accent: 'bg-orange-600 text-white hover:bg-orange-700',
      danger: 'bg-red-600 text-white hover:bg-red-700',
    }[variant];

    const sizeClass = {
      sm: 'px-3 py-1 text-sm',
      md: 'px-4 py-2 text-base',
      lg: 'px-6 py-3 text-lg',
    }[size];

    const disabledClass = props.disabled ? 'opacity-50 cursor-not-allowed' : '';

    return (
      <button
        ref={ref}
        className={clsx(baseClass, variantClass, sizeClass, disabledClass, className)}
        disabled={loading || props.disabled}
        {...props}
      >
        {loading ? '⏳ Loading...' : props.children}
      </button>
    );
  }
);

Button.displayName = 'Button';

export default Button;
