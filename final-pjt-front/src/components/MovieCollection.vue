<template>
  <div>
    <!-- 텍스트 사이즈 주기 -->
    <div class="mx-3 text-start">{{ collectionTitle }}</div>
    <div class="d-flex row justify-content-center">
      <MovieCard v-for="(movie, idx) in movies" :movie="movies[idx]" :key="idx"/>
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
  data: function () {
    return {
      
    }
  },
  props: {
    movies: Array,
    collectionTitle: String,
  }
}
</script>

<style>

</style>