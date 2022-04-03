<template>
  <div>
    <Profile />
    <TreeImage />
  </div>
</template>

<script>
// @ is an alias to /src
import Profile from "@/components/Profile.vue";
import TreeImage from "@/components/TreeImage.vue";

export default {
  name: "ProfileView",
  components: {
    Profile,
    TreeImage,
  },
};
</script>