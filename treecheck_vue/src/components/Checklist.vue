


<template>
<div id="wrapper">
  <form @submit.prevent="addTask">
    <input v-model="newTask" />
    <button>Add Task</button>
    
  </form>
  <ul>
    <li v-for="task in tasks" :key="task.id">
      <input type="checkbox" v-model="task.task_status" @click="!task.task_status ? totalDones++ : totalDones--"> <!--this shits switched bc tastk_status is delayed-->
      <span :class="{done: task.task_status}">{{ task.text }}</span>
      <button @click="removeTask(task)">X</button>
    </li>
  </ul>
  </div>
</template>

<style>
.done {
  text-decoration: line-through;
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
      // axios.get('/api/v1/tasks-list/' + '1', {headers: head})
      //   .then(response => {
      //     this.tasks = response.data;
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   });

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