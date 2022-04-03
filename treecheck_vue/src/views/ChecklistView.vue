<template>
  <div class="home">
    <div id="wrapper">
      CURRENT TOTAL {{total}}
      CURRENT STUFF {{curCompleted}}
      <h1 class="title"> My List </h1>
      <div class="lb-container">
          <Checklist @totalDones="msg => curCompleted=msg" @totalTotals="msg => total=msg" :curCompletedPass="curCompleted"></Checklist>
      </div>
      <div class="split right">
        <div class="centered">
          <div id= "wrapper">
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
import Checklist from '@/components/Checklist.vue'  
import TreeImage from '@/components/TreeImage.vue'
import Vue from 'vue';
let imgURLS = ["https://cdn.discordapp.com/attachments/959836713239314457/959981006381801492/1.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006646030416/25.PNG", "https://cdn.discordapp.com/attachments/959836713239314457/959981006893502464/75.PNG", 'https://cdn.discordapp.com/attachments/959836713239314457/959981007132557373/100.PNG']
//onst EventBus = new Vue();
//import Checklist from '../components/Checklist.vue'

export default {
  name: 'ChecklistView',
  data(){
    return{
      total : 0,
      curCompleted : 0,
      image : imgURLS[0],
      filler : imgURLS[0]
    }
  },
  components: {
    Checklist,
    TreeImage,
  },
  computed: {
    changeImage(){
      return imgURLS[Math.floor(this.curCompleted/this.total*imgURLS.length)-1];
    }
  },
  mounted(){
    //set totalPass and curCompletedPass according to API
  },
  methods:{
    updateTree(left, right){
      left ==='totalDone' ? this.total = right : this.curCompleted=right;
      console.log(left, right);
    }
  },
}
</script>

<style>
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
  position: fixed;
  top: 15vh;
  height: 70vh;
  right: 5vw;
  width: 50vw;
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
  transform: translate(15%, 0%);
  text-align: center;
  height: 100%;
  width: auto;
  /* height: auto; */
}


</style>