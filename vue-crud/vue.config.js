const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      '^/api': {
        target: '',
        changeOrigin: true,
        logLevel: 'debug',
        pathRewrite: {'^/api': '/'},
      }
    }
  }
})
