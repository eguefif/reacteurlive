<script setup lang="ts">
  import MapFr from '@components/map/Map.vue'
  import Info from '@components/info/Info.vue'
  import { onMounted, ref } from 'vue';
  import axios from 'axios';
  import { type Plant, type Reactor } from "./plant";

  const loading = ref<boolean>(true);
  const plants = ref<Map<string, Plant>>(new Map());
  const plant = ref<Plant | undefined>(undefined);

  onMounted(async () => {
    loading.value = true;
    const response = await axios.get<Reactor[]>('/plants');
    loading.value = false;

    response.data.forEach((reactor: Reactor) => {
      const plant: Plant = plants.value.get(reactor.name) || {
          name: reactor.name,
          sector: reactor.sector,
          subSector: reactor.sector,
          gps: reactor.gps,
          city: reactor.city,
          departement: reactor.departement,
          region: reactor.region,
          reactors: [],
      };
      plant.reactors.push(reactor);
      plants.value.set(reactor.name, plant)
    });
  });
</script>

<template>
  <div v-if="loading">Loading</div>
  <div class="wrapper" v-else>
    <div class="info">
      <Info :plant="plant" />
    </div>
    <div class="map">
      <MapFr :plants="plants" v-model="plant" class="map"/>
    </div>
  </div>
</template>

<style scoped>
  .wrapper{
    display: flex;
    justify-content: space-between;
    gap: 32px;
  }

  .info {
    flex-basis: 35%;
  }
  .map {
    flex-basis: 65%;
  }
</style>
