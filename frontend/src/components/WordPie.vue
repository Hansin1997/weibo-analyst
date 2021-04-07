<template>
  <canvas ref="chart" width="400" height="200"></canvas>
</template>
<script>
import Chart from "chart.js/auto";
export default {
  name: "WordBar",
  props: {
    pos: Number,
    neg: Number,
  },
  data() {
    return {
      chart: null,
    };
  },
  methods: {
    update() {
      while (this.chart.data.datasets[0].data.length > 0)
        this.chart.data.datasets[0].data.pop();
      this.chart.data.datasets[0].data.push(this.pos);
      this.chart.data.datasets[0].data.push(this.neg);
      this.chart.update();
    },
  },
  mounted() {
    this.chart = new Chart(this.$refs.chart, {
      type: "pie",
      data: {
        labels: [this.$t("pos"), this.$t("neg")],
        datasets: [
          {
            label: this.$t("emotion"),
            data: [this.pos, this.neg],
            backgroundColor: ["rgb(54, 162, 235)", "rgb(255, 99, 132)"],
            hoverOffset: 4,
          },
        ],
      },
    });
    this.chart.update();
  },
  watch: {
    pos() {
      this.update();
    },
    neg() {
      this.update();
    },
  },
};
</script>

<style>
</style>