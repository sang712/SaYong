import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    user: [],
  },
  mutations: {
    GET_MOVIE_LIST(state, movieList) {
      state.movies = movieList
    }
  },
  actions: {
    getMovieList({commit}) {
      axios.get('http://127.0.0.1:8000/movies')
      .then(res => {
        const movieList = res.data
        commit("GET_MOVIE_LIST", movieList)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
