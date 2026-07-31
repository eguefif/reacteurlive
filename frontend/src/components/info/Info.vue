<template>
  <div class="wrapper">
    <div>Global info</div>
    <PlantInfo :plant="plant" />
  </div>
</template>

<script setup lang="ts">
  import { type Plant } from '@pages/plant';
  import PlantInfo from './PlantInfo.vue'

  defineProps<{
  plant?: Plant
  }>();
</script>

<style scoped>

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 32px;
}
</style
