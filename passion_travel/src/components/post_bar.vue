<template>
<div>
  <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <title>发表问题 - 马蜂窝</title>
      <meta name="renderer" content="webkit" />

      <link
        href="http://css.mafengwo.net/css/cv/css+base:css+jquery.suggest:css+plugins:css+plugins+jquery.jgrowl:css+other+popup:css+mfw-header.2015^YlVS^1566868943.css"
        rel="stylesheet"
        type="text/css"
      />

      <link
        href="http://css.mafengwo.net/css/cv/css+mfw-ask+change_ask_v2:css+mfw-ask+upload_pics^Z1w^1552011937.css"
        rel="stylesheet"
        type="text/css"
      />
      <link
        href="http://css.mafengwo.net/css/mfw-footer.css?1558532347"
        rel="stylesheet"
        type="text/css"
      />

      <link
        href="http://css.mafengwo.net/css/mfw-toolbar.css?1537192876"
        rel="stylesheet"
        type="text/css"
      />
    </head>
    <body style="position: relative;">
      <header1></header1>
      <input
        type="hidden"
        id="_j_info"
        data-tags="{&quot;1016&quot;:&quot;\u81ea\u9a7e&quot;,&quot;1052&quot;:&quot;\u4eb2\u5b50&quot;,&quot;1040&quot;:&quot;\u6444\u5f71&quot;,&quot;1036&quot;:&quot;\u7f8e\u98df&quot;,&quot;1044&quot;:&quot;\u6ed1\u96ea&quot;,&quot;1068&quot;:&quot;\u8d2d\u7269&quot;,&quot;1112&quot;:&quot;\u5f92\u6b65&quot;,&quot;1048&quot;:&quot;\u6f5c\u6c34&quot;,&quot;1096&quot;:&quot;\u9a91\u884c&quot;}"
        data-bind_mobile="0"
        data-ask_uid="0"
      />
      <div class="wrapper" id="_js_qa_wrapper" data-is_bind_mobile="0" data-ask_uid="0">
        <div class="qt-container clearfix">
          <!-- 提问主要内容 -->
          <div class="qt-main">
            <!-- 面包屑导航 -->
            <div class="crumb">
              <a href="/wenda/">旅游问答</a> &gt;
              <span>我要提问</span>
            </div>

            <!-- 问题标题 -->
            <div class="qt-tit">
              <h5>问题标题</h5>
              <div class="qt-con">
                <input type="text" placeholder="标题不小于10字哦" class="_j_title" v-model="forum_name" />
                <span class="count">
                  <span class="_j_title_num">0</span>/80 字
                </span>
                <span class="_j_min_num hide">10</span>
                <span class="error err-tips _j_title_error hide"></span>
              </div>
            </div>

            <!-- 问题详细内容 -->
            <div class="qt-details" id="_qa_detail">
              <!-- 工具栏容器 -->
              <div id="toolbar-container"></div>

              <!-- 编辑器容器 -->
              <div id="editor">
                <p>This is the initial editor content.</p>
              </div>
            </div>

            <!-- 选择目的地 -->
            <div class="qt-mdd _qa_block" id="_qa_mdd">
              <h5>选择目的地</h5>
              <div class="qt-con _qa_select" id="_qa_select_mdds">
                <input type="text" placeholder class="_j_mdd" v-model="city" />
              </div>
            </div>

            <div class="qt-interest _qa_block" id="_qa_interest">
              <h5>选择兴趣标签</h5>
              <div class="qt-con _j_interest_list">
                <dl class="interest-description">
                  <dt>
                    <i></i>
                    <span>什么是兴趣标签</span>
                  </dt>
                  <dd>兴趣标签是一个问题的类型，它有助于为你的问题匹配擅长该类问题的蜂蜂回答。目前仅开放了以下几个话题，更多类型我们会逐步开放。</dd>
                </dl>
                <div class="interest-tags">
                  <a class="btn-interest _j_interest" data-id="1016">
                    <i></i>自驾
                  </a>
                  <a class="btn-interest _j_interest" data-id="1052">
                    <i></i>亲子
                  </a>
                  <a class="btn-interest _j_interest" data-id="1040">
                    <i></i>摄影
                  </a>
                  <a class="btn-interest _j_interest" data-id="1036">
                    <i></i>美食
                  </a>
                  <a class="btn-interest _j_interest" data-id="1044">
                    <i></i>滑雪
                  </a>
                  <a class="btn-interest _j_interest" data-id="1068">
                    <i></i>购物
                  </a>
                  <a class="btn-interest _j_interest" data-id="1112">
                    <i></i>徒步
                  </a>
                  <a class="btn-interest _j_interest" data-id="1048">
                    <i></i>潜水
                  </a>
                  <a class="btn-interest _j_interest" data-id="1096">
                    <i></i>骑行
                  </a>
                </div>
              </div>
            </div>

            <!-- 通知 -->
            <div class="qt-notice">
              <div class="checkbox _j_anonymous"></div>
              <p>匿名提问（其他用户将不会在你的窝里看到这个问题）</p>
            </div>
            <div class="qt-notice _qa_block" id="_qa_notice">
              <div class="checkbox _j_mobile active"></div>
              <p>收到答案时短信通知我</p>
            </div>

            <!-- 发布按钮 -->
            <!-- <div class="publish_question"> -->
            <button class="qt-post-btn _j_publish" title="发布问题" @click="sub">发布问题</button>
            <!-- </div> -->
          </div>

          <!-- 提问侧边栏 -->
          <div class="qt-sider">
            <div class="qts-tit">提问的正确姿势</div>
            <div class="qts-con">
              <p>1.问题要【具体】【真实】【诚恳】，问题较多，需全面阐述时，可以添加问题补充。结伴/交易/与旅行无关的提问将被删除。</p>
              <p>2.给问题添加目的地，并打上正确的标签将有助于更快地获得回答。</p>
            </div>
          </div>
        </div>
      </div>
      <foot></foot>
    </body>
  </html>
