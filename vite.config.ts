import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    fs: {
      // Slidev 52.16+ import guard incorrectly resolves root-relative
      // /img/... paths as C:\img\... on Windows. Disabling strict mode
      // prevents the false-positive errors on public/ assets.
      strict: false,
    },
  },
})
