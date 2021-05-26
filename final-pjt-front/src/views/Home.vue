<template>
  <div class="home">
    <!-- 캐로셀 div -->
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://cdn.pixabay.com/photo/2017/11/24/10/43/ticket-2974645_960_720.jpg" class="inline-block w-100" alt="...">
          <!-- <div class="carousel-caption d-none d-md-block">
            <h5>First slide label</h5>
            <p>Some representative placeholder content for the first slide.</p>
          </div> -->
        </div>
        <div class="carousel-item">
          <img src="https://entrepreneurship.babson.edu/wp-content/uploads/2020/10/Movie-1200-630.jpg" class="inline-block w-100" alt="...">
          <!-- <div class="carousel-caption d-none d-md-block">
            <h5>Second slide label</h5>
            <p>Some representative placeholder content for the second slide.</p>
          </div> -->
        </div>
        <div class="carousel-item">
          <img src="https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2018/03/13153742/RT_300EssentialMovies_700X250.jpg" class="inline-block w-100" alt="...">
          <!-- <div class="carousel-caption d-none d-md-block">
            <h5>Third slide label</h5>
            <p>Some representative placeholder content for the third slide.</p>
          </div> -->
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev"> 
        <span class="carousel-control-prev-icon" style="background-color: #000000; border-radius: 40%" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" style="background-color: #000000; border-radius: 40%" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!-- 캐로셀 div 끝 -->
    <!-- 영화 컬렉션 -->
    <div class="container">
      <MovieCollection :movies="movies" :collectionTitle="collectionTitle"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCollection from '@/components/MovieCollection.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCollection,
  },
  data: function() {
    return {
      collectionTitle: "모든 영화",
    }
  },
  computed: {
    ...mapState([
      'movies'
    ])
  }
}
</script>
<style scoped>
.carousel-item{
}
.carousel-item img{
  object-fit: cover;
  max-width: 1280px;
  max-height: 720px;
  width: auto;
  height: auto;
}
</style>