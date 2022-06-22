import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AdminView from '../pages/admin/AdminView.vue'
import ProductList from '../pages/admin/ProductList.vue'
import MainView from '../pages/MainView.vue'
import CreateProduct from '../pages/admin/CreateProduct.vue'
import EditProduct from '../pages/admin/EditProduct.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    component: MainView,
  },
  {
    path: '/admin',
    component: AdminView,
    children: [
      {path: 'products', component: ProductList},
      {path: 'products/create', component: CreateProduct},
      {path: 'products/:id/edit', component: EditProduct}
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
