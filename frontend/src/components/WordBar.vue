<template>
  <canvas ref="chart" width="400" height="200"></canvas>
</template>
<script>
const options = {
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};
import Chart from "chart.js/auto";
export default {
  name: "WordBar",
  props: {
    rank: Array,
    label: String,
  },
  data() {
    return {
      chart: null,
    };
  },
  methods: {
    update(rank) {
      while (this.chart.data.labels.length > 0) this.chart.data.labels.pop();

      while (this.chart.data.datasets[0].data.length > 0)
        this.chart.data.datasets[0].data.pop();

      for (let r in rank) {
        this.chart.data.labels.push(rank[r][0]);
        this.chart.data.datasets[0].data.push(rank[r][1]);
      }
      this.chart.update();
    },
  },
  mounted() {
    let tColor = this.$q.localStorage.getItem("tColor");
    this.chart = new Chart(this.$refs.chart, {
      type: "bar",
      data: {
        labels: [],
        datasets: [
          {
            label: this.label ? this.label : "",
            data: [],
            backgroundColor: [tColor ? tColor : "rgba(255, 99, 132, 0.2)"],
            borderColor: ["rgba(255, 99, 132, 1)"],
            borderWidth: 1,
          },
        ],
      },
      options: options,
    });
    this.update(this.rank);
  },
  watch: {
    rank() {
      this.update(this.rank);
    },
  },
};
</script>

<style>
</style>