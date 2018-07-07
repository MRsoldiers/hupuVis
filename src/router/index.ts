// tslint:disable:match-default-export-name
import Vue from 'vue'
import Router from 'vue-router'

// import HelloWorld from '../components/HelloWorld.vue'

import HupuView from '../components/HupuView.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HupuView',
      component: HupuView
    }
  ]
})
