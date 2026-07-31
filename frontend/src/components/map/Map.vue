<script setup lang="ts">
  import { onMounted, onUnmounted, ref } from 'vue';
  import L from 'leaflet';
  import 'leaflet/dist/leaflet.css';
  import { type LeafletMouseEvent } from 'leaflet'
  import { type Plant } from "@pages/plant";

  const mapContainer = ref<HTMLDivElement | null>(null);
  let map: L.Map | null = null;

  const props = defineProps<{
    plants: Plant[]
  }>();

  const selectedPlant = defineModel<Plant> ();

  function addMarkers(plantList: Plant[]) {
    if (!map) return;
    plantList.forEach((plant: Plant) => {
      const coordinate: number[] = plant.gps
      .split(',')
      .map((entry: string) => entry.trim())
      .map((entry: string) => Number(entry));

      L.marker(coordinate as [number, number])
      .bindPopup(plant.name)
      .on('click', (_e: LeafletMouseEvent) => selectedPlant.value = plant)
      .addTo(map as L.Map);
    });
  }

  onMounted(async () => {
    if (!mapContainer.value) return;
    map = L.map(mapContainer.value).setView([46.6, 2.5], 6);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    addMarkers(props.plants);
  });

  onUnmounted(() => {
  if (map) map.remove()
  })
</script>

<template>
  <div class="map-wrapper">
    <div ref="mapContainer" class="map"></div>
  </div>
</template>

<style scoped>
  .map-wrapper{
    display: flex;
    justify-content: center;
  }
  .map {
    height: 800px;
    width: 1000px;

  }
</style>
