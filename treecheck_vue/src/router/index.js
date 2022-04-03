import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Leaderboard from '../components/Leaderboard.vue'
import Profile from '../components/Profile.vue'
import ChecklistView from '../views/ChecklistView.vue'


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
    component: Profile
  },
  {
    path: '/checklist',
    name: 'checklist',
    component: ChecklistView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
