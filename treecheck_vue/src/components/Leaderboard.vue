<template>
  <div>
    <b-button @click="toggleBusy">Toggle Busy State</b-button>

    <b-table :items="items" :busy="isBusy" class="mt-3" outlined>
      <template #table-busy>
        <div class="text-center text-danger my-2">
          <b-spinner class="align-middle"></b-spinner>
          <strong>Loading...</strong>
        </div>
      </template>
    </b-table>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Leaderboard',
    data() {
      return {
        isBusy: false,
        trees: []
      }
    },
    components:{
    },
    methods: {
      toggleBusy() {
        this.isBusy = !this.isBusy;
      },
      getTrees() {
        axios.get('/api/v1/trees')
          .then(response => {
            this.trees = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
  }
</script>