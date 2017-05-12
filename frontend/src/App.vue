<template>
    <div>
        <search></search>
        <Analysis></Analysis>
    </div>
</template>

<script>
    import search from './components/search.vue'
    import Analysis from './components/Analysis.vue'

    export default {
        components: {
            search,
            Analysis
        }
    }
</script>

<style lang="scss">
#main {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 2em auto;
  width: 50em; 
  border: 1px solid #ccc;
  padding: 1.5em; 
  background: white;
}
</style>
