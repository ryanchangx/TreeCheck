<script>

//<!-- <img alt="Vue logo" src="./assets/logo.png"> -->

let imgURLS = ["img1", "img2", "img3", "img4"]
import Checklist from './Checklist.vue'

export default {
  
  name: 'TreeImage',
  props:{
      totalPass: Number,
      curCompletedPass: Number
  },
  data() {  
    return {
      total: this.totalPass,
      curCompleted: this.curCompletedPass,
      curLink: imgURLS[0],
    }
  },
  methods: {
      updateTree(){
          let status = this.curCompleted/this.total;
          this.curLink = imgURLS[Math.floor(status*imgURLS.length)];
      }
    },
  components: {
      Checklist,
  }
}

</script>

<template>
  <img alt="Current Tree" :src="curLink">

</template>