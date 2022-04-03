


<template>
<div id="wrapper">
  <form @submit.prevent="addTask">
    <input v-model="newTask" />
    <button>Add Task</button>
    
  </form>
  <ul>
    <li v-for="task in tasks" :key="task.id">
      <input type="checkbox" v-model="task.task_status" @click="!task.task_status ? totalDones++ : totalDones--"> <!--this shits switched bc tastk_status is delayed-->
      <span :class="{done: task.task_status}">{{ task.task_name }}</span>
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
let id = 0;

export default {
  name: 'Checklist',
  data() {
    return {
      newTask: '',
      hideCompleted: false,
      isBusy: false,
      tasks: [],
      totalTotals: 0, //get from storage
      totalDones: 0, //get from storage
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
      axios.get('/api/v1/tasks-list')
        .then(response => {
          this.tasks = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addTask() {
      this.tasks.push({ id: id++, text: this.newTask, done: false })
      this.newTask = '';
      this.totalTotals++;
    },
    removeTask(tasks) {
      if(tasks.task_status === true){
        this.totalDones--;
      }
      this.tasks = this.tasks.filter((t) => t !== tasks)
      this.totalTotals--;
    },
    toggleBusy() {
      this.isBusy = !this.isBusy;
    },
  }
}
  
</script>