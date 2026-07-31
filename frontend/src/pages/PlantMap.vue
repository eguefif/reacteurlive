<script setup lang="ts">
  import Map from '@components/map/Map.vue'
  import Info from '@components/info/Info.vue'
  import { onMounted, ref } from 'vue';
  import axios from 'axios';
  import { type Plant } from "./plant";

  const loading = ref<boolean>(true);
  const plants = ref([] as Plant[]);
  const plant = ref<Plant | undefined>(undefined);

  onMounted(async () => {
    loading.value = true;
    const response = await axios.get<Plant[]>('/plants');
    loading.value = false;

    plants.value = response.data;
    plants.value.forEach((plant: Plant) => console.log(plant.gps))
  });
</script>

<template>
  <div v-if="loading">Loading</div>
  <div class="wrapper" v-else>
    <div class="info">
      <Info :plant="plant" />
    </div>
    <div class="map">
      <Map :plants="plants" v-model="plant" class="map"/>
    </div>
  </div>
</template>

<style scoped>
  .wrapper{
    display: flex;
    justify-content: space-between;
  }

  .info {
    flex-basis: 35%;
  }
  .map {
    flex-basis: 65%;
  }
</style>
