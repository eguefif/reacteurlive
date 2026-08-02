<template>
  <div class="flex flex-col gap-[32px] m-[16px]">
    <div class="h-[124px] p-16 text-2xl">Global info</div>
    <div class="divider w-[324px] mx-auto"></div>
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
