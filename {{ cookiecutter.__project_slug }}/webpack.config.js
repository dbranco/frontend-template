const prod = process.env.NODE_ENV === 'production';

const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: "development",
{%- if cookiecutter.flavor == "javascript" -%}
  entry: "/src/index.jsx",
{%- elif cookiecutter.flavor == "typescript" -%}
entry: "/src/index.tsx",
{% endif %}
  output: {
    path: __dirname + '/dist/',
    publicPath: "/",
  },
  module: {
    rules: [
    {%- if cookiecutter.flavor == "javascript" -%}
      {
        test: /\.js|\.jsx$/,
        exclude: /node_modules/,
        resolve: {
          extensions: ['.js', '.jsx', '.json'],
        },
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react"],
          },
        },
      },
    {%- elif cookiecutter.flavor == "typescript" -%}
      {
        test: /\.(ts|tsx)$/,
        exclude: /node_modules/,
        resolve: {
          extensions: ['.ts', '.tsx', '.js', '.json'],
        },
        use: 'ts-loader',
      },
    {% endif %}
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ],
  },
  devtool: prod ? undefined : 'source-map',
  plugins: [
    new HtmlWebpackPlugin({
      template: 'index.html',
    }),
    new MiniCssExtractPlugin(),
  ],
};
