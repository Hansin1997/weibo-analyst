<template>
  <q-page padding>
    <div class="text-h5 q-mb-sm">
      <q-btn @click="() => $router.back()" flat icon="arrow_back" round />
      {{ $t("settings") }}
    </div>
    <q-separator />
    <div class="setting">
      <div class="q-mt-sm q-mb-sm q-gutter-sm">
        <div>
          <div class="text-h6">
            <q-icon name="settings" /><span>{{ $t("oauth") }}</span>
          </div>
          <div class="q-gutter-sm q-pa-md">
            <q-input filled v-model="model.client_id" :label="$t('clientId')" />
            <q-input
              filled
              v-model="model.client_secret"
              :label="$t('clientSecret')"
            />
            <q-input
              filled
              v-model="model.redirect_uri"
              :label="$t('redirectUri')"
            />
          </div>
        </div>

        <div>
          <div class="text-h6">
            <q-icon name="settings" /><span>{{ $t("style") }}</span>
          </div>
          <div class="q-gutter-sm q-pa-md">
            <word-cloud
              style="width: 100%"
              :rank="[
                ['Hello Word', 1],
                ['Python', 0.5],
                ['Java', 0.7],
                ['C++', 0.5],
                ['PHP', 0.2],
                ['Java Script', 0.5],
              ]"
            />
            <q-input filled v-model="model.bgColor" :label="$t('bgColor')">
              <template v-slot:append>
                <q-icon name="colorize" class="cursor-pointer">
                  <q-popup-proxy
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-color v-model="model.bgColor" />
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>

            <q-input filled v-model="model.tColor" :label="$t('tColor')">
              <template v-slot:append>
                <q-icon name="colorize" class="cursor-pointer">
                  <q-popup-proxy
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-color v-model="model.tColor" />
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>

            <q-input filled v-model="model.hlColor" :label="$t('hlColor')">
              <template v-slot:append>
                <q-icon name="colorize" class="cursor-pointer">
                  <q-popup-proxy
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-color v-model="model.hlColor" />
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
          </div>
        </div>
      </div>
      <div class="row q-mt-sm q-mb-sm">
        <q-space />
        <q-btn @click="save" color="primary" :label="$t('save')" />
      </div>
    </div>
  </q-page>
</template>

<script>
import WordCloud from "src/components/WordCloud.vue";
export default {
  components: { WordCloud },
  name: "Settings",
  data() {
    return {
      model: {
        client_id: null,
        client_secret: null,
        redirect_uri: "http://127.0.0.1:8080/login",
        bgColor: "#ffe0e0",
        hlColor: "#f02222",
        tColor: "#c09292",
      },
    };
  },
  methods: {
    load() {
      for (let i in this.model) {
        let val = this.$q.localStorage.getItem(i);
        if (val) this.model[i] = val;
      }
    },
    save() {
      for (let i in this.model) this.$q.localStorage.set(i, this.model[i]);
    },
  },
  mounted() {
    this.load();
  },
  watch: {
    "model.bgColor"(a, b) {
      if (a == b) return;
      this.$root.$emit("onStyleChange", "bgColor", this.model.bgColor);
    },
    "model.tColor"(a, b) {
      if (a == b) return;
      this.$root.$emit("onStyleChange", "tColor", this.model.tColor);
    },
    "model.hlColor"(a, b) {
      if (a == b) return;
      this.$root.$emit("onStyleChange", "hlColor", this.model.hlColor);
    },
  },
};
</script>

<style scoped>
.setting {
  max-width: 600px;
  margin: 0 auto;
}
</style>