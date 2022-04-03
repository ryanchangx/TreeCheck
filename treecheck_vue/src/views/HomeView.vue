<template>
  <div class="home">
    <div id="wrapper">
      <router-link to="/" class="navbar-item"><img alt="Vue logo" src="../assets/logo.png" ></router-link>
      <!-- replace with logo image later-->
      <h1 class= "title">Tree Check</h1>
      <br>
      <h2 class= "mid"> About tree check zzz Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi suscipit quibusdam doloremque pariatur neque facilis laborum odit accusamus, velit perspiciatis tenetur dignissimos voluptatum sed reprehenderit excepturi nobis? Cum, nemo eaque.</h2>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'  
import MenuBurger from '@/components/MenuBurger.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    MenuBurger
  }
}
</script>

<style scoped>
.title{
  color:	#3b8570;
  font-family: 'Shrikhand', cursive;
  font-size: 70px;
  text-align: center;
}

</style>

<style scoped>
.mid{
  padding: 0px;
}
</style>

<style>
body {
  background-color:#cbe8d6;
  text-align: center;
  font-family: 'Lora', sans-serif;
  color: #273c2d;
  font-size: 10px;
  padding: 30px;
}

</style>