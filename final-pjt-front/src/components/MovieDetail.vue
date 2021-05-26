<template>
  <div>
    <p>영화 상세페이지</p>
    <div class="card mb-3 container">
      <div class="row g-0 justify-content-between">
        <div class="col-md-4 row p-0">
          <img :src=movie.poster_path class="col-12 p-0" alt="movie_poster">
          <!-- MovieCard.vue의 찜 버튼이 추가되면 여기에도 추가하기 -->
        </div>
        <div class="col-md-8">
          <div class="card-body text-start">
            <h1 class="card-title">{{ movie.title }}</h1>
            <span>{{ movie.release_date| year }} | </span>
            <span>{{ movieGenres }}</span>
            <br>
            <span class="card-text">평균 점수 : {{ movie.vote_average }} | </span>
            <span>
              내 점수 : 
              <StarRating :grade="gradeNumber" :maxStars="10" :hascounter="true" :movie="movie" :user="user"/>
            </span>
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
import StarRating from '@/components/StarRating.vue'

export default {
  name: 'MovieDetail',
  components: {
    StarRating,
  },
  data: function() {
    return {
      movie: [],
      movieGenres: [],
      gradeNumber: 0,
    }
  },
  props: {
    'pk': Number,
    'user': Object,
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
    const ratingList = this.movie.rating_set.filter(rating => {
      return rating.user === this.user.id
    })
    this.gradeNumber = ratingList.reduce((acc, num) => {
      return acc*0 + num.rank
    }, 0)
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