
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
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <title>帐号登录 - 马蜂窝</title>
      <meta property="mfw:partner-platform" content />
    </head>
    <body>
      <div class="wrapper">
        <div class="container container-login">
          <a href="http://www.mafengwo.cn" title="返回首页" class="logo">马蜂窝</a>
          <div class="signup-forms">
            <div class="signup-box" id="_j_signup_box">
              <div class="inner inner_v2 clearfix">
                <div class="inner_v2_left">
                  
                    <input type="hidden" name="token" value="90ec5a7fa0d0a15fb55c3a97031ecd78" />
                    <div class="form-field">
                      <input type="hidden" name="token" value="a8734c99f91cad1e1fd3902bd3380dbf" />
                      <div class="form-field">
                        <input
                          v-model="name"
                          type="text"
                          placeholder="用户名"
                          autocomplete="off"
                          data-type="mobile"
                          data-verification-name="用户名"
                          class="verification[required,maxSize[50],custom[mobile]]"
                          value
                        />
                        <input
                          v-model="phone"
                          type="text"
                          placeholder="您的手机号码"
                          autocomplete="off"
                          data-type="mobile"
                          data-verification-name="手机号码"
                          class="verification[required,maxSize[50],custom[mobile]]"
                          value
                        />

                        <input
                          v-model="password"
                          type="password"
                          placeholder="您的密码"
                          autocomplete="off"
                          data-type="mobile"
                          data-verification-name="密码"
                          class="verification[required,maxSize[50],custom[mobile]]"
                          value
                        />
                        <input
                          v-model="code"
                          type="text"
                          placeholder="验证码"
                          autocomplete="off"
                          data-type="mobile"
                          data-verification-name="密码"
                          class="verification[required,maxSize[50],custom[mobile]]"
                          value
                        />
                        <button  @click="get_code">获取验证码</button>
                      </div>
                    </div>

                    <div class="submit-btn">
                      <button @click="register">立即注册</button>
                    </div>
                
                  <div class="agreement">
                    注册视为同意
                    <a
                      target="_blank"
                      href="http://www.mafengwo.cn/s/agreement.html"
                    >《马蜂窝用户使用协议》</a>
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
                  <img src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3785526823,2346108270&fm=26&gp=0.jpg" />
                  <p>
                    Hi
                    <br />This is Wasp
                  </p>
                </div>
              </div>
              <div class="bottom-link">
                已有帐号?
                <router-link :to="{name:'login'}">马上登录</router-link>
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
import { send } from "../../static/js/comm";
export default {
  name: "register",
  data: function() {
    return {
      phone: "",
      code: "",
      password: "",
      name:''
    };
  },
  methods: {
    get_code: function() {
      if (this.phone == "") {
        alert("请输入手机号");
      } else {
        send("http://47.97.203.203:8000/user/get_code/", "post", {
          phone: this.phone
        }).then(res => {
          if (res.data.code == 200) {
            console.log(res);
          }
        });
      }
    },
    register: function() {
      if ((this.code != "") & (this.password != "") & (this.phone != "") & (this.name != "")) {
        send("http://47.97.203.203:8000/user/register/", "post", {
          username: this.phone,
          phone: this.phone,
          name:this.name,
          password: this.password,
          code: this.code
        }).then(res => {
          if (res.data.code == 200) {
            alert("注册成功");
          }
        });
      } else {
        alert("用户信息不全");
      }
    }
  }
};
</script>