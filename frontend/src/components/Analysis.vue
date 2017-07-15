<template>
    <div class="analysis">
        <h2>Database Analysis</h2>
        <div class="button-group">
            <button v-for="key in analysisItems" v-bind:value="key.value" @click="flashAnalysis(key.value)" type="button" class="button button-pill button-action">
                {{ key.text}}
            </button>
        </div>
        <div id="chartArea" style="margin: 0 auto; width: 600px; height:400px;"></div>
    </div>
</template>


<script>
// import axios from 'axios'
// import echarts from '//cdn.bootcss.com/echarts/3.2.2/echarts.simple.min.js'
// var echarts = require('echarts/lib/echarts');
// require('echarts/lib/chart/pie')
// require('echarts/lib/component/tooltip');

axios.defaults.baseURL = 'http://123.207.89.91:5000/api';
var myChart = null;

// var options = ({
//     backgroundColor: 'white',

//     tooltip : {
//         trigger: 'item',
//         formatter: "{a} {b}: {c} ({d}%)"
//     },

//     visualMap: {
//         show: true,
//         min: 80,
//         max: 600,
//         inRange: {
//             colorLightness: [0, 1]
//         }
//     },
//     series: [
//         {
//             name:'来源',
//             type:'pie',
//             radius : '55%',
//             center: ['50%', '50%'],
//             data:[],
//             roseType: 'radius',
//         }
//     ]
// })

export default {
  name:'analysis',
  data () {
    return {
        analysisData: [],
        analysisItems: [
            {text: '来源', value: 'source'},
            {text: '泄露时间', value: 'xtime'},
            {text: '邮箱后缀', value: 'suffix_email'}
        ]
    }
  },
  methods:{
    flashAnalysis: function (value) {
        myChart = echarts.init(document.getElementById('chartArea'));
        myChart.showLoading({
            text: "数据获取ing...",
        });
        axios.get('/analysis/'+value).then(response => {
            if(response.data.status === 'ok'){
                this.analysisData = [];
                for (var key in response.data.data) {
                    var item = response.data.data[key];
                    this.analysisData.push({
                        "value": item["sum"],
                        "name": item["_id"]
                    })
                }
                myChart.hideLoading();
                myChart.setOption({
                    tootip: {
                        show: true,
                        trigger: 'item',
                        formatter: "{a} {b}: {c} ({d}%)"
                    },
                    series: {
                        name: '来源',
                        type: 'pie',
                        data: this.analysisData
                    }
                });

            }
        })
        .catch(error => { console.log(error); })
        }
    },
    // mounted(){
    //     myChart = echarts.init(document.getElementById('chartArea'));
    // }
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
