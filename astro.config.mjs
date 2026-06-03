// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://medivora.onrender.com',
  trailingSlash: 'ignore',
  build: {
    inlineStylesheets: 'auto',
    // Compress HTML output
    assets: '_assets',
  },
  // Prefetch all links by default for snappy navigation
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  integrations: [
    sitemap({
      changefreq: 'monthly',
      priority: 0.8,
      lastmod: new Date(),
      // Mark key pages as higher priority
      customPages: [
        'https://medivora.onrender.com/',
        'https://medivora.onrender.com/foundations',
        'https://medivora.onrender.com/safety-pipeline',
        'https://medivora.onrender.com/case-studies',
      ],
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
    build: {
      // Split CSS per-page for smaller payloads
      cssCodeSplit: true,
      rollupOptions: {
        output: {
          // Keep chunk names human-readable for debugging
          manualChunks: undefined,
        },
      },
    },
  },
});
