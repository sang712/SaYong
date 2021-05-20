<template>
  <div>
    <div class="mx-3 text-start">Movie Collection Title</div>
    <div class="d-flex flex-row">
      <MovieCard/>
      <MovieCard/>
      <MovieCard/>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieCollection',
  components: {
    MovieCard,
  },
}
</script>

<style>

</style>