import Vue from 'vue'
import Router from 'vue-router'
import bourn from '@/components/bourn'
import index from '@/components/index'
import login from '@/components/login'
import register from '@/components/register'
import community from '@/components/community'
import community_detail from '@/components/community_detail'
import setting from '@/components/setting'
import post_bar from '@/components/post_bar'
import strategy from '@/components/strategy'

import AAA from '@/components/AAA'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
    {
        path: '/bourn',
        name: 'bourn',
        component: bourn
    }, 
    {
        path: '/',
        name: 'index',
        component: index
    },
    {
        path: '/login',
        name: 'login',
        component: login
    },
    {
        path: '/register',
        name: 'register',
        component: register
    },
    {
        path: '/community',
        name: 'community',
        component: community
    },
    {
        path: '/community_detail',
        name: 'community_detail',
        component: community_detail
    },
    {
        path: '/setting',
        name: 'setting',
        component: setting
    },
 
    {
        path: '/setting*',
        name: 'setting',
        component: setting
    },
    {
        path: '/post_bar',
        name: 'post_bar',
        component: post_bar
    },
    {
        path: '/strategy',
        name: 'strategy',
        component: strategy
    },
    {
        path: '/AAA',
        name: 'AAA',
        component: AAA
    },

  ]
})
