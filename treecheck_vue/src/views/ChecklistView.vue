<template>
  <div class="home">
    <div id="wrapper">
      CURRENT TOTAL {{total}}
      CURRENT STUFF {{curCompleted}}
      <h1> MY LIST </h1>
      <div class="lb-container">
          <Checklist @totalDones="msg => curCompleted=msg" @totalTotals="msg => total=msg" :curCompletedPass="curCompleted"></Checklist>
      </div>
      <div class="tree-container">
        <!-- <TreeImage :totalPass="total" :curCompletedPass="curCompleted"></TreeImage> -->
        IMMAGE: {{changeImage || filler}}
        <!--tree comp here-->
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Checklist from '@/components/Checklist.vue'  
import TreeImage from '@/components/TreeImage.vue'
import Vue from 'vue';
let imgURLS = ["img1", "img2", "img3", "img4"]
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

</style>