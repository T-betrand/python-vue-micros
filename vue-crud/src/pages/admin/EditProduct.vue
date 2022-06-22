<template>
    <form @submit.prevent="edit" class="container-fluid ml-5 pl-5">
        <div class="form-group">
            <label>Title</label>
            <input v-model="title" name="title" class="form-control">
        </div>
        <div class="form-group">
            <label>Image</label>
            <input v-model="image" name="image" class="form-control">
        </div>
        <button class="btn btn-outline-secondary">Update</button>
    </form>
</template>

<script>

import {ref, onMounted} from "vue"
import {useRoute, useRouter} from "vue-router";

export default {
    name: "EditProduct",

    setup(){
        const title = ref('');
        const image = ref('');
        const router = useRouter();
        const route = useRoute();

        onMounted(async () => {
            const response = await fetch(`http://0.0.0.0:8000/api/products/${route.params.id}`);

            const product = await response.json();

            title.value = product.title;
            image.value = product.image;
        });


        const edit = async () => {
            await fetch(`http://0.0.0.0:8000/api/products/${route.params.id}`, {
                method: 'PUT',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({
                    title: title.value,
                    image: image.value,
                })
            });

            await router.push('/admin/products');
        }


        return {
            title,
            image,
            edit
        }
    }
}
</script>
