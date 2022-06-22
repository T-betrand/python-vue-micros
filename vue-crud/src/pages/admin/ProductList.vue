<template>
  <div class="ml-5 pl-5">
    <div class="pt-3 pb-2 mb-3 border-bottom">
      <div class="btn-toolbar mb-2 mb-md-0">
        <router-link to="products/create" class="btn btn-sm btn-outline-secondary">Add</router-link>
      </div>
    </div>
    <div class="table-responsive border-right">
      <table class="table table-striped table-sm ml-5 pl-5">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Image</th>
            <th scope="col">Title</th>
            <th scope="col">Likes</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td><img :src="product.image" height="50" alt="" /></td>
            <td>{{ product.title }}</td>
            <td>{{ product.likes }}</td>
            <td>
              <div class="btn-group mr-2">
                <a
                  href="#"
                  class="btn btn-sm btn-outline-secondary"
                  @click="del(product.id)"
                  >Delete</a
                >
                <router-link :to="`/admin/products/${product.id}/edit`" class="btn btn-sm btn-outline-secondary">Edit</router-link>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";

import { Product } from "../../interfaces/product";

export default {
  name: "ProductList",

  setup() {
    const products = ref([]);

    onMounted(async () => {
      const response = await fetch("http://0.0.0.0:8000/api/products");
      products.value = await response.json();
    });

    const del = async (id: number) => {
      if (confirm("Are you sure you want to delete this product")) {
        await fetch(`http://0.0.0.0:8000/api/products/${id}`, {
          method: "DELETE",
        });

        products.value = products.value.filter((p: Product) => p.id !== id);
      }
    };

    return {
      products,
      del,
    };
  },
};
</script>
