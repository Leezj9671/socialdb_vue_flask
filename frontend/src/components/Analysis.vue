<template>
    <div class="analysis">
        <h2>当前数据库分析:</h2>
        <button v-for="key in analysisItems" v-bind:value="key.value" @click="flashAnalysis(key.value)">
            {{ key.text}}
        </button>
        <div id="chartArea" style="width: 600px;height:400px;text-align:center" ></div>
    </div>
</template>

<script>
import axios from 'axios'
import echarts from 'echarts'

axios.defaults.baseURL = 'http://123.207.89.91:5000/api';
var myChart = null;

var options = ({
    backgroundColor: 'white',

    title: {
        text: '数据分析',
        left: 'middle',
        top: 20,
        textStyle: {
            color: '#ccc'
        }
    },

    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },

    visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
            colorLightness: [0, 1]
        }
    },
    series : [
        {
            name:'来源',
            type:'pie',
            radius : '55%',
            center: ['50%', '50%'],
            data:[],
            roseType: 'radius',
            label: {
                normal: {
                    textStyle: {
                        color: 'rgba(255, 255, 255, 0.3)'
                    }
                }
            },
            labelLine: {
                normal: {
                    lineStyle: {
                        color: 'rgba(255, 255, 255, 0.3)'
                    },
                    smooth: 0.2,
                    length: 10,
                    length2: 20
                }
            },
            itemStyle: {
                normal: {
                    color: '#c23531',
                    shadowBlur: 200,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            },

            animationType: 'scale',
            animationEasing: 'elasticOut',
            animationDelay: function (idx) {
                return Math.random() * 200;
            }
        }
    ]
})

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
                // options.series.push({
                //         name: '来源',
                //         type: 'pie',
                //         data: this.analysisData
                // })
                myChart.setOption({
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
    mounted(){
        myChart = echarts.init(document.getElementById('chartArea'));
    }
}
</script>

