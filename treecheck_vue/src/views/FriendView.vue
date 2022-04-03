<template>
  <div class="home">
    <div id="wrapper">
      <h1 class="title"> My List </h1>
      <div class="lb-container">
          <FriendCheck @totalDones="msg => curCompleted=msg" @totalTotals="msg => total=msg" :curCompletedPass="curCompleted"></FriendCheck>
      </div>
      <div class="split right">
        <div class="centered">
          <div id= "wrapper">
            <!-- <b1 class= "growthprog">Today's Growth:</b1> -->
          <!-- {{changeImage||filler}} -->
        <!-- <TreeImage :totalPass="total" :curCompletedPass="curCompleted"></TreeImage> -->
         <!-- <img alt="Vue logo" src="./1.png" > -->
         <img :src='changeImage||filler'>
         </div>
        <!--tree comp here-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import FriendCheck from '@/components/FriendCheck.vue'  
import TreeImage from '@/components/TreeImage.vue'
import router from '../router'
import Vue from 'vue';
let imgURLS = ["https://cdn.discordapp.com/attachments/959836713239314457/959981006381801492/1.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006646030416/25.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006893502464/75.PNG", 'https://cdn.discordapp.com/attachments/959836713239314457/959981007132557373/100.PNG']
//onst EventBus = new Vue();
//import Checklist from '../components/Checklist.vue'

export default {
  name: 'FriendView',
  data(){
    let user_id = new URLSearchParams(window.location.search);
    return{
      total : 0,
      curCompleted : 0,
      image : imgURLS[0],
      filler : imgURLS[0],
      userID : user_id,
    }
  },
  components: {
    FriendCheck,
    TreeImage,
  },
  computed: {
    changeImage(){
      return imgURLS[Math.floor(this.curCompleted/this.total*imgURLS.length)-1];
    }
  },
  mounted(){
    if($cookies.get('loggedIn') != 'true'){
      $cookies.set('loggedIn', 'false');
      router.push("/login");
      alert("please log in!")
    }
    this.userID = $cookies.get('userID');
  },
  methods:{
  },
}
</script>

<style scope>
.growthprog{
  color:	#3b8570;
  font-family: 'Shrikhand', cursive;
  font-size: 30px;
  text-align: center;
  top: 10vh;
  letter-spacing: .5;
}

body {
  background-color:#cbe8d6;
  text-align: center;
}

.split {
  
  /* width: 100%; */
  position: fixed;
  z-index: 1;
  /* overflow-x: hidden; */
  overflow-y: hide;
  padding-top: 20px;
}

/* Control the right side */
.right {
  background: rgba(255, 255, 255, 0.294);
  position: fixed;
  top: 30vh;
  height: 60vh;
  right: 5vw;
  width: 40vw;
}

/* If you want the content centered horizontally and vertically */
.centered {
  height: 100%;
  padding: 20px;
  /* position: absolute; */
  /* top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); */
  text-align: center;
}
#wrapper {
  height: 100%;
}

/* Style the image inside the centered container, if needed */
.centered img {
  transform: translate(-5%, 0%);
  text-align: center;
  height: 90%;
  width: auto;
  /* height: auto; */
}


</style>