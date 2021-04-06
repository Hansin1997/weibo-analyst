<template>
  <canvas ref="chart" width="1462.5" height="1462"></canvas>
</template>

<script>
import wc from "wordcloud";

export default {
  name: "WordCloud",
  props: {
    rank: Array,
  },
  data() {
    return {
      chart: null,
      style: {
        bgColor: "#ffe0e0",
        hlColor: "#f02222",
        tColor: "#c09292",
      },
    };
  },
  methods: {
    initialize(rank) {
      let cvs = this.$refs.chart;
      let width = cvs.clientWidth;
      let screenWidth = this.$q.screen.width;
      let style = this.style;
      this.chart = wc(cvs, {
        gridSize: Math.round((16 * width) / 512),
        weightFactor: function (size) {
          return (Math.pow(size * 70, 1.3) * width) / 512;
        },
        fontFamily: "Times, serif",
        color: function (word, weight) {
          return weight === 1
            ? style.hlColor
              ? style.hlColor
              : "#f02222"
            : style.tColor
            ? style.tColor
            : "#c09292";
        },
        rotateRatio: 0.5,
        rotationSteps: 2,
        backgroundColor: style.bgColor ? style.bgColor : "#ffe0e0",
        list: rank,
      });
    },
  },
  mounted() {
    for (let i in this.style) {
      let val = this.$q.localStorage.getItem(i);
      if (val) this.style[i] = val;
    }
    this.$root.$on("onStyleChange", (key, val) => {
      this.style[key] = val;
      this.initialize(this.rank);
    });
    this.initialize(this.rank);
  },
  watch: {
    rank() {
      this.initialize(this.rank);
    },
  },
};
</script>

<style>
</style>