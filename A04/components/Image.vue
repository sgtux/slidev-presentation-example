<script setup lang="ts">
const props = defineProps({
  src: {
    default: '',
  },
  height: {
    default: undefined
  },
  width: {
    default: undefined
  },
  style: {
    default: undefined
  }
})

const IMAGE_PATH = 'http://localhost:8000/'

</script>

<template>
  <img alt="" v-bind:src="IMAGE_PATH + props.src" v-bind:width="props.width" v-bind:height="props.height" v-bind:style="props.style" />
</template>
