<template>
  <div class="m-0 py-1 mx-xxl-0 col-xl-2 mx-xl-1 col-lg-3 col-sm-6">
     <!-- style="width: 18rem;"> -->
    <router-link :to="{ name: 'MovieDetail', params: { pk: movie.id } }">
      <div class="card bg-light" style="height: 100%;">
        <img :src=movie.poster_path class="card-img" alt="...">
        <div class="card-img-overlay p-xl-2">
          <div class="position-relative">
            <button v-show="isStyle" @click.prevent="dips" class="btn rounded-circle p-0 position-absolute top-0 end-0" style="background-color: #FFFFFF; width: 30px; height: 30px"><i class="fas fa-star" style="color: #FFE400;"></i></button>
            <button v-show="!isStyle" @click.prevent="dips" class="btn rounded-circle p-0 position-absolute top-0 end-0" style="background-color: #FFFFFF; width: 30px; height: 30px"><i class="far fa-star" style="color: #D5D5D5;"></i></button>
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
import { mapState } from 'vuex'

export default {
  name: 'MovieCard',
  data: function () {
    return {
      isStyle: false,
      
    }
  },
  props: {
    movie: Object,
    // title: '',
    // explanation: '',
  },
  computed: {
    ...mapState([
      'username',
      'user',
    ]),
  },
  beforeMount: function() {
    if (this.user) {
        this.isStyle = this.user.favorite_movies.some((movie) => {
          return this.movie.id === movie.id
        })
        
      } else {
        this.isStyle = false
      }
  },
  // watch: {
  //   isDip: function() {

  //   }
  // },
  methods: {
    isDip: function() {
      
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const headers = {
        Authorization: `JWT ${token}`
      }
      return headers
    },
    dips: function() {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/favorite/`,
        headers: this.setToken(),
      })
      .then((res) => {
        console.log(res)
        this.isStyle = !this.isStyle
      })
      .catch((err) => {
        if (err.response.status === 401) {
          this.$router.push({ name: 'Login', params: { needToLogin: true } })
        }
        console.log(err.response)
      })
    }
  }
}
</script>

<style>

</style>