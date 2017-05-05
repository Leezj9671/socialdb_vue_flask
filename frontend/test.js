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
]

var ainfo = [
    {
        "jd":123,
        "tb":110,
        "qq":100
    }
]

var vm = new Vue({
    el:".main",
    data:{
        selected: '用户名',
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
        },
        flashAnalysis(){
            console.log("analysis")
        }
    }
});