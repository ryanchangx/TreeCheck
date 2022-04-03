<template>
  <div class="home">
    <div id="wrapper">
      <router-link to="/" class="logo"><img alt="Vue logo" width=20 height=10 src="https://cdn.discordapp.com/attachments/959836713239314457/959981007132557373/100.PNG" ></router-link>
      <br>
      <!-- replace with logo image later-->
      <h1 class= "title">Tree Check</h1>
      <br>
      <h2 class= "mid"> Welcome to Tree Check! This is the future of productivity.</h2>
      <br>
      <h4>The purpose of this site is to motivate you to work towards finishing all of the tasks on your task list!

          Feel free to invite your friends, and add them to compete!
        <br>
        <br>

        As you finish all of your tasks, your personal tree will grow and flourish! You can check out the progress of your friends at  at the leaderboard section!

        <br>
        <br>
        Good luck with your tasks, and remember: <b>Lets grow together!</b>
      </h4>

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

<style>
.logo img{
  height: 160px;
  width: auto;
}

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