import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    users: [],
    genres: [],
    ratings: [],
    reviews: [],
    user: { favorite_movies: [] },
    username: '',
    isLogin: false,
  },
  mutations: {
    GET_MOVIE_LIST(state, movieList) {
      state.movies = movieList
    },
    GET_USER_LIST(state, userList) {
      state.users = userList
    },
    GET_RATING_LIST(state, ratingList) {
      state.ratings = ratingList
    },
    GET_REVIEW_LIST(state, reviewList) {
      state.reviews = reviewList
    },
    GET_GENRE_LIST(state, genreList) {
      const genres = {}
      genreList.forEach(genre => {
        genres[genre.id] = genre.name
      })
      state.genres = genres
    },
    GET_USER(state, user) {
      state.user = user
    },
    UPDATE_MOVIE(state, movie) {
      const updatedMovieIdx = state.movies.findIndex(formerMovie => {
        return movie.id === formerMovie.id
      })
      state.movies.splice(updatedMovieIdx, 1, movie)
    },
    IS_LOGIN(state) {
      const token = localStorage.getItem('jwt')
      if (token) {
        state.isLogin = true
      } else {
        state.isLogin = false
      }
    },
    LOGIN(state) {
      state.isLogin = true
    },
    // LOGOUT(state) {
    //   state.isLogin = false
    // }
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
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/genres',
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then(res => {
        const genreList = res.data
        commit("GET_GENRE_LIST", genreList)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getUserList({commit}) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/index/',
        headers: {Authorization: `JWT ${token}`},
      })
      .then(res => {
        const userList = res.data
        commit("GET_USER_LIST", userList)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getRatingList({commit}) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/rating/',
        headers: {Authorization: `JWT ${token}`},
      })
      .then(res => {
        const ratingList = res.data
        commit("GET_RATING_LIST", ratingList)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getReviewList({commit}) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/review/',
        headers: {Authorization: `JWT ${token}`},
      })
      .then(res => {
        const reviewList = res.data
        commit("GET_REVIEW_LIST", reviewList)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getUser({commit}) {
      const token = localStorage.getItem('jwt')
      this.state.username = localStorage.getItem('username')
      if (this.state.username) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/${this.state.username}/`,
          headers: {Authorization: `JWT ${token}`},
        })
        .then(res => {
          // console.log(res)
          const user = res.data
          // console.log("getUser", this.state.username, user)
          commit("GET_USER", user)
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        // console.log(this.state.username)
      }
    },
    updateMovie({commit}, movie_id) {
      const token = localStorage.getItem('jwt')
      if (this.state.username) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/${movie_id}/`,
          headers: {Authorization: `JWT ${token}`},
        })
        .then(res => {
          const movie = res.data
          commit("UPDATE_MOVIE", movie)
        })
      }
    },
    isLogin({commit}) {
      // 로그인 했는지 확인
      commit("IS_LOGIN")
    },
    login({commit}) {
      // 로그인 하기
      commit("LOGIN")
    },
    // logout({commit}) {
    //   // 로그아웃 하기
    //   commit("LOGOUT")
    // }
  },
  getters: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const headers = {
        Authorization: `JWT ${token}`
      }
      return headers
    },
    // https://vuex.vuejs.org/guide/getters.html#method-style-access
    getUserObjectById: (state) => (id) => {
      return state.users.find(user => user.id === id)
    }
  },
  modules: {

  }
})
