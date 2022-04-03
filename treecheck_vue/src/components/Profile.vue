<template>
  <div id="wrapper">
    <h1 class="title">
      <strong>Account</strong>
    </h1>
    <div id="content">
      <div id="info">
        <br>
        <h1 class = "bd">Hey, welcome {{ username }}! </h1>
        <h2 style="bd"><br>It's great to have you here!</h2>

        <br><br><br><br>
        <h2>
          &emsp;made with ❤️ by TreeCheck
        </h2>
      </div>
    </div>
    <div class="split right">
        <!--tree comp here-->
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
import TreeImage from '@/components/TreeImage.vue'
import router from '../router'
import Vue from 'vue';
let imgURLS = ["https://cdn.discordapp.com/attachments/959836713239314457/959981006381801492/1.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006646030416/25.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006893502464/75.PNG", 'https://cdn.discordapp.com/attachments/959836713239314457/959981007132557373/100.PNG']
//onst EventBus = new Vue();
//import Checklist from '../components/Checklist.vue'


export default {
  // todo fetch data
  name: "Profile",
  data() {
    return {
      id : 0,
      username:"",
      user_id : '',
      newTask: '',
      hideCompleted: false,
      isBusy: false,
      tasks: [],
      totalTotals: 0, //get from storage
      totalDones: 0, //get from storage
    }
  },
  components: {
    TreeImage
  },
  computed:{
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
    this.username = $cookies.get('username');
  },
    emits : ['totalDones', 'totalTotals'],
  watch: {
    totalDones(){
      this.$emit('totalDones', this.totalDones);
      
    },
    totalTotals(){
      this.$emit('totalTotals', this.totalTotals);
      
    }
  },
  methods:{
    updateTree(left, right){
      left ==='totalDone' ? this.total = right : this.curCompleted=right;
      console.log(left, right);
    }
  },
}
</script>


<style scope>
bd{
  background-color:#cbe8d6;
  text-align: left;
  font-family: 'Lora', sans-serif;
  color: #273c2d;
  font-size: 7px;
  padding: 30px;
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

/*
#info {
  display: flex;
  text-align: start;
  flex-direction: column;
  padding: 8em;
  margin-top: 5em;
}
*/
</style>