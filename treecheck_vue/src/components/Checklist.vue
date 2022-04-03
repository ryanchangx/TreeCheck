


<template>
<div id="wrapper">
  <form @submit.prevent="addTask">
    <input v-model="newTask" />
    <button>Add Task</button>
  </form>
  <ul>
    <li v-for="task in tasks" :key="task.id">
      <input type="checkbox" v-model="task.task_status">
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
      tasks: []
    }
  },
  components: {
  },
  mounted() {
    this.getTasks();
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
      this.newTask = ''
    },
    removeTask(tasks) {
      this.tasks = this.tasks.filter((t) => t !== tasks)
    },
    toggleBusy() {
      this.isBusy = !this.isBusy;
    },
  }
}
  
</script>