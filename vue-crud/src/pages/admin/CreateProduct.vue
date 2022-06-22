<template>
    <form @submit.prevent="submit" class="container-fluid ml-5 pl-5">
        <div class="form-group">
            <label>Title</label>
            <input v-model="title" name="title" class="form-control">
        </div>
        <div class="form-group">
            <label>Image</label>
            <input v-model="image" name="image" class="form-control">
        </div>
        <button class="btn btn-outline-secondary">Save</button>
    </form>
</template>

<script>

import {ref} from "vue"
import {useRouter} from "vue-router";

export default {
    name: "CreateProduct",

    setup(){
        const title = ref('');
        const image = ref('');
        const router = useRouter();

        const submit = async () => {
            await fetch('http://0.0.0.0:8000/api/products', {
                method: 'POST',
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
            submit
        }
    }
}
</script>
