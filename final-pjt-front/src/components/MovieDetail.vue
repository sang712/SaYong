<template>
  <div>
    <p>영화 상세페이지</p>
    <div class="card mb-3 container">
      <div class="row g-0 justify-content-between">
        <div class="col-md-4 row p-0">
          <img :src=movie.poster_path class="col-12 p-0" alt="movie_poster">
        </div>
        <div class="col-md-8">
          <div class="card-body text-start">
            <h1 class="card-title">{{ movie.title }}</h1>
            <span>{{ movie.release_date| year }} | </span>
            <span v-for="(genre, idx) in movie.genres" :key="idx">{{ genre| genre }} | </span>
            <br>
            <span class="card-text">누적관객 : {{ movie.popularity| popularity }} | </span>
            <span class="card-text">평균 점수 : {{ movie.vote_average }}</span>
            <hr>
            <h4>줄거리</h4>
            <p v-if="movie.overview" class="card-text">{{ movie.overview }}</p>
            <p v-else>등록된 줄거리가 없습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  data: function() {
    return {
      movie: [],
    }
  },
  props: {
    'pk': Number,
  },
  function: {

  },
  created() {
    this.movie = this.movies[Number(this.pk)]
  },
  computed: {
    ...mapState([
      'movies',
      'genres',
    ])
  },
  filters: {
    year: function(value) {
      return value.substring(0,4)
    },
    genre: (value) => {
      return value
      // return this.genres[value]
    },
    popularity: (value) => {
      return value * 1000
    }
  }
}
</script>

<style>

</style>