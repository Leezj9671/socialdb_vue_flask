<template>
    <div class="analysis">
        <h2>Database Analysis</h2>
        <div class="button-group">
            <button v-for="key in analysisItems" v-bind:value="key.value" @click="flashAnalysis(key.value, key.text)" type="button" class="button button-pill button-action">
                {{ key.text}}
            </button>
        </div>
        <div id="chartArea" style="margin: 0 auto; width: 700px; height:400px;"></div>
    </div>
</template>


<script>
// 改为CDN引入
// import axios from 'axios'
// var echarts = require('echarts/lib/echarts');
// require('echarts/lib/chart/pie')
// require('echarts/lib/component/tooltip');

var myChart = null;

export default {
  name:'analysis',
  data () {
    return {
        analysisData: [],
        legendData: [],
        analysisItems: [
            {text: '来源', value: 'source'},
            {text: '泄露时间', value: 'xtime'},
            {text: '邮箱后缀', value: 'suffix_email'},
            {text: '导入时间', value: 'create_time'}
        ]
    }
  },
  methods:{
    flashAnalysis: function (value, vtext) {
        myChart.showLoading({
            text: "数据获取ing...",
        });
        axios.get('/analysis/'+value).then(response => {
            if(response.data.status === 'ok'){
                this.analysisData = [];
                this.legendData = [];
                for (var key in response.data.data) {   
                    var item = response.data.data[key];
                    this.analysisData.push({
                        "value": item["sum"],
                        "name": item["_id"]
                    });
                    this.legendData.push(item["_id"]);
                }
                myChart.hideLoading();
                myChart.setOption({
                    title: {
                        text: vtext,
                        x: 'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: this.legendData
                    },
                    series: {
                        name: vtext,
                        type: 'pie',
                        data: this.analysisData
                    }
                });
            }
        })
        .catch(error => { console.log(error); })
        }
    },
    mounted(){
        myChart = echarts.init(document.getElementById('chartArea'));
    }
}
</script>

<style>
@import url(http://www.bootcss.com/p/buttons/css/buttons.css);
.analysis {
    text-align: center;
}
.button-action {
    background-color: #339966;
    border-color: #339966;
}
.button-action:hover, focus {
    background-color: #339999;
    border-color: #339999;
}
</style>
