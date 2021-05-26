<template>
  <div>
    <div class="card m-3">
      <div class="card-header">
        <div></div>
        <span>{{ review.id }}</span> - 
        <span>{{ review.title }}</span>
        <button>리뷰 수정 삭제</button>
        <button @click="likeReview" v-show="currentUserLikeThisReview">좋아요 취소</button>
        <button @click="likeReview" v-show="!currentUserLikeThisReview">좋아요</button>
      </div>
      <div class="card-body">
        <blockquote class="blockquote mb-0">
          <p>{{ review.content }}</p>
          <footer class="blockquote-footer">
            <span>{{ user.username }}</span> on 
            <cite title="movietitle">{{ movie.title }}</cite>
            <div v-show="!review.like_users.length == 0">좋아요: {{ review.like_users }}</div>
            <div>
              <span class="">작성: {{ review.created_at| date }}</span> | 
              <span class="">수정: {{ review.updated_at| date }}</span>
            </div>
            <h3>Comments</h3>
            <div v-for="(comment, idx) in review.comment_set" :key="idx" class="border">
              <div class="">{{ $store.getters.getUserObjectById(comment.user).username }}</div>
              <div class="">{{ comment.content }}</div>
              <div class="">{{ comment.created_at| date }}</div>
            </div>
            <h3>Writer</h3>
            <div class="border">
              <ShortAccountCard :user="user" class="container"/>
            </div>
          </footer>
        </blockquote>
      </div>
    </div>
  </div>
</template>

<script>
import ShortAccountCard from '@/components/ShortAccountCard.vue'
import axios from 'axios'


export default {
  name: 'Review',
  components: {
    ShortAccountCard,
  },
  data: function () {
    return {
      movie: {},
      user: {}, // 이 글을 쓴 사람, 작성자
      currentUser: this.$store.state.user,  // 현재 접속자
    }
  },
  props: {
    review: {},
  },
  computed: {
    currentUserLikeThisReview () {
      // 리뷰 기준 접근
      return this.review.like_users.includes(this.currentUser.id)
      // 유저 기준 접근
      // return this.currentUser.like_reviews.includes(...)
    },
  },
  methods: {
    likeReview: function () {
      // 리뷰를 좋아요 하면 review를 갱신한다.
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/like/`,
        headers: this.$store.getters.setToken,
      })
        .then(res => {
          this.review = res.data
        })
        .catch(err => {console.log(err)})
    },
  },
  created: function () {
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/movies/${this.review.movie}/`,
      headers: this.$store.getters.setToken,
    })
      .then(res => {
        this.movie = res.data
      })
      .catch(err => {console.log(err)})
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/accounts/${this.review.user}/`,
      headers: this.$store.getters.setToken,
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

    // getMovie: function (value) {
    //   // console.log(value)
    //   return this.movie
    // },
  },

}
</script>

<style>

</style>