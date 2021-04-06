<template>
  <require-authorization>
    <template v-slot="{ user, token }">
      <q-skeleton type="QAvatar" size="32px" v-if="user == null" />
      <q-btn dense flat round v-else>
        <avatar :user="user" />
        <q-menu>
          <div class="text-center q-pa-md">
            <avatar size="64" field="avatar_large" :user="user" />
            <div class="text-bold q-mt-md">{{ user.screen_name }}</div>
            <!-- <div class="text-caption">{{ user.email }}</div> -->
          </div>
          <q-list style="min-width: 150px">
            <q-separator />
            <q-item @click="logout" v-ripple clickable v-close-popup>
              <q-item-section class="text-center">
                {{ $t("logout") }}
              </q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
    </template>
    <template slot="unauthorized">
      <q-btn
        :to="{ name: 'login', params: { redirect_uri: $route.fullPath } }"
        flat
        :label="$t('login')"
      />
    </template>
  </require-authorization>
</template>

<script>
import Avatar from "./Avatar.vue";
import RequireAuthorization from "./RequireAuthorization.vue";
export default {
  components: { RequireAuthorization, Avatar },
  name: "AvatarButton",
  methods: {
    logout() {
      this.$q.localStorage.remove("token");
      this.$q.sessionStorage.remove("user");
      this.$root.$emit("onUserUpdate", null);
      this.$root.$emit("onTokenUpdate", null);
    },
  },
};
</script>

<style>
</style>