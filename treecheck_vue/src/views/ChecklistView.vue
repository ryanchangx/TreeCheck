<template>
  <div class="home">
    <div id="wrapper">
      <h1> MY LIST </h1>
      <div class="lb-container">
          <Checklist></Checklist>
      </div>
      <div class="tree-container">
        <!--tree comp here-->
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Checklist from '@/components/Checklist.vue'  
import Vue from 'vue';
//onst EventBus = new Vue();
//import Checklist from '../components/Checklist.vue'

export default {
  name: 'ChecklistView',
  components: {
    Checklist,
  }
}
</script>


<style>
body {
  background-color:#cbe8d6;
  text-align: center;
}

</style>