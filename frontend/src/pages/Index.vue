<template>
  <q-page padding>
    <q-list separator>
      <q-item
        v-for="(item, index) in data"
        :key="index"
        clickable
        :to="{ name: 'comment', query: { id: item.id } }"
      >
        <q-item-section avatar>
          <avatar :user="item.user" />
        </q-item-section>
        <q-item-section>
          <q-item-label>{{ item.user.screen_name }}</q-item-label>
          <q-item-label caption>{{ item.text }}</q-item-label>
          <q-item-label caption>
            <q-icon name="comment" />
            <span>
              {{ item.comments_count }}
            </span>
          </q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-icon name="keyboard_arrow_right" />
        </q-item-section>
      </q-item>
      <q-item v-if="loading">
        <q-space />
        <q-spinner-puff color="primary" size="4em" />
        <q-space />
      </q-item>
      <q-item v-else-if="hasMore">
        <q-space />
        <q-btn flat color="primary" :label="$t('loadMore')" @click="loadMore" />
        <q-space />
      </q-item>
    </q-list>
  </q-page>
</template>

<script lang="ts">
import Avatar from "src/components/Avatar.vue";
import Vue from "vue";
export default Vue.extend({
  components: { Avatar },
  name: "Comment",
  data() {
    return {
      loading: false,
      page: 1,
      res: null,
      data: [],
      hasMore: true,
    };
  },
  methods: {
    loadMore() {
      if (this.loading) return;
      this.loading = true;
      this.$api
        .getTimeline(this.page)
        .then((res) => {
          this.res = res;
          this.data = this.data.concat(res.statuses);
          this.page++;
          if (res.statuses == null || res.statuses.length == 0)
            this.hasMore = false;
        })
        .finally(() => (this.loading = false));
    },
  },
  mounted() {
    this.loadMore();
  },
});
</script>
