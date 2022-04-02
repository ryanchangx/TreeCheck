<template>
  <b-container fluid>
    <h1 class="text-white">
      <strong>MY PROFILE</strong>
    </h1>
    <span class="h1" id="greeting">HEY <u>NAME</u>!<span>
  </b-container>
</template>

<style scoped>
* {
  border: 1px solid #000000;
  font-family: cursive;
  color: white;
}

#greeting {
  left: 0;
}
</style>

<script>
export default {
  name: "Profile",
};
</script>