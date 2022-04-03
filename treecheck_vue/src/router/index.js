import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Leaderboard from '../components/Leaderboard.vue'
import ProfileView from '../views/ProfileView.vue'
import ChecklistView from '../views/ChecklistView.vue'
import { LayoutPlugin } from 'bootstrap-vue'
import LoginView from '../views/LoginView.vue'
import FriendView from '../views/FriendView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/leaderboard',
    name: 'leaderboard',
    component: Leaderboard
  },
  {
    path: '/account',
    name: 'account',
    component: ProfileView
  },
  {
    path: '/checklist',
    name: 'checklist',
    component: ChecklistView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/friend/?id=:id',
    name: 'friend',
    component: FriendView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
