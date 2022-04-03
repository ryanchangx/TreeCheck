<template>
  <div id="wrapper">
    <h1 class="text-white">
      <strong>MY PROFILE</strong>
    </h1>
    <div id="content">
      <div id="info">
        <h1>HEY <u style="text-transform:uppercase;">{{ name }}</u>!</h1>
        <h2 style="margin-top: 1em">Info:</h2>
        <h2>
          &emsp;username = <u>{{ username }}</u>
        </h2>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  font-family: cursive;
  color: white;
}

#info {
  display: flex;
  text-align: start;
  flex-direction: column;
  padding: 8em;
  margin-top: 5em;
}
</style>

<script>
export default {
  // todo fetch data
  name: "Profile",
  data() {
    return {
      name: "Joe",
      username: "bobbytherossdog",
      userID: 1,
    };
  },
};
</script>