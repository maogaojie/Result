<template>
  <div>
    <div class="content">
      <div class="hd">
        <strong>我的信息</strong>
        <span>
          资料完善度
          <div class="progress">
            <div class="num">65%</div>
            <div class="on" style="width:65%"></div>
          </div>
        </span>
      </div>

      <div class="userinfo">
        <form action method="post" id="_j_form">
          <div
            class="alert alert-danger"
            style="color: #a94442;background-color: #f2dede;border-color: #ebccd1;display:none"
          ></div>
          <dl class="clearfix">
            <dt>名号：</dt>
            <dd>
              <input
                type="text"
                v-model="name"
                maxlength="16"
                autocomplete="off"
                data-verification-name="名号"
                class="verification[required,funcCall[checkNickname]]"
              />
            </dd>
          </dl>
          <dl class="clearfix">
            <dt>性别：</dt>
            <dd>
              <label>
                <span class="cssradio">
                  <input type="radio" v-model="gender" value="0" />
                  <span></span>
                </span>男
              </label>
              <label>
                <span class="cssradio">
                  <input type="radio" v-model="gender" value="1" />
                  <span></span>
                </span>女
              </label>
              <label>
                <span class="cssradio">
                  <input type="radio" v-model="gender" value="2" />
                  <span></span>
                </span>保密
              </label>
            </dd>
          </dl>
          <dl class="clearfix">
            <dt>居住城市：</dt>
            <dd class="input-group">
              <input type="text" v-model="city" autocomplete="off" data-verification-name="居住城市" />
              <ul class="input-suggest"></ul>
            </dd>
          </dl>
          <dl class="clearfix">
            <dt>出生日期：</dt>
            <dd>
              <table style="text-align: right;">
                <tr>
                  <td>
                    <select class="sel_year" name="YYYY">
                      <option value>请选择</option>
                    </select>
                    <font>年</font>
                    <select class="sel_month" name="MM">
                      <option value>请选择</option>
                    </select>
                    <font>月</font>
                    <select class="sel_day" name="DD">
                      <option value>请选择</option>
                    </select>
                    <font>日</font>
                  </td>
                </tr>
                <tr></tr>
              </table>
            </dd>
          </dl>
          <dl class="clearfix">
            <dt>个人简介：</dt>
            <dd>
              <textarea
                v-model="intro"
                data-verification-name="个人简介"
                placeholder="例：摄影师/旅居澳洲/潜水爱好者"
                class="verification[maxSize[100]]"
                maxlength="100"
              ></textarea>
            </dd>
          </dl>

          <div class="btn-sub">
            <button @click="sub">保存</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import header from "@/components/header";
import foot from "@/components/foot";
import { send, sendToken } from "../../../static/js/comm";

export default {
  data: function() {
    return {
      birth_year: "",
      birth_month: "",
      birth_day: "",
      name: "",
      gender: "",
      intro: "",
      city: ""
    };
  },

  methods: {
    sub: function() {
      sendToken("http://47.97.203.203:8000/user/userinfor/", "post", {
        birth_year: this.birth_year,
        birth_month: this.birth_month,
        birth_day: this.birth_day,
        name: this.name,
        gender: this.gender,
        intro: this.intro,
        city: this.city
      }).then(res => {
        if (res.data.code == 200) {
          alert("保存成功");
        }
      });
    }
  }
};
</script>