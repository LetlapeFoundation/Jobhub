/**
 * PWA (Progressive Web App) utilities
 */

import { Workbox } from 'workbox-window';
import toast from 'react-hot-toast';

export function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    const wb = new Workbox('/sw.js');

    wb.addEventListener('installed', () => {
      console.log('✅ Service Worker installed');
    });

    wb.addEventListener('controlling', () => {
      console.log('✅ Service Worker is now controlling the page');
      toast.success('App updated! Refresh to see changes.');
    });

    wb.addEventListener('externalwaiting', () => {
      console.log('⚠️ New Service Worker waiting');
    });

    wb.register().catch((err) => {
      console.error('❌ Service Worker registration failed:', err);
    });
  }
}
