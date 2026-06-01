import eslintPluginAstro from 'eslint-plugin-astro';

export default [
  ...eslintPluginAstro.configs.recommended,
  {
    ignores: [
      'dist/**',
      '.astro/**',
      'node_modules/**',
      '.venv/**',
      'docs/reference/**',
    ],
  },
  {
    rules: {
      'no-unused-vars': 'warn',
    },
  },
];
