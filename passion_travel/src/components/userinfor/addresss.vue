<template>
  <div>
    <div class="content">
      <div class="hd">
        <strong>收货地址</strong>
        <span>
          资料完善度
          <div class="progress">
            <div class="num">65%</div>
            <div class="on" style="width:65%"></div>
          </div>
        </span>
      </div>

      <div class="userinfo">
        <!--setMobile-->
        <div class="set-mobile">
          <form id="addForm">
            <!--UserInfo-->
            <dl class="clearfix">
              <dt>姓名：</dt>
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
              <dt>所在地区:</dt>
              <v-distpicker
               
                province="---请选择省---"
                city="---请选择市---"
                area="---请选择区---"
              ></v-distpicker>
            </dl>
            <dl class="clearfix">
              <dt>详细地址：</dt>
              <dd>
                <textarea
                  v-model="detail"
                  
                  class="checkEmpty"
                  data-error="请填写详细地址"
                ></textarea>
              </dd>
            </dl>
            <dl class="clearfix">
              <dt>手机号码：</dt>
              <dd>
              
                <input
                  type="text"

                  v-model="phone"
                  class="checkEmpty"
                  data-error="请填写手机号码"
                />
            
              </dd>
            </dl>
            <dl class="clearfix">
              <dt>邮政编码：</dt>
              <dd>
                <input
                  type="text"
                  
                  v-model="zipcode"
                 
                  class="checkEmpty"
                  data-error="请填写邮政编码"
                />
              </dd>
            </dl>
            <!-- <dl class="clearfix">
              <dd class="set-first">
                <input type="hidden" id="is_default" name="is_default" value="0" />
                <input type="check" name="is_default" id="setDefault"/>设置为默认收货地址
              </dd>
            </dl> -->
          </form>
          <dl class="clearfix">
            <dd class="btn-sub">
              <a class="btn2"  @click="clear">取消</a>
              <a class="btn1" @click="save">保存</a>
            </dd>
          </dl>
       
          <!--UserInfoEnd-->
        </div>
        <!--setMobile end-->
      </div>
    </div>
  </div>
</template>
<script>
import { sendToken } from "../../../static/js/comm";
import VDistpicker from "v-distpicker";

export default {
  data: function() {
    return {
      provice: "",
      city: "",
      area: "",
      name:'',
      detail:'',
      phone:'',
      zipcode:''

    };
  },

  methods: {
    save: function(data) {
      this.provice = data.provice.value;
      this.city = data.city.value;
      this.area = data.area.value;
      console.log(data);
      sentToken("http://47.97.203.203:8000/user/login/", "post", {});
    },
    clear:function(){
      this.provice='';
      this.city='',
      this.area='',
      this.name='',
      this.detail='',
      this.phone='',
      this.zipcode='',
      location.reload()
    }
  },
  components: {
    VDistpicker
  }
};
</script>