</div>
</template>
<script>

import header from "@/components/header";
import foot from "@/components/foot";
import { send, sendToken } from "../../static/js/comm";
import CKEditor from "@ckeditor/ckeditor5-build-decoupled-document";
import "@ckeditor/ckeditor5-build-decoupled-document/build/translations/zh-cn"; //中文包
export default {
  data: function() {
    return {
      forum_name: "",
      city: "",
      tag_id: 88,
      is_anonymity: 0,
      is_note: 0,
      editor:null,//编辑器实例
    };
  },
  components: {
    header1: header,
    foot: foot,
  
  },
  mounted() {
    this.initCKEditor()
  },
  methods: {
    sub: function() {
      sendToken("http://47.97.203.203:8000/user/user_forum/", "post", {
        forum_name: this.forum_name,
        forum_text: this.editor.getData(),
        city: this.city,
        tag_id: this.tag_id,
        is_anonymity: this.is_anonymity,
        is_note: this.is_note,
        user_id: localStorage.getItem("user_id")
      }).then(res => {
        if (res.data.code == 200) {
          alert("发表成功");
        }
      });
    },
    initCKEditor() {
        CKEditor.create(document.querySelector('#editor'), {
          ckfinder: {
            uploadUrl: 'http://47.97.203.203:8000/user/image/'
            //后端处理上传逻辑返回json数据,包括uploaded(选项true/false)和url两个字段
          }
        }).then(editor => {
          const toolbarContainer = document.querySelector('#toolbar-container');
          toolbarContainer.appendChild(editor.ui.view.toolbar.element);
          this.editor = editor //将编辑器保存起来，用来随时获取编辑器中的内容等，执行一些操作
        }).catch(error => {
          console.error(error);
        });
     }
  }
};
</script>