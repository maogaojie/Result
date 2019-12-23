<template>
  <div id="header" xmlns="http://www.w3.org/1999/html">
    <div class="mfw-header">
      <div class="header-wrap clearfix" id="_j_head_nav_warper">
        <div class="head-logo">
          <a class="mfw-logo" title="马蜂窝自由行" href="http://www.mafengwo.cn/"></a>
        </div>
        <ul class="head-nav" data-cs-t="headnav" id="_j_head_nav">
          <li
            class="head-nav-index _j_head_nav_index head-nav-active"
            data-cs-p="s"
            data-tab-item="首页"
          >
            <a href="http://www.mafengwo.cn/">首页</a>
          </li>
          <li class="head-nav-place _j_head_nav_mdd" data-cs-p="mdd" data-tab-item="目的地">
            <router-link :to="{name:'bourn'}">目的地</router-link>
          </li>
          <li class="head-nav-gonglve _j_head_nav_gonglve" data-cs-p="gonglve" data-tab-item="旅游攻略">
            <router-link :to="{name:'strategy'}">旅游攻略</router-link>
          </li>
         
        
         
          <li class="head-nav-hotel _j_head_nav_hotel" data-cs-p="hotel" data-tab-item="社区">
            <router-link :to="{name:'community'}">社区</router-link>
          </li>

         
          <li
            class="head-nav-choice _j_head_nav_choice"
            data-cs-p="choice"
            data-tab-item="马蜂窝旅行者之选"
          >
            <a href="http://www.mafengwo.cn/poi/choice/group">
              <div class="mfwzx-logo"></div>
            </a>
          </li>
        </ul>
        <div class="head-search" data-online="1">
          <div class="head-search-wrapper">
            <div class="head-searchform">
              <input name="q" type="text" id="_j_head_search_input" autocomplete="off" />
              <a role="button" href="javascript:" class="icon-search" id="_j_head_search_link"></a>
            </div>
          </div>
        </div>
        <div
          id="pagelet-block-159051b6ca00900bc6cb7ec08172705c"
          class="pagelet-block"
          data-api="apps:user:pagelet:pageViewHeadInfo"
          data-params="{&quot;type&quot;:1}"
          data-async="1"
          data-controller="/js/pageletcommon/pageHeadUserInfoWWWNormal"
        >
          <div class="login-out" v-if="name==''">
            <a
              class="weibo-login"
              href="https://passport.mafengwo.cn/weibo"
              title="微博登录"
              rel="nofollow"
            ></a>
            <a class="qq-login" href="https://passport.mafengwo.cn/qq" title="QQ登录" rel="nofollow"></a>
            <a
              class="weixin-login"
              href="https://passport.mafengwo.cn/wechat"
              title="微信登录"
              rel="nofollow"
            ></a>
            
            <router-link :to="{name:'login'}" rel="nofollow">登录</router-link>
            <span class="split">|</span>
            <router-link :to="{name:'register'}" rel="nofollow">注册</router-link>
          </div>
          <div class="login-info">
                  <div class="head-msg" id="_j_head_msg">
                    <router-link class="drop-trigger" :to="{name:'setting'}" rel="nofollow">
                      {{name}}
                      <span class="head-msg-new hide" style="display: none;"></span>
                    </router-link>
                  </div>
                  <div class="head-msg" id="_j_head_msg">
                    <a class="drop-trigger" href="javascript:" rel="nofollow">
                      <i class="icon-msg"></i>
                      消息
                      <i class="icon-caret-down"></i>
                      <span class="head-msg-new hide" style="display: none;"></span>
                    </a>
                  </div>
                  <div class="head-daka ">
                    <a class="btn head-btn-daka" href="javascript:" rel="nofollow" id="head-btn-daka" title="打卡" data-japp="daka">打卡</a>
                    <!-- <a class="btn-active head-btn-daka" href="javascript:" rel="nofollow" id="head-btn-daka-active" title="打卡推荐" data-japp="daka">打卡推荐</a> -->
                    <a class="btn-active head-btn-daka" href="javascript:" rel="nofollow" id="head-btn-daka-active" title="已打卡" data-japp="daka">已打卡</a>
                  </div>
	        </div>
        </div>
      </div>
      <div class="shadow"></div>
    </div>

  </div>
</template>
<script>
export default {
  data:function(){
    return{
      name:localStorage.getItem('name'),
    }
  },

}
</script>
