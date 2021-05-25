<template>
  <div>
    <div class="card m-3">
      <div class="card-header">
        <span>{{ review.id }}</span> - 
        <span>{{ review.title }}</span>
        <button>리뷰 수정 삭제</button>
      </div>
      <div class="card-body">
        <blockquote class="blockquote mb-0">
          <p>{{ review.content }}</p>
          <footer class="blockquote-footer">
            <span>{{ user.username }}</span> on 
            <cite title="movietitle">{{ movie.title }}</cite>
            <div>좋아요: {{ review.like_users }}</div>
            <span class="">작성: {{ review.created_at| date }}</span> | 
            <span class="">수정: {{ review.updated_at| date }}</span>
          </footer>
        </blockquote>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Review',
  data: function () {
    return {
      movie: {},
      user: {},
    }
  },
  props: {
    review: {},
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const headers = {
        Authorization: `JWT ${token}`
      }
      return headers
    },
  },
  created: function () {
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/movies/${this.review.movie}/`,
      headers: this.setToken(),
    })
      .then(res => {
        this.movie = res.data
      })
      .catch(err => {console.log(err)})
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/accounts/${this.review.user}/`,
      headers: this.setToken(),
    })
      .then(res => {
        this.user = res.data
      })
      .catch(err => {console.log(err)})
  },
  filters: {
    date: function(value) {
      // console.log(value)
      // console.log(typeof value)
      return value.substring(0,10) + " " + value.substring(11,13) + "시 " + value.substring(14,16) + "분"
    },
    // getUser: function(value) { // user.pk로 사람의 정보를 가져오는 함수
    //   console.log(value)
    // },
    // getMovie: function (value) {
    //   // console.log(value)
    //   return this.movie
    // },
  },

}
</script>

<style>

</style>