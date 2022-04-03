<template>
  <div class="home">
    <div id="wrapper">
      <h1 class="title"> Leaderboard </h1>
      <ul>
        <li v-for="tree in trees" :key="tree.id">
            <h3 class="user">{{ tree.username }} </h3>
            <h4 class="level">{{ tree.treelevel }} </h4>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Leaderboard',
    data() {
      return {
        isBusy: false,
        trees: [],
      }
    },
    components:{
    },
    mounted(){
      this.getTrees();
    },
    methods: {
      toggleBusy() {
        this.isBusy = !this.isBusy;
      },
      getTrees() {
        fetch('http://128.199.5.103:8181/api/v1/leaderboard-data/').then(function(response) {
          return response.json();
         })
        .then(response => {
          //alert(JSON.stringify(response))
          this.trees = response;
        })
        // .catch(error => {
        //   console.log(error);
        // });
      },
    },
  }
</script>

<style>
li h3{
  
  height: 70px;
  background-color: #3b857000;
  color: white;
  font-family: 'Shrikhand', cursive;
  font-size: 30px;
  text-align: center;
  margin: 14px;
  display: grid;
  grid-template-columns: 30px 1fr;
  border-radius: 10px;
  /*grid-template-columns: 30px 1fr;*/
  letter-spacing: .5px;
  left: 100px;
  /*column-gap: 20px;*/

}
li h4{
  margin-right: 13px;
  text-align: right;
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