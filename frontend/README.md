# Frontend

> A frontend used by vue.js 

## Build Setup

``` bash
# install Node.js from https://nodejs.org/en/download/
# install vue-cli
npm install -g vue-cli

# if npm is too slowly, you can install cnpm to replace npm
npm install -g cnpm --registry=https://registry.npm.taobao.org

# install dependencies
npm install
# Because of using CDN, now you can ignore it.
# Or you can using command below in development mode. Decide on you.
# But you must to change some import setence in *.vue
~~npm install axios~~
~~npm install echarts~~

# serve with hot reload at localhost:8080
npm run dev
```

## Modify IP address
- App.vue => axios.defaults.baseURL='[backend IP]'
For detailed explanation on how these things work, please connect to leezj9671@gmail.com or commit an issue. :>