<template>
  <div class="Search">
    <h1>A Database</h1>
    <select v-model="selected">
        <option v-for="option in options" v-bind:value="option.value">
            {{ option.text }}
        </option>
    </select>
    <input
        placeholder="请输入并按下回车进行搜索"
        type="text"
        class="searchInput" 
        v-model="searchStr"
        v-on:keyup.enter="search"
    />
    <h2 v-show="errorinfo">暂无数据，请重新输入</h2>
    <div class="container" v-show="retItems.length">
        <h2>返回数据如下:</h2>
        <table style="table-layout:fixed">
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
  name: 'Search',
  data () {
    return {
      selected: 'user',
      searchStr: '',
      errorinfo: '',
      options: [
        { text: '用户名', value: 'user' },
        { text: '密码', value: 'pwd' },
        { text: '邮箱', value: 'email' },
        { text: '哈希密码', value: 'pwdHash' }        
      ],
      retItems: [],
      analysisInfos: [],
    }
  },
  methods:{
        search: function () {
            this.errorinfo = '';
            axios.get('/find/'+ this.selected + '/' + this.searchStr)
                .then(response => {
                    if(response.data.status === 'ok'){
                        this.retItems = response.data.data.concat();
                        this.searchStr = '';
                    }
                    else{
                        this.retItems = [];
                        this.searchStr = [];
                        this.errorinfo = '输入错误';
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }
}
</script>

<style lang="scss">

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

table{
    border:1px solid #000; 
    border-collapse:collapse; 
    font-family:Arial; 
} 

.container {
  text-align: center;
  overflow: hidden;
  width: 800px;
  margin: 0 auto;
}

.container table {
  width: 100%;
}

.container td, .container th {
  overflow: auto;
  padding: 10px;
}

.container th {
  border-bottom: 1px solid #ddd;
  position: relative;
  width: 30px;
}

</style>
