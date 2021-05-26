<template>
  <div>
    <div v-if="recommend" class="collection container mb-5">
      <h3 class="collectionTitle">{{ collectionTitle }}</h3>
      <div class="d-block" style="position: absolute; left: 0px; width: 100%; height: 317px; background: #020715;"></div>
      <div id="carouselExampleFade" class="carousel slide" data-bs-ride="carousel" data-bs-touch="true">
        <div class="carousel-inner">
          <div style="overflow-x: scroll;">
            <div class="d-flex flex-nowrap row">
            <!-- <div :class="num==1 ?'carousel-item active d-flex flex-nowrap row' : 'carousel-item d-flex flex-nowrap row'" style="overflow-x: visible;" v-for="num in Math.ceil(movies.length/6)" :key=num> -->
              <MovieCard v-for="(movie, idx) in movies" :key="idx" :movie="movies[idx]" :recommend="true" />
              <!-- <MovieCard v-for="(movie, idx) in movies.slice(6*(num-1), 6*num + 1)" :key="idx" :movie="movies[idx]" :recommend="true" /> -->
            <!-- </div> -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <!-- 텍스트 사이즈 주기 -->
      <h2 class="collectionTitle">{{ collectionTitle }}</h2>
      <div class="d-flex row justify-content-center">
        <MovieCard v-for="(movie, idx) in movies" :movie="movies[idx]" :key="idx"/>
      </div>
    </div>
  </div>
  <!-- <div class="container" style="overflow-x:scroll;">
    <div class="d-flex flex-nowrap row">
      <div v-for="movie in movies" :key="movie.pk" class="col-5 col-lg-2">
        <a :href="'http://127.0.0.1:8000/movies/' + movie.pk" class="text-decoration-none text-dark">
          <div class="card border-white">
            <img :src="movie.poster_path" class="card-img-top" alt="...">
            <div class="card-body">
              <p v-text="movie.title" class="card-text text-center fw-bold"></p>
              <p v-text="movie.release_date" class="card-text text-center"></p>
            </div>
          </div>
        </a>
      </div>
    </div>  
  </div> -->
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
    recommend: Boolean,
  }
}
</script>

<style scoped>
.collectionTitle {
  margin: 2rem 0rem 8px 0rem; /* 상, 우, 하, 좌 */
  text-align: start;
}
.collection .container{
  margin: 25px 10px;
  background: #141414;
  box-shadow: 0 0 15px 10px #141414;
}
</style>