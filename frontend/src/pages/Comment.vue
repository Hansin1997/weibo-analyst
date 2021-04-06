<template>
  <q-page padding>
    <div style="margin: 0 auto; max-width: 800px">
      <q-stepper v-model="step" vertical color="primary" animated>
        <q-step
          :name="1"
          :title="$t('commentQuery')"
          icon="comment"
          :done="step > 1"
        >
          <q-form class="q-gutter-sm" @submit="process">
            <q-input v-model="id" :label="$t('commentId')" filled> </q-input>
            <q-input
              v-model="limit"
              :label="$t('commentLimit')"
              type="number"
              filled
            >
            </q-input>

            <q-stepper-navigation>
              <q-btn type="submit" color="primary" :label="$t('continue')" />
            </q-stepper-navigation>
          </q-form>
        </q-step>

        <q-step
          :name="2"
          :title="$t('commentQuering')"
          icon="computer"
          :done="step > 2"
        >
          <div class="flex flex-center">
            <q-spinner-pie color="primary" size="22em" />
          </div>
        </q-step>

        <q-step :name="3" :title="$t('commentCompleted')" icon="image">
          <div class="text-center">
            <word-cloud :rank="rank" class="full-width" />

            <word-bar
              :rank="rank"
              :label="$t('wordFrequency')"
              class="full-width"
            />

            <word-pie :neg="nlp.neg" :pos="nlp.pos" class="full-width" />
          </div>

          <q-expansion-item>
            <template slot="header">
              <q-item-section>
                {{ $t("rawResult") }}
              </q-item-section>
            </template>
            <template>
              <pre>{{ result }}</pre>
            </template>
          </q-expansion-item>

          <q-stepper-navigation class="text-right">
            <q-btn
              @click="step = 1"
              color="primary"
              :label="$t('back')"
              class="q-ml-sm"
            />
          </q-stepper-navigation>
        </q-step>
      </q-stepper>
    </div>
  </q-page>
</template>

<script lang="ts">
import WordBar from "src/components/WordBar.vue";
import WordCloud from "src/components/WordCloud.vue";
import WordPie from "src/components/WordPie.vue";
import Vue from "vue";
export default Vue.extend({
  name: "PageIndex",
  components: { WordCloud, WordBar, WordPie },
  data() {
    return {
      id: this.$route.query.id || "",
      limit: 200,
      rank: [
        ["foo", 1],
        ["bar", 0.5],
      ],
      nlp:{
        pos:0,
        neg:0
      },
      result: null,
      step: 1,
    };
  },
  methods: {
    process() {
      this.step = 2;
      this.$api
        .processCommentTask(this.id, this.limit)
        .then((res) => {
          this.result = res;
          this.rank = res.data.rank;
          this.nlp = res.data.nlp;
          this.step = 3;
        })
        .catch((e) => {
          this.step = 1;
          return Promise.reject(e);
        });
    },
  },
});
</script>
