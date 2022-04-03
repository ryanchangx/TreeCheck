<template>
<div class="split left">
  <div class="centered">
    <div id="wrapper">
        <ul>
            <li v-for="task in tasks" :key="task.id">
            <input type="checkbox" v-model="task.task_status">
            <span :class="{done: task.task_status}">{{ task.text }}</span>
            </li>
        </ul>
  </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'FriendCheck',
  data() {
    return {
      user_id : 0,
      username : '',
      newTask: '',
      hideCompleted: false,
      isBusy: false,
      tasks: [],
      recentDelete: "",
    }
  },
  components: {
  },
  mounted() {
    //change to get from api
    this.user_id = new URL(location.href).searchParams.get('id')
    this.getTasks();
  },
  methods: {
    getTasks() {
      fetch('http://128.199.5.103:8181/api/v1/user-profile/' + this.user_id + '/').then(function(response) {
        return response.json();
      }).then((data) => { 
        this.tasks = response.data["tasks"];
        this.username = response.data["user"];
        }
        );
      },
  }
}
  
</script>
<style>
form input{
  height: 30px;
  background-color: white;
  color: #3b8570;
  font-family: 'Shrikhand', cursive;
  font-size: 20px;
  text-align: center;
  margin: 30px;
  border-radius: 10px;
  border-color: white;
  /*grid-template-columns: 30px 1fr;*/
  letter-spacing: .5px;
  /*column-gap: 20px;*/
}

form button{
  border-radius: 10px;
  border-color: rgba(255, 255, 255, 0);
  background-color: white;
  color: #3b8570;
  font-size: 10px;
  text-align: center;
  margin: 0px;
  font-family: 'Shrikhand', cursive;
  font-size: 20px;
  transform: 15px;
  letter-spacing: .5px;
}
form button:hover{
  background-color: #f1fefb;
}

.done {
  text-decoration: line-through;
}
.split {
  height: 100%;
  /* width: 100%; */
  position: fixed;
  z-index: 1;
  top: 0;
  /* overflow-x: hidden; */
  overflow-y: scroll;
  overflow-y: scroll;
}
/* Control the left side */
.left {
  background: rgba(255, 255, 255, 0.294);
  position: fixed;
  top: 30vh;
  height: 60vh;
  left: 5vw;
  width: 50vw;
}
/* If you want the content centered horizontally and vertically */
.centered {
  
  padding: 20px;
  /* position: absolute; */
  /* top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); */
  text-align: center;
}
/* Style the image inside the centered container, if needed */
.centered img {
  width: 200px;
  border-radius: 50%;
}
/* .add {
  position: fixed;
  top: 30vh;
  left: 20vw;
  height: 20px;
  width: 50px;
  background-color: green;
} */
ul {
  padding: 0;
}
li {
  height: 70px;
  background-color: #3b8570;
  color: white;
  font-family: 'Shrikhand', cursive;
  font-size: 30px;
  top: 10px;

  text-align: center;
  margin: 30px;
  border-radius: 10px;
  display: grid;
  /*grid-template-columns: 30px 1fr;*/
  grid-template-rows: 20px 40px ;
  letter-spacing: .5px;
  /*column-gap: 20px;*/

}
.remove {
  /* grid-row: 1 / 3;
  grid-column: 1 / 2; */
  background-color: rgba(255, 255, 255, 0);
  padding: 10px;
  border-color: rgba(255, 255, 255, 0);
  
  /* border-width: 4px;
  border-color: black;*/
  /*border-style: dotted;*/
  /* 
  
  */
  border-radius: 10px; 
  width: 50px;
  /* border-bottom-left-radius: 30px;
  box-shadow: 5px 30px 2px 10px purple; */
  /*box-shadow: 0px 0px 5px 1px #151515;*/
  /*filter: blur(5px);*/
  font-size: 20px;
  /*transition: width 500ms, filter 500ms, background-color 350ms, box-shadow 3s 2s, border-bottom-right-radius 3s;*/
}
.remove:hover {
  background-color: #74b6a3;
 /* filter: blur(0px);
  border-style: solid; */
  /*border-bottom-right-radius: 40px;
  box-shadow: 0px 0px 5px 1px #f0f;*/
}

li input{
  width: 50px;
  height:50px;
}


li button {
    background-color: 	#3b8570;
    font-size: 50%;
    border-color: #3b857000;
    text-align: right;
    color: rgba(255, 255, 255, 0.617);
    letter-spacing: .5px;
}

li button:hover {
    background-color: 	#377664;
    font-size: 50%;
    border-color: #3b857000;
    text-align: right;
    color: rgba(255, 255, 255, 0.617);
    letter-spacing: .5px;
}

</style>