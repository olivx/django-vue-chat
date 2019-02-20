import Vue from 'vue'
import Router from 'vue-router'

import Chat from '@/components/Chat'
import UserAuth from '@/components/UserAuth'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/auth',
      name: 'UserAuth',
      component: UserAuth
    },
    {
      path: '/chats',
      name: 'Chat',
      component: Chat
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('auth_token') !== null || to.path === '/auth') {
    next()
  } else {
    next('/auth')
  }
})
export default router
