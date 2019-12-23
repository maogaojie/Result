<template>
<div>
  <html>
    <head>
      <link
        href="https://css.mafengwo.net/css/cv/css+login+login_v2:mobile+css+omc+login-omc+login-omc^ZlY^1550829726.css"
        rel="stylesheet"
        type="text/css"
      />

      <link
        href="https://static.tongdun.net/captcha/main/1.7.5/tdCaptcha.css?t=437336"
        rel="stylesheet"
        type="text/css"
      />
      <link
        href="https://css.mafengwo.net/css/cv/css+login+login_v2:mobile+css+omc+login-omc+login-omc^ZlY^1550829726.css"
        rel="stylesheet"
        type="text/css"
      />

      <link
        href="https://static.tongdun.net/captcha/main/1.7.5/tdCaptcha.css?t=437336"
        rel="stylesheet"
        type="text/css"
      />
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <title>帐号登录 - 马蜂窝</title>
      <meta property="mfw:partner-platform" content />
    </head>
    <body>
      <div class="wrapper">
        <div class="container container-login">
          <a href="http://www.mafengwo.cn" title="返回首页" class="logo">马蜂窝</a>
          <div class="signup-forms flip">
            <div class="login-box" id="_j_login_box">
              <div class="inner inner_v2 clearfix">
                <div class="inner_v2_left">
                  <div class="form-field">
                    <input
                      v-model="username"
                      type="text"
                      placeholder="您的手机号"
                      autocomplete="off"
                      data-verification-name="帐号"
                      class="verification[required,maxSize[50],funcCall[checkShowCode]]"
                      value
                    />
                    <div class="err-tip"></div>
                  </div>
                  <div class="form-field">
                    <input
                      v-model="password"
                      type="password"
                      placeholder="您的密码"
                      autocomplete="off"
                      data-verification-name="密码"
                      class="verification[required,minSize[4],maxSize[50]]"
                    />
                    <div class="err-tip"></div>
                  </div>
                  <div class="form-link">
                    <a href="/forget">忘记密码</a>
                  </div>
                  <div class="submit-btn">
                    <button @click="login">登 录</button>
                  </div>

                  <div class="connect">
                    <p class="hd">用合作网站账户直接登录</p>
                    <div class="bd">
                      <a href="/weibo" class="weibo">
                        <i></i>新浪微博
                      </a>
                      <a href="/qq" class="qq">
                        <i></i>QQ
                      </a>
                      <a href="/wechat" class="weixin">
                        <i></i>微信
                      </a>
                      <div class="clear"></div>
                    </div>
                  </div>
                </div>
                <div class="inner_v2_right">
                  <img
                    src="https://ss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1369340476,1334861031&fm=74&app=80&f=PNG&size=f121,90?sec=1880279984&t=a137ce773bb7ae585c3b70a051c996dc"
                  />
                  <p>Hi this is wasp</p>
                </div>
              </div>
              <div class="bottom-link">
                还没有帐号?
                <router-link :to="{name:'register'}">马上注册</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="photoby">
        &lt;&nbsp;
        <a href="http://www.mafengwo.cn/i/3070996.html" target="_blank">摩洛哥的零一夜</a>&nbsp;&gt;&nbsp;by&nbsp;
        <a
          href="http://www.mafengwo.cn/u/69428094.html"
          target="_blank"
        >ir_is_qr</a>
      </div>
      <div
        class="fullscreen-bg"
        style="background-image: url(&quot;https://images.mafengwo.net/images/signup/wallpaper/21.jpg&quot;);"
      >
        <img
          src="https://images.mafengwo.net/images/signup/wallpaper/21.jpg&#10;"
          style="width: 1295px; height: auto; margin-top: -93px;"
        />
      </div>
    </body>
  </html>
</div>
</template>
<script>
import { send, sendToken } from "../../static/js/comm";
export default {
  name: "login",
  data: function() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    login: function() {
      send("http://47.97.203.203:8000/user/login/", "post", {
        username: this.username,
        password: this.password
      }).then((res)=>{
        if (res.data.code == 200){
          localStorage.setItem('user_id',res.data.user_id)
          localStorage.setItem('token',res.data.token)
          localStorage.setItem('name',res.data.name)
          alert('登录成功')
          this.$router.push('/')
        }
      });
    }
  }
};
</script>
