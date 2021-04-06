<template>
  <div>
    <q-avatar :size="computedSize" v-if="user">
      <q-img :width="computedSize" :height="computedSize" :src="user[avatarField]" />
    </q-avatar>
  </div>
</template>

<script>
import RequireAuthorization from "./RequireAuthorization.vue";
export default {
  name: "Avatar",
  props: {
    size: String,
    field: String,
    user: Object,
  },
  components: { RequireAuthorization },
  computed: {
    computedSize() {
      return (this.size ? this.size : "32") + "px";
    },
    avatarField() {
      return this.field ? this.field : "profile_image_url";
    },
  },
};
</script>

<style scoped>
</style>