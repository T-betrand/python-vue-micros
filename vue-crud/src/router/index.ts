import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AdminView from '../pages/admin/AdminView.vue'
import ProductList from '../pages/admin/ProductList.vue'
import MainView from '../pages/MainView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: MainView,
  },
  {
    path: '/admin',
    component: AdminView,
    children: [
      {path: '/products', component: ProductList}
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
