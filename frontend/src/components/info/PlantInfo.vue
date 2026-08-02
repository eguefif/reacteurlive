<template>
  <div class="mx-auto">
    <div v-if="!plant">Select a plant</div>
    <div v-if="plant" class="card bg-base-300 w-96 shadow-sm">
      <div class="card-body flex flex-col gap-[32px]">
        <figure>
          <img :src="imageUrl" :alt="plant.name"/>
        </figure>
        <div class="card-title"> {{ plant.name }} </div>
        <div class="ml-[16px] flex flex-col gap-[16px]">
          <div> Région {{ capitalizedRegion }} - {{ plant.city }} ({{ plant.departement }}) </div>
          <div> {{ plant.reactors.length }} réacteurs {{ plant.sector}}</div>
          <div> Puissance totale de {{ totalPower }} mégawatt</div>
          <div v-for="(reactor, index) in plant.reactors">
            <div>Réacteur {{ index + 1}} : {{reactor.powerMW }} mégawatt</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
    import {computed } from 'vue';
    import { type Plant } from "@pages/plant";
    const props = defineProps<{
      plant?: Plant
    }>();

    const totalPower = computed(() => {
      if (!props.plant) return 0;
      const result = props.plant.reactors.reduce((acc, value) => acc + value.powerMW
      , 0);
      return result;
      });

    const capitalizedRegion = computed(() => {
      if(!props.plant) return "";
      const firstLetter = props.plant.region.charAt(0).toUpperCase();
      return firstLetter + props.plant.region.toLowerCase().slice(1);
    })

    const imageUrl = computed(() => {
      if (!props.plant) return "/images/image-missing.png";

      return "/images/" + props.plant.name.toLowerCase() + ".png"
    })
</script>

<style scoped>
  .wrapper {
    flex: 1
  }
</style>
