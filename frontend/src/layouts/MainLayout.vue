<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          <q-icon name="cloud" /> {{ $t("title") }}
        </q-toolbar-title>
        <q-btn :to="{ name: 'settings' }" flat round icon="settings" />
        <avatar-button />
      </q-toolbar>
      <q-toolbar>
        <q-tabs align="justify" no-caps>
          <q-route-tab :label="$t('index')" :to="{ name: 'index' }" />
          <q-route-tab :label="$t('comment')" :to="{ name: 'comment' }" />
          <q-route-tab disable :label="$t('person')" :to="{ name: 'person' }" />
          <q-route-tab :label="$t('settings')" :to="{ name: 'settings' }" />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from "@vue/composition-api";
import AvatarButton from "src/components/AvatarButton.vue";

export default defineComponent({
  name: "MainLayout",
  components: { AvatarButton },
  data() {
    return {
      tag: "index",
    };
  },
});
</script>
