<template>
    <div>
        <div class="tops">
            <h1>It's A Database</h1>
            <h2>A Social Engineering Database</h2>
            <search></search>
        </div>
        <Analysis></Analysis>
    </div>
</template>

<script>
    import search from './components/search.vue'
    import Analysis from './components/Analysis.vue'
    // axios.defaults.baseURL = 'http://localhost:5000/api';
    axios.defaults.baseURL = 'http://123.207.89.91:5000/api';
    export default {
        components: {
            search,
            Analysis
        }
    }
</script>

<style>
#main {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fff;
  margin: 2em auto;
  width: 50em; 
  border: 1px solid #ccc;
  padding: 1.5em; 
  background: white;
}
.tops {
    position: relative;
    text-align: center;
    background-color: #27ae60;
    color: #fff;
    margin-bottom: 0;
    padding-bottom: 50px;
    padding-top: 20px;
    line-height: 20px;
}
h1 {
    line-height: 1;
    letter-spacing: -2px;
    font-weight: 700;
    font-size: 4em;
    text-align: center;
    text-shadow: 0 1px 3px rgba(0,0,0,.4), 0 0 30px rgba(0,0,0,.075);
}
h2 {
    font-size: 2em;
}

</style>
