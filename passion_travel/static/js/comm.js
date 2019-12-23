import axios from 'axios' 
//封装axios请求
export function send(url,type,data){
    var d = new FormData()
    for (var key in data){
        d.append(key,data[key])
    }
    return axios({
        url:url,
        method:type,
        data:d,
    })
}


export function sendToken(url,type,data){
    var d = new FormData()
    for (var key in data){
        d.append(key,data[key])
    }
    var token = localStorage.getItem('token')
    console.log('token:'+token)
    return axios({
        url:url,
        data:data,
        method:type,
        responseType:'json',
        headers:{
            'Authorization':'JWT '+token
        }
    })
}
