import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    genres: [],
    user: [],
  },
  mutations: {
    GET_MOVIE_LIST(state, movieList) {
      state.movies = movieList
    },
    GET_GENRE_LIST(state, genreList) {
      const genres = {}
      genreList.forEach(genre => {
        genres[genre.id] = genre.name
      })
      state.genres = genres
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
    },
    getGenreList({commit}) {
      axios.get('http://127.0.0.1:8000/movies/genres')
      .then(res => {
        const genreList = res.data
        commit("GET_GENRE_LIST", genreList)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
