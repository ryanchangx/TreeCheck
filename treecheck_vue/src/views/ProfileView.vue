<template>
  <div>
    <div h><Profile /></div>
    <div class="right"><img src="https://cdn.discordapp.com/attachments/959836713239314457/959981007132557373/100.PNG" class='right' height=35% width: auto></div>
  </div>
</template>

<script>
import router from '../router'
// @ is an alias to /src
import Profile from "@/components/Profile.vue";
import TreeImage from "@/components/TreeImage.vue";

export default {
  mounted(){
    if($cookies.get('loggedIn') != 'true'){
      
      $cookies.set('loggedIn', 'false');
      router.push("/login");
      alert("Please log in!")
    }
  },
  name: "ProfileView",
  components: {
    Profile,
    TreeImage,
  },
};
</script>