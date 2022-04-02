<script>

//<!-- <img alt="Vue logo" src="./assets/logo.png"> -->

let imgURLS = ["img1", "img2", "img3", "img4"]
import Checklist from './Checklist.vue'

export default {
  
  name: 'TreeImage',
  props(){
      total: Integer
  },
  data() {  
    return {
      curCompleted: 0,
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
      Checklist
  }
}

</script>

<template>
  <img alt="Current Tree" :src="curLink">
</template>