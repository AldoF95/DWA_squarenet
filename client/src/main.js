import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

Vue.use(require('vue-moment'))

import axios from'axios'
Vue.use(axios)

import VueCookie from 'vue-cookie'
Vue.use(VueCookie)

import VCalendar from 'v-calendar'
Vue.use(VCalendar)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
