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

const IMAGE_PATH_TO_USE = '#IMAGE_PATH_TO_USE#'

const IMAGE_PATH = IMAGE_PATH_TO_USE.includes('IMAGE_PATH_TO_USE') ? 'http://localhost:8000/' : IMAGE_PATH_TO_USE

</script>

<template>
  <img alt="" v-bind:src="IMAGE_PATH + props.src" v-bind:width="props.width" v-bind:height="props.height" v-bind:style="props.style" />
</template>