<template>
  <div>
      <NavBar/>
    <div class="container-fluid">
      <div class="row">
          <MenuSide />

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 container-fluid">
            <!-- changes component based on the route -->
            <router-view/> 
        </main>
      </div>
    </div>
  </div>
</template>



<script>
import NavBar from "@/components/NavBar.vue"
import MenuSide from "@/components/MenuSide.vue"

export default {
  name: "AdminView",

  components: {
      NavBar,
      MenuSide,
  }
};
</script>
