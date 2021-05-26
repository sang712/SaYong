import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Account from '../views/Account.vue'
import Signup from '@/views/Signup.vue'
import Login from '@/views/Login.vue'
import ReviewList from '@/views/ReviewList.vue'
import Review from '@/components/Review.vue'
import MovieDetail from '@/components/MovieDetail.vue'
import AccountPK from '@/views/AccountPK.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/Recommend.vue')
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
  },
  {
    path: '/account/:pk',
    name: 'AccountPK',
    component: AccountPK,
    props: true,
  },
  {
    path: '/review',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/review/:pk',
    name: 'Review',
    component: Review,
    props: true,
  },
  {
    path: '/movie/:pk',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    props: true,
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
