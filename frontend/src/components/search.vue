<template>
  <div class="Search">
    <select v-model="selected" class="Select">
        <option v-for="option in options" v-bind:value="option.value" class="options">
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
        <table>
            <thead>
            <tr>
                <th>用户名</th>
                <th>邮箱</th>
                <th>来源</th>
                <th>泄漏时间</th>
                <th>密码</th>
                <th>hash密码</th>
            </tr>
            </thead>
            <tbody>
                <tr v-for="item in retItems">
                    <td>{{ item.user}}</td>
                    <td>{{ item.email}}</td>
                    <td>{{ item.source}}</td>
                    <td>{{ item.xtime }}</td>
                    <td>{{ item.password}}</td>
                    <td>{{ item.passwordHash}}</td>
                </tr>
            </tbody>
        </table>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Search',
  data () {
    return {
      selected: 'user',
      searchStr: '',
      errorinfo: '',
      options: [
        { text: '用户名', value: 'user' },
        { text: '密码', value: 'password' },
        { text: '邮箱', value: 'email' },
        { text: '哈希密码', value: 'passwordHash' }        
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

<style>

h1, h2 {
  font-weight: normal;
}

h1 {
  color: #fff;
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
    margin-top: 2em;
    border:1px solid none;
    padding: 20px;
    border-collapse: collapse;
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
} 

.container {
  text-align: center;
  overflow: hidden;
  width: 60em;
  margin: 0 auto;
}

.container table {
  width: 100%;
}

.container td {
    font-size: 10px;
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
.searchInput {
    outline: none;
    height: 30px;
    width: 680px;
    border : 1px solid  #FFFFFF;
    padding : 15px 30px 15px 30px;
    font-size: 1em;
    font-family: BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
.searchInput:focus {
    box-shadow: 2px 2px 2px #336633;
}
.Select {
    height: 62px;
    width: 100px;
    border : 1px solid  #FFFFFF;
    font-size: 1em;
    font-family: BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
    outline: none;
    border: none;
    padding: 0 0 0 10px;
}
.Select .options {
    outline: none;
    border: none;
}
</style>
