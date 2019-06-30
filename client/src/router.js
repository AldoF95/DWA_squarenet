import Vue from 'vue'
import Router from 'vue-router'
import Profile from './views/profile_view'
import Home from './views/Home'
import Homepage from './components/homepage'
import ProfileSettings from './components/profile_settings'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/profile/settings',
      name: 'profile-settings',
      component: ProfileSettings
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/',
      name: 'homepage',
      component: Homepage
    },
    {
      path: '/register',
      name: 'register',
      component: Homepage
    }
  ]
})
