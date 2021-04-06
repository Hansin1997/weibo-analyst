<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <q-page> </q-page>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import Vue from "vue";
import qs from "querystring";
import { v1 } from "uuid";
import { AccessToken } from "src/sdk/Model";
export default Vue.extend({
  name: "Login",
  data() {
    return {};
  },
  methods: {
    validateState(val: string) {
      let state = this.$q.localStorage.getItem("state");
      if (state == null || val == null) return false;
      return val == state;
    },
    generateState() {
      let uuid = v1();
      this.$q.localStorage.set("state", uuid);
      return uuid;
    },
    removeState() {
      this.$q.localStorage.remove("state");
    },
    connect() {
      let r = <string>this.$q.localStorage.getItem("redirect_uri");
      let cid = <string>this.$q.localStorage.getItem("client_id");
      let query = qs.stringify({
        redirect_uri: r ? r : "http://127.0.0.1:8080/login",
        client_id: cid,
        response_type: "code",
        state: this.generateState(),
      });
      location.replace("https://api.weibo.com/oauth2/authorize?" + query);
    },
    callback(response: { state: string; code: string }) {
      if (this.validateState(response.state)) {
        let r = <string>this.$q.localStorage.getItem("redirect_uri");
        let cid = <string>this.$q.localStorage.getItem("client_id");
        let cst = <string>this.$q.localStorage.getItem("client_secret");
        if (response.code)
          this.$api
            .getToken(
              response.code,
              r ? r : "http://127.0.0.1:8080/login",
              cid,
              cst
            )
            .then((token) => this.onConnectSuccess(token))
            .catch(this.onConnectFail);
        else this.onConnectFail(new Error("Login failed, Token invalid"));
      } else this.onConnectFail(new Error("Uninitialized"));
    },
    onConnectSuccess(token: AccessToken) {
      this.removeState();
      let redirect = <string>this.$route.query.redirect_uri;
      this.$router.replace(redirect ? { path: redirect } : { name: "index" });
    },
    onConnectFail(e: Error) {
      throw e;
    },
  },
  mounted() {
    let response = this.$route.query.code
      ? {
          code: <string>this.$route.query.code,
          state: <string>this.$route.query.state,
        }
      : null;
    if (response != null) {
      this.callback(response);
    } else {
      this.connect();
    }
  },
});
</script>