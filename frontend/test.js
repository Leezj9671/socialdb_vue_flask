// testdata
var items = [
    {
        "user":"123",
        "password":"1234",
        "passwordHash":"asdfadsfasd",
        "email":"afsd@qq.com",
        "source":"jd",
        "xtime":"2016.2"
    },
    {
        "user":"123",
        "password":"1234",
        "passwordHash":"asdfadsfasd",
        "email":"afsd@qq.com",
        "source":"jd",
        "xtime":"2016.2"
    }
];

var ainfo = [
    {
        "jd":123,
        "tb":110,
        "qq":100
    }
];

axios.defaults.baseURL = 'http://123.207.89.91:5000/api';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
var vm = new Vue({
    el:".main",
    data:{
        selected: 'user',
        options: [
        { text: '用户名', value: 'user' },
        { text: '密码', value: 'password' },
        { text: '哈希密码', value: 'passwordHash' },
        { text: '邮箱', value: 'email' }
        ],
        retItems: items,
        analysisInfos: ainfo,
    },
    methods:{
        search(ev){
            console.log(ev.target.value)
            console.log(this.data.selected)
            axios.get('/find/' + selected + '/' + ev.target.value)
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        flashAnalysis(){
            console.log("analysis")
        }
    }
});