<template>
<div class="split left">
  <div class="centered">
    <div id="wrapper">
  <form @submit.prevent="addTask">
    <input v-model="newTask" />
    <button>Add Task</button>
    
  </form>
  <ul>
    <li v-for="task in tasks" :key="task.id">
      <input type="checkbox" v-model="task.task_status" @click="!task.task_status ? totalDones++ : totalDones--"> <!--this shits switched bc tastk_status is delayed-->
      <span :class="{done: task.task_status}">{{ task.text }}</span>
      <button @click="removeTask(task)">Remove Task</button>
    </li>
  </ul>
  </div>
  </div>



</div>
</template>


<style>
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
  padding-top: 20px;
}
/* Control the left side */
.left {
  position: fixed;
  top: 25vh;
  height: 50vh;
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
  text-align: center;
  margin: 30px;
  border-radius: 10px;
  display: grid;
  /*grid-template-columns: 30px 1fr;*/
  grid-template-rows: 20px 40px ;
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

</style>



<script>
// http://128.199.5.103:8181/api/v1/tasks-list
/*
  example object:
  [
    {
        "id": 1,
        "user_id": 2,
        "task_name": "win citrus hack",
        "task_description": "be better at coding",
        "task_status": false
    }
  ]
*/
import axios from 'axios';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
let head = {
  'Access-Control-Allow-Headers': '*',
  
}
export default {
  name: 'Checklist',
  data() {
    return {
      id : 0,
      newTask: '',
      hideCompleted: false,
      isBusy: false,
      tasks: [],
      totalTotals: 0, //get from storage
      totalDones: 0, //get from storage
      recentDelete: "",
    }
  },
  components: {
  },
  mounted() {
    this.getTasks(); //change to get from api
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
  methods: {
    getTasks() {
      fetch('http://128.199.5.103:8181/api/v1/usertasklist/1').then(function(response) {
        return response.json();
        
      }).then((data) => data.forEach(task=>{ 
        this.id = task.id;
        this.addTasks(task.task_name)
      }
        ));
      },
    addTask() {
      this.tasks.push({ id: this.id++, text: this.newTask, done: false })
      let dataa = {task_name: this.newTask}
      this.totalTotals++;
      fetch('http://128.199.5.103:8181/api/v1/addtask/'+'1/',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dataa)
      }).then((data) => console.log(data))
      this.newTask = '';
    },
    addTasks(taskText) {
      this.tasks.push({ id: this.id++, text: taskText, done: false })
      this.totalTotals++;
    },
    removeTask(tasks) {
      let temp = tasks.text;
      if(tasks.task_status === true){
        this.totalDones--;
      }
      this.tasks = this.tasks.filter((t) => t !== tasks)
      this.totalTotals--;
      let dataa = {task_name: temp}
      fetch('http://128.199.5.103:8181/api/v1/deletetask/'+'1/',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dataa)
      }).then((data) => console.log(data))
    },
    toggleBusy() {
      this.isBusy = !this.isBusy;
    },
  }
}
  
</script>