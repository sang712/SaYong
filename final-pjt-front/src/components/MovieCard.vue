<template>
  <div class="m-0 py-1 mx-xxl-0 col-xl-2 mx-xl-1 col-lg-3 col-sm-6">
     <!-- style="width: 18rem;"> -->
    <router-link :to="{ name: 'MovieDetail', params: { pk: movie.id } }">
      <div class="card bg-light" style="height: 100%;">
        <img :src=movie.poster_path class="card-img" alt="...">
        <div class="card-img-overlay p-xl-2">
          <div class="position-relative">
            <button @click.prevent="dips" class="btn rounded-circle p-0 position-absolute top-0 end-0" style="background-color: #FFFFFF; width: 30px; height: 30px"><i class="far fa-star" style="color: #D5D5D5;"></i></button>
            <!-- v-if="movie.favorite_users.includes(this.user)" -->
            <!-- <button v-else @click.prevent="dips" class="btn rounded-circle p-0 position-absolute top-0 end-0" style="background-color: #FFFFFF; width: 30px; height: 30px"><i class="fas fa-star" style="color: #FFE400;"></i></button> -->
          </div>
        </div>
        <!-- <router-link :to="{ name: 'MovieDetail', params: { pk: movie.id } }"> -->
          <p class="card-title m-2 mx-3 text-start">{{ movie.title }}</p>
        <!-- </router-link> -->
      </div>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieCard',
  data: function () {
    return {

    }
  },
  props: {
    movie: Object,
    // title: '',
    // explanation: '',
  },
  methods: {
    dips: function() {
      // 요청 응답에 문제 있음 아마 db상에서 맞지 않는 거 같음
      // 현재 에러 메시지
      // TypeError: Field 'id' expected a number but got <django.contrib.auth.models.AnonymousUser object at 0x0000022FB480DBE0>.
      console.log(this.movie.id)
      axios.post(`http://127.0.0.1:8000/movies/${this.movie.id}/favorite/`)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>