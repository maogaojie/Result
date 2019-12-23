// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import header from './components/header.vue'
import foot from './components/foot.vue'
import axios from 'axios'
import $ from 'jquery'                                                                                                                                      
import Distpicker from 'v-distpicker'

Vue.config.productionTip = false

Vue.prototype.axios = axios
axios.defaults.baseURL = '/api'
axios.defaults.withCredentials=true;

Vue.component('hd', header)
Vue.component('foot', foot)
    /* eslint-disable no-new */
import information from './components/userinfor/information'
import addresss from './components/userinfor/addresss'
import myimage from './components/userinfor/myimage'

Vue.component('information',information)
Vue.component('addresss',addresss)
Vue.component('myimage',myimage)

new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})
