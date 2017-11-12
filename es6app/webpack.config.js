let path = require('path'),
  HtmlWebpackPlugin = require('html-webpack-plugin'),
  ExtractTextPlugin = require('extract-text-webpack-plugin'),
  CopyWebpackPlugin = require('copy-webpack-plugin');

//define sass extract
const extractSass = new ExtractTextPlugin({
  filename: 'index.css',
  disable: false,
  allChunks: true
});

module.exports = {
  //source-map houd bij waar de code vandaankomt na het samenvoegen van alle code.
  devtool: "source-map",
  // Bundel alles waarnaar word verwezen in de entry file.
  entry: {
    app: './src/index.js',
    css: './src/styles/main.scss'
  },
  //Output is de file waar de gebundelde code wordt neergezet.
  output: {
    //dirname is waar de webpack.config.js file staat. 
    //dist is de folder waar de code in werd geplaatst
    path: path.resolve(__dirname, "dist"),
    filename: '[name].js', // name is de naam die je bij entry hebt gegeven.
  },
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader'
      }
    },{
      test: /\.scss$/,
      //with sourceMaps no file extraction 
      use: [{
        loader: 'style-loader'
        },{
        loader: 'css-loader',
          options: {
            sourceMap: true
          }
        },{
        loader: 'sass-loader',
          options: {
            sourceMap: true
          }
        }
      ]
    }]
  },
  plugins: [
    new HtmlWebpackPlugin({
      //filename:'../index.html',
      template: './src/index.html'
    }),
    /*
      new ExtractTextPlugin({
          filename:"css/index.css",
          disable:false,
          allChunks:true
      })*/
    extractSass,
    new CopyWebpackPlugin([
      // Copy directory contents to {output}/
      {
        from: 'src/img'
      },
    ])
  ],
  devServer: {
    contentBase: path.join(__dirname, "src"),
    //compress: true,
    port: 8080,
    stats: 'minimal',
    //open new window in browser
    open: false
  }
}