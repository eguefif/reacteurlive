<template>
  <div class="wrapper">
    <div v-if="plant">{{ plant }}</div>
    <div v-if="!plant">Select a plant</div>
  </div>
</template>

<script setup lang="ts">
    import { type Plant } from "@pages/plant";
    defineProps<{
      plant?: Plant
    }>();
</script>

<style scoped>
  .wrapper {
    flex: 1
  }
</style>
