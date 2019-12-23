<template>
<div>
  <html>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>我的信息</title>

    <link
      href="https://css.mafengwo.net/css/cv/css+base:css+jquery.suggest:css+plugins:css+plugins+jquery.jgrowl:css+other+popup:css+mfw-header.2015^YlVS^1566868943.css"
      rel="stylesheet"
      type="text/css"
    />
    <link
      href="https://css.mafengwo.net/css/other/isettings.css?1551925756"
      rel="stylesheet"
      type="text/css"
    />
    <header1></header1>
    <div class="wrapper clearfix">
      <div class="aside">
        <router-link to="/setting/information">
          <i class="i1"></i>我的信息
        </router-link>

        <router-link to="/setting/myimage">
          <i class="i2"></i>我的头像
        </router-link>

        <router-link to="/setting/addresss">
          <i class="i3"></i>我的地址
        </router-link>
      </div>

      <component :is="componentId" :transport_data="transport_data"></component>
    </div>
    <foot></foot>
  </html>
</div>
</template>
<script>

import header from "@/components/header";
import foot from "@/components/foot";
import { send, sendToken } from "../../static/js/comm";
import addresss from "@/components/userinfor/addresss";
import information from "@/components/userinfor/information";
import myimage from "@/components/userinfor/myimage";

export default {
  data: function() {
    return {
      componentId: "information",
      transport_data: ""
    };
  },
  components: {
    header1: header,
    foot: foot
  },
  methods: {
    add:function(){

    }
  },
  watch: {
    $route() {
      var path_ = this.$route.params.pathMatch; // 获取到了通配符匹配到的路径
      console.log(path_);
      if (path_ == "/information") {
        this.transport_data = "个人信息";
        this.componentId = "information";
      }
      if (path_ == "/myimage") {
        this.transport_data = "这是我的头像";
        this.componentId = "myimage";
      }
      if (path_ == "/addresss") {
        this.transport_data = "这是我的地址";
        this.componentId = "addresss";
      }

      // this.axios({
      // 	url:'/api/' + path_,
      // }).then((res)=>{
      // 	this.transport_data = res.data.data
      // })
    }
  }
};
</script>
        
    

