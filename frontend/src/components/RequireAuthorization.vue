<template>
  <div>
    <slot v-bind="{ user, token }" v-if="authorized" />
    <slot name="unauthorized" v-else> 😢 Unauthorized </slot>
  </div>
</template>
<script lang="ts">
import { AccessToken } from "src/sdk/Model";
import Vue from "vue";
let lock = false;
export default Vue.extend({
  name: "RequireAuthorization",

  data() {
    return {
      user: null,
      token: null,
    };
  },
  methods: {
    onTokenUpdate(token: AccessToken) {
      this.token = token;
      if (lock || !token) return;
      lock = true;
      this.$api
        .getUser()
        .then((user) => {
          this.$root.$emit("onUserUpdate", user);
        })
        .catch((e) => {
          this.$q.localStorage.remove("token");
          this.$q.sessionStorage.remove("user");
          this.$root.$emit("onTokenUpdate", null);
          this.$root.$emit("onUserUpdate", null);
          return Promise.reject(e);
        })
        .finally(() => (lock = false));
    },
    onUserLoaded(user: any) {
      this.user = user;
    },
  },
  computed: {
    authorized() {
      return this.token != null;
    },
  },
  mounted() {
    this.$root.$on("onTokenUpdate", this.onTokenUpdate);
    this.$root.$on("onUserUpdate", this.onUserLoaded);
    if (this.$q.localStorage.has("token")) {
      let t = <AccessToken>this.$q.localStorage.getItem("token");
      if (t.expired_at != undefined && new Date() > t.expired_at) {
        this.$q.localStorage.remove("token");
        this.$q.sessionStorage.remove("user");
        this.$root.$emit("onTokenUpdate", null);
        this.$root.$emit("onUserUpdate", null);
        return;
      }
      this.onTokenUpdate(t);
      this.onUserLoaded(this.$q.sessionStorage.getItem("user"));
    }
  },
});
</script>