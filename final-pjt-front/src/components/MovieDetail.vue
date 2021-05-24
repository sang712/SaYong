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
            <span>{{ movieGenres }} | </span>
            <br>
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
      movieGenres: [],
    }
  },
  props: {
    'pk': Number,
  },
  function: {

  },
  created() {
    this.movie = this.movies.find((movie) => {
      return (movie.id===Number(this.pk))
    })
    this.movieGenres = this.movie.genres.map(genre => {
      return genre.name
    }).join('/')
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
    popularity: (value) => {
      return value * 1000
    }
  }
}
</script>

<style>

</style>