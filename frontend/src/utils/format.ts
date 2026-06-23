/**
 * Utility functions
 */

export const formatSalary = (amount: number): string => {
  return new Intl.NumberFormat('en-ZA', {
    style: 'currency',
    currency: 'ZAR',
    minimumFractionDigits: 0,
  }).format(amount);
};

export const formatDate = (date: string | Date): string => {
  return new Intl.DateTimeFormat('en-ZA').format(new Date(date));
};

export const truncate = (text: string, length: number): string => {
  return text.length > length ? `${text.substring(0, length)}...` : text;
};
