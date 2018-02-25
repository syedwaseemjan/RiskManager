import Vue from 'vue'
import Router from 'vue-router'

import SubNavbar from './components/SubNavbar'

import About from './views/About'
import Home from './views/Home'
import Risk from './views/Risk'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      components: {
        subnavbar: SubNavbar,
        main: Home
      }
    },
    {
      name: 'risk',
      path: '/risk/:riskId',
      components: {
        subnavbar: SubNavbar,
        main: Risk
      }
    },
    {
      path: '/about',
      components: {
        subnavbar: SubNavbar,
        main: About
      }
    },
    {
      path: '/contact',
      components: {
        subnavbar: SubNavbar,
        main: About
      }
    }
  ]
})
