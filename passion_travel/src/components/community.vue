<template>
<div>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>旅游问答,解决旅行问题,基于旅游的问答分享平台 - 马蜂窝</title>
    <meta
      name="description"
      content="马蜂窝旅游问答是基于旅游的问答分享平台,这里聚集了各路旅行达人,只要你有旅行中的问题,在马蜂窝问答问出来,总有旅行经验丰富或者居住在当地的旅行家会为你热心解答"
    />
    <meta name="keywords" content="马蜂窝旅游问答" />
    <meta name="renderer" content="webkit" />
  </head>
  <body style="position: relative;">
    <div class="topBar">
      <div class="topBarC">
        <div class="logo">
          <a title="马蜂窝自由行" href="/">马蜂窝自由行</a>
        </div>
        <div class="t_nav">
          <ul id="pnl_nav" data-cs-t="headnav_wo">
            <li data-cs-p="index">
              <strong class="t">
                <a href="/">首页</a>
              </strong>
            </li>
            <li data-cs-t="wenda" data-cs-p="wenda">
              <strong class="t">
                <a data-cs-p="from_wo_nav" href="/wenda/">问答</a>
              </strong>
            </li>
            <li data-cs-t="things" data-cs-p="things">
              <strong class="t">
                <a data-cs-p="from_wo_nav" href="/mall/things.php">马蜂窝周边</a>
              </strong>
            </li>
            <li data-cs-p="together">
              <strong class="t">
                <a href="/together/">结伴</a>
              </strong>
            </li>
            <li data-cs-p="group">
              <strong class="t">
                <a href="/group/">小组</a>
              </strong>
            </li>
            <li data-cs-p="mall">
              <strong class="t">
                <a href="/club/">蜂首俱乐部</a>
              </strong>
            </li>
            <li class="drop" data-cs-p="other">
              <strong class="t">
                <a href="/app/hun.php">
                  更多
                  <b></b>
                </a>
              </strong>
              <div class="c">
                <a href="/focus/" target="_blank">真人兽</a>

                <a href="/school/" target="_blank">马蜂窝高校</a>
                <a href="/photo_pk/prev.php" target="_blank">照片PK</a>
                <a href="/auction/" target="_blank">马蜂窝拍卖行</a>
                <a href="/mall/virtual_goods.php" target="_blank">道具商店</a>

                <a href="/club/" target="_blank">蜂首聚乐部</a>
                <a href="/home/vip_show.php" target="_blank">VIP</a>
                <a href="/game/wager.php" target="_blank">分歧终端机</a>
              </div>
            </li>
          </ul>
        </div>
        <div class="t_search">
          <form method="GET" action="/search/q.php" name="search">
            <input type="text" class="key" value name="q" id="word" />
            <input type="submit" value class="btn" />
          </form>
        </div>

        <div class="t_info">
          <div
            id="pagelet-block-23a93ec36a5cd508e2d7f6f156aec4a9"
            class="pagelet-block"
            data-api="apps:user:pagelet:pageViewHeadInfo"
            data-params="{&quot;type&quot;:2}"
            data-async="1"
            data-controller="/js/pageletcommon/pageHeadUserInfoWWWDark"
          >
            <div class="no_login">
              <span>
                <a href="https://passport.mafengwo.cn">登录</a> /
                <a href="https://passport.mafengwo.cn/regist.html">注册</a>
              </span>
              <a class="login-qq" href="https://passport.mafengwo.cn/qq"></a>
              <a class="login-weibo" href="https://passport.mafengwo.cn/weibo"></a>
              <a class="login-renren" href="https://passport.mafengwo.cn/renren"></a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <input
      type="hidden"
      id="_j_param"
      data-type="0"
      data-key
      data-mddid
      data-tid
      data-more="1"
      data-time
    />
    <div class="wrapper wrapper-new" data-cs-t="wenda">
      <div class="col-main">
        <div class="i-main">
          <div class="mt-nav clearfix i_link">
            <a href="/wenda/">问答首页</a>
            <em></em>
            <div class="drop-mine _j_crumb_my">
              <a class="drop-hd" href="/wenda/u/0/answer.html" target="_blank">
                <i></i>我的问答
              </a>
              <ul class="drop-bd" style="display: none;">
                <li>
                  <a href="/wenda/u/0/question.html" target="_blank">我的提问</a>
                </li>
                <li>
                  <a href="/wenda/u/0/answer.html" target="_blank">我的回答</a>
                </li>
                <li>
                  <a href="/wenda/u/0/solution.html" target="_blank">为我推荐的提问</a>
                </li>
              </ul>
            </div>
            <em></em>
            <a href="/qa/expert.php">指路人</a>
            <em></em>
            <a href="/mall/" target="_blank">
              马蜂窝商店
              <i class="ask_hot_ico"></i>
            </a>
            <span class="title">
              <a class="mobile-wd">
                <i></i>手机问答
                <div class="h5_ask"></div>
              </a>
              <em></em>
              <a href="/g/i/11289526.html" target="_blank">
                <i></i>查看如何使用
              </a>
            </span>
          </div>

          <div class="search-box">
            <div class="search-panel" data-cs-t="wenda">
              <div class="clearfix _j_suggest_hd">
                <div class="sp-input">
                  <input
                    type="text"
                    id="_j_wenda_seach_input"
                    value
                    placeholder="提问前请先搜索，看看你的问题其他蜂蜂是否已经问过"
                  />
                </div>
                <input type="button" id="_j_wenda_seach_button" class="sp-button" data-mddid="0" />
              </div>
              <div class="bd _j_suggest_box hide"></div>
            </div>
          </div>
        </div>
        <div class="newcate-wrap _j_qa_list">
          <div class="hd">
            <ul class="cate-tab">
              <li class="on _j_change_type" data-type="0">
                <a>热门问题</a>
              </li>
              <li class="_j_change_type" data-type="1">
                <a>最新问题</a>
              </li>
              <li class="_j_change_type" data-type="2">
                <a>待回答问题</a>
              </li>
            </ul>
          </div>
          <div class="bd newcate-bd" v-for="i in bar_list" :key="i.index">
            <ul class="_j_pager_box">
              <li class="item clearfix" data-qid="10474851">
                <div class="title">
                  <router-link :to="{name:'community_detail',query:{id:i.id}}">{{i.forum_name}}</router-link>
                </div>
                <div class="container">
                  <div class="avatar">
                    <a href="/wenda/u/79167497/answer.html" target="_blank" class="_j_filter_click">
                      <img class="_j_filter_click" :src="i.user.image_name" />
                    </a>
                  </div>
                  <div class="user-info">
                    {{i.user.name}}
                    <a
                      class="level _j_filter_click"
                      href="/rank/lv.php?uid=79167497"
                      target="_blank"
                      rel="nofollow"
                    >LV.40</a>
                  </div>
                  <div class="desc clearfix">
                    <a
                      href="/wenda/detail-10474851-10629958.html"
                      target="_blank"
                      style="color: #666;"
                    >
                      <div v-html="i.forum_text"></div>
                    </a>
                  </div>
                  <div class="tags">
                    <a
                      class="a-tag _j_filter_click"
                      href="/wenda/tag-19229.html"
                      target="_blank"
                    >行前准备</a>
                    <a
                      class="a-tag _j_filter_click"
                      href="/wenda/tag-17968.html"
                      target="_blank"
                    >当地体验</a>
                    <a class="a-tag _j_filter_click" href="/wenda/tag-3131.html" target="_blank">涛岛</a>
                    <a
                      class="a-tag _j_filter_click"
                      href="/wenda/tag-18851.html"
                      target="_blank"
                    >休闲娱乐</a>
                    <a class="a-tag _j_filter_click" href="/wenda/tag-1291.html" target="_blank">住宿</a>
                  </div>
                  <div class="operate">
                    <div class="zan">
                      <i></i>336
                    </div>
                    <div class="mdd">
                      <a href="/wenda/area-187613.html" class="_j_filter_click" target="_blank">
                        <i class="_j_filter_click"></i>全球
                      </a>
                    </div>
                    <div class="cate-share">
                      <a class="_js_showShare _j_filter_click">分享</a>
                      <div
                        class="cate-share-pop _j_share_pop hide clearfix"
                        data-title="把兴趣爱好变成职业，是怎样的体验？"
                        data-qid="10474851"
                        data-aid="10629958"
                        data-anum="412"
                        data-content="谢邀，蜂蜂们大家好，我是 @路客 ，旅行摄影玩家，职业摄影师。两年前辞去国内某一线互联网公司高管职位，一个人背起相机就走上这条持续了500多天的旅途（并还在继续）。虽然这段经历听起来很潇洒很牛B，但跟很多旅行家不同的是我没火，哈哈哈哈…以下回答仅代表..."
                      >
                        <a
                          title="分享到新浪微博"
                          class="sina _j_do_share _j_filter_click"
                          data-site="wb"
                          data-username="路客照相机"
                        ></a>
                        <a
                          title="分享到QQ空间"
                          class="zone _j_do_share _j_filter_click"
                          data-site="qz"
                          data-username="路客照相机"
                        ></a>
                        <a
                          title="分享到微信"
                          class="weixin _j_do_share_wx _j_filter_click"
                          data-site="wx"
                          data-username="路客照相机"
                        ></a>
                      </div>
                    </div>
                    <a
                      href="/wenda/detail-10474851-10629958.html"
                      target="_blank"
                      style="text-decoration: none;"
                    >
                      <span class="reply">评论 (145)</span>
                    </a>
                    <span class="date">发布于2017-12-25 04:16</span>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <div class="_j_pager">
            <div class="ft ft_load_btn">
              <div class="answer-more _j_add_more_button">
                <a>
                  加载更多
                  <i></i>
                </a>
              </div>
            </div>
            <div class="ft ft_loading _j_add_loading_button hide">
              <div class="answer-loading">
                正在加载
                <i></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-side">
        <div class="i-ask">
          <router-link :to="{name:'post_bar'}" class="btn-ask btn-ask2">
            <i></i>我要提问
          </router-link>
        </div>

        <div class="i_total">
          <div class="i_total" data-cs-t="wenda">
            <div class="mod mod-slide _j_slide">
              <ul class="slide-img _j_slide_img" data-cs-p="topic_recommend_pic">
                <li style="display: none;">
                  <span>
                    <a
                      target="_blank"
                      href="https://www.mafengwo.cn/wenda/detail-18411223-18459260.html"
                    >
                      <img
                        src="https://n1-q.mafengwo.net/s9/M00/47/BA/wKgBs12B9giAUUdaAADar4FZtQk984.jpg"
                      />
                    </a>
                  </span>
                  <h3>
                    <a
                      target="_blank"
                      href="https://www.mafengwo.cn/wenda/detail-18411223-18459260.html"
                    >如何省钱/赚钱保持常年旅行？</a>
                  </h3>
                </li>
                <li style="display: none;">
                  <span>
                    <a target="_blank" href="https://imfw.cn/l/26765236">
                      <img
                        src="https://n3-q.mafengwo.net/s13/M00/02/F6/wKgEaVx2WNSATa4-AADhkqCkWA468.jpeg"
                      />
                    </a>
                  </span>
                  <h3>
                    <a target="_blank" href="https://imfw.cn/l/26765236">坐飞机应如何挑选到好座位？</a>
                  </h3>
                </li>
                <li style="display: list-item;">
                  <span>
                    <a
                      target="_blank"
                      href="http://www.mafengwo.cn/wenda/detail-15453646-15512742.html"
                    >
                      <img
                        src="https://p3-q.mafengwo.net/s12/M00/B4/0F/wKgED12B91uAfmgeAAD8bvp7kT0659.jpg"
                      />
                    </a>
                  </span>
                  <h3>
                    <a
                      target="_blank"
                      href="http://www.mafengwo.cn/wenda/detail-15453646-15512742.html"
                    >有什么APP可以拯救废片？</a>
                  </h3>
                </li>
              </ul>
              <div class="slide-trigger" id="_j_slide_btn">
                <span class data="0"></span>
                <span data="1" class></span>
                <span data="2" class="on"></span>
              </div>
            </div>
          </div>

          <div class="i_num">
            共
            <span id="q_total">4662147</span>问题
            <span id="u_total">9052302</span>人参与
          </div>
        </div>

        <dl class="i-tags tag-area _j_tags">
          <dt>问答热门地区</dt>
          <dd class="clearfix">
            <div class="label">境外</div>
            <ul class="_j_open_mdd_list">
              <li>
                <a
                  class="_j_change_mdd"
                  data-mddid="10189"
                  data-cs-p="index_foreign_mdd"
                  title="香港"
                  data-mddname="香港"
                >
                  香港
                  <em>61854</em>
                </a>
              </li>

              <li class="_j_mdd_see_more">
                <a class="more_selector" data-cs-p="index_foreign_seemore">更多</a>
              </li>
            </ul>
          </dd>
          <dd class="clearfix">
            <div class="label">境内</div>
            <ul class="_j_open_mdd_list">
              <li>
                <a
                  class="_j_change_mdd"
                  data-mddid="10068"
                  data-cs-p="index_china_mdd"
                  title="哈尔滨"
                  data-mddname="哈尔滨"
                >
                  哈尔滨
                  <em>14056</em>
                </a>
              </li>

              <li class="_j_mdd_see_more">
                <a class="more_selector" data-cs-p="index_china_seemore">更多</a>
              </li>
            </ul>
          </dd>
        </dl>

        <div class="rank _j_rank" style="margin-top: 20px;">
          <div class="hd">
            排行榜
            <ul class="tab-time">
              <li class="_j_rank_change_date" data-type="0">
                <span>今日</span>
              </li>
              <li class="_j_rank_change_date" data-type="1">
                <span>本周</span>
              </li>
              <li class="_j_rank_change_date on" data-type="2">
                <span>本月</span>
              </li>
            </ul>
          </div>
          <div class="bd">
            <ul class="tab-num" data-cs-p="rank_list">
              <li class="on _j_rank_change_flag" data-rank="0" data-cs-d="金牌数">金牌数</li>
              <li class="_j_rank_change_flag" data-rank="1" data-cs-d="回答数">回答数</li>
              <li class="_j_rank_change_flag" data-rank="2" data-cs-d="被顶次数">被顶次数</li>
            </ul>
            <ul class="rank-list _j_rank_list">
              <li class="r-top r-top1 clearfix">
                <em class="num">1</em>
                <div class="user no_qid">
                  <a
                    class="avatar"
                    href="/wenda/u/85649206/answer.html"
                    target="_blank"
                    rel="nofollow"
                  >
                    <img
                      src="https://p1-q.mafengwo.net/s11/M00/C9/78/wKgBEFzsCTmAaMArACXkCuEMtDs88.jpeg?imageMogr2%2Fthumbnail%2F%2148x48r%2Fgravity%2FCenter%2Fcrop%2F%2148x48%2Fquality%2F90"
                    />
                  </a>
                  <span class="name">
                    <a href="/wenda/u/85649206/answer.html" target="_blank" rel="nofollow">JC-JIANG</a>
                  </span>
                  <span class="level">
                    <a href="/wenda/u/85649206/answer.html" target="_blank" rel="nofollow">LV.28</a>
                  </span>
                </div>
                <span class="num">85</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div id="float-pannel-gloable">
      <img
        class="float-image"
        src="https://p4-q.mafengwo.net/s14/M00/BB/8C/wKgE2l0r2W-ALHaeAACAt6lqXyA464.png"
        style="width:178px;"
      />
      <div class="float-btn">
        <img
          id="closed"
          src="https://n4-q.mafengwo.net/s13/M00/46/AC/wKgEaVy2xHeAZJhRAAADGY-wozY871.png"
        />
      </div>
    </div>

    <foot></foot>
  </body>
</div>
</template>
<script>
import foot from "@/components/foot";
import { send } from "../../static/js/comm";
export default {
  data: function() {
    return {
      bar_list: ""
    };
  },
  component: {
    foot: foot
  },
  mounted() {
    send("http://47.97.203.203:8000/user/all_forum/", "get").then(res => {
      console.log(res);

      if (res.data.code == 200) {
        this.bar_list = res.data.all_forum;
        console.log(res.data);
      }
    });
  }
};
</script>