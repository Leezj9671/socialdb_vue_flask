<template>
  <div class="app">
    <h1>A Database</h1>
    <h2>搜索信息:</h2>
    <select v-model="selected">
        <option v-for="option in options" v-bind:value="option.value">
            {{ option.text }}
        </option>
    </select>
    <input
        placeholder="请输入相关信息,输入回车键进行搜索"
        type="text"
        class="searchInput" 
        v-model="searchStr"
        v-on:keyup.enter="search"
    />
    <div class="dataform">
        <h2 v-show="retItems.length">输入数据如下:</h2>
        <table>
            <thead>
            <tr>
                <th>用户名</th>
                <th>邮箱</th>
                <th>密码</th>
                <th>hash密码</th>
                <th>来源</th>
                <th>泄漏时间</th>
            </tr>
            </thead>
            <tbody>
                <tr v-for="item in retItems">
                    <td>{{ item.user}}</td>
                    <td>{{ item.email}}</td>
                    <td>{{ item.password}}</td>
                    <td>{{ item.passwordHash}}</td>
                    <td>{{ item.source}}</td>
                    <td>{{ item.xtime }}</td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://123.207.89.91:5000/api';

export default {
  name: 'app',
  data () {
    return {
      selected: 'user',
      searchStr: '',
      options: [
        { text: '用户名', value: 'user' },
        { text: '密码', value: 'password' },
        { text: '邮箱', value: 'email' }
      ],
      retItems: [],
      analysisInfos: [],
    }
  },
  methods:{
        search: function () {
            axios.get('/find/'+ this.selected + '/' + this.searchStr)
                .then(response => {
                    console.log(this.searchStr)
                    if(response.data.status === 'ok'){
                        this.retItems = response.data.data.concat();
                        this.searchStr = ''
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        flashAnalysis(){
            console.log("analysis")
        }
    }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 2em auto;
  width: 50em; 
  border: 1px solid #ccc;
  padding: 1.5em; 
  background: white;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

table{
    border:1px solid #000; 
    border-collapse:collapse; 
    font-family:Arial; 
} 

table caption{       /*����*/ 
    text-align:middle; 
    width:700px;
    padding-bottom:6px; 
} 

table th{           /*���б���*/ 
    border:1px solid #000; 
    background-color:#E2E2E2; 
    color:#000000; 
    text-align:left; 
    font-weight:normal; 
    padding:2px 8px 2px 6px; 
    margin:0px; 
} 
table td{
    border:1px solid #000;   /* ��Ԫ���߿� */ 
}
table th, td {
 min-width: 0.1em;
 padding: 10px 20px;
}
table input{          /*������������ʽ*/ 
    width:100px;
    padding:1px 3px 1px 3px; 
    margin:0px; 
    border:none;                /* ��������Ҫ�߿� */ 
    font-family:Arial; 
}
</style>
