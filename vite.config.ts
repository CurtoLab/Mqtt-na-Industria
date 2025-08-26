import { defineConfig } from 'vite'

export default defineConfig({
    build: {
        sourcemap: false
    },
    optimizeDeps: {
        exclude: ['monaco-editor']
    },
    define: {
        global: 'globalThis'
    }
})
