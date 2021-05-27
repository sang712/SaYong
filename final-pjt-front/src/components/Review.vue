<template>
  <div>
    <div class="card m-3">
      <div class="card-header">
        <router-link :to="{ name: 'Review', params: { pk: review.id, review: review } }">
          <h3>{{ review.id }} | 
          {{ review.title }}</h3>
        </router-link>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#reviewModifyModal">
          리뷰 수정
        </button>
        <!-- Modal -->
        <div class="modal fade" id="reviewModifyModal" tabindex="-1" aria-labelledby="reviewModifyModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="reviewModifyModalLabel">리뷰 수정</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                리뷰 수정 내용
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                <button type="button" class="btn btn-primary">삭제</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#reviewDeleteModal">
          리뷰 삭제
        </button>
        <!-- Modal -->
        <div class="modal fade" id="reviewDeleteModal" tabindex="-1" aria-labelledby="reviewDeleteModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="reviewDeleteModalLabel">리뷰 삭제</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                리뷰를 삭제하시겠습니까?
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                <button type="button" class="btn btn-danger">삭제</button>
              </div>
            </div>
          </div>
        </div>
        <button @click="likeReview" v-show="currentUserLikeThisReview" class="btn"><i class="fas fa-thumbs-up"></i></button>
        <button @click="likeReview" v-show="!currentUserLikeThisReview" class="btn"><i class="far fa-thumbs-up"></i></button>
      </div>
      <div class="card-body">
        <blockquote class="blockquote mb-0">
          <p>{{ review.content }}</p>
          <footer class="blockquote-footer">
            <router-link :to="{ name: 'AccountPK', params: { pk: user.id }}">
                <cite>{{ user.username }}</cite>
            </router-link>
            on 
            <router-link :to="{ name: 'MovieDetail', params: { pk: movie.id }}">
              <cite title="movietitle">{{ movie.title }}</cite>
            </router-link>
            <div v-show="!review.like_users.length == 0">좋아요: {{ review.like_users }}</div>
            <div>
              <span class="">작성: {{ review.created_at| date }}</span> | 
              <span class="">수정: {{ review.updated_at| date }}</span>
            </div>
            <h3>Comments</h3>
            <div class="table" v-if="!review.comment_set.length">댓글이 없습니다</div>
            <table class="table" v-else>
              <thead>
                <tr>
                  <th scope="col">id</th>
                  <th scope="col">review</th>
                  <th scope="col">user</th>
                  <th scope="col">content</th>
                  <th scope="col">created_at</th>
                  <th scope="col">updated_at</th>
                </tr>
              </thead>
              <tbody v-for="(comment, idx) in review.comment_set" :key="idx">
                <tr>
                  <th scope="row">{{ comment.id }}</th>
                  <td>{{ comment.review }}</td>
                  <td>{{ $store.getters.getUserObjectById(comment.user).username }}</td>
                  <td>{{ comment.content }}</td>
                  <td>{{ comment.created_at }}</td>
                  <td>{{ comment.updated_at }}</td>
                </tr>
              </tbody>
            </table>
            <div v-for="(comment, idx) in review.comment_set" :key="idx" class="border">
              <router-link :to="{ name: 'AccountPK', params: { pk: comment.user }}">
                {{ $store.getters.getUserObjectById(comment.user).username }}
              </router-link>
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