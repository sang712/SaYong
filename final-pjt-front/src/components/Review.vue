<template>
  <div>
    <div class="card m-3">
      <div class="card-header d-flex justify-content-between">
        <div class="mx-3 my-1">
          <router-link class="text-decoration-none" :to="{ name: 'Review', params: { pk: review.id, review: review } }">
            <h3 class="text-start m-0">{{ review.id }} | 
            {{ review.title }}</h3>
          </router-link>
        </div>
        <!-- Button trigger modal -->
        <div>
          <span v-show="!review.like_users.length == 0">좋아요: {{ review.like_users.length }}</span>
          <button @click="likeReview" v-show="currentUserLikeThisReview" class="btn"><i class="fas fa-thumbs-up"></i></button>
          <button @click="likeReview" v-show="!currentUserLikeThisReview" class="btn"><i class="far fa-thumbs-up"></i></button>

          <button v-if="isSameUser" type="button" class="btn btn-primary m-2 btn-sm" data-bs-toggle="modal" data-bs-target="#reviewModifyModal">
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
                    <div class="loginForm d-flex justify-content-center row">
                      <div class="input-group position-relative col-12">
                        <div for="title" class="align-middle">리뷰 제목: </div>
                        <input type="text" id="title" v-model="review.title" class="mr-2 form-control" style="width: auto;">
                      </div>
                      <div class="input-group position-relative col-12">
                        <div for="content" class="align-middle">내용: </div>
                        <textarea type="content" id="password" v-model="review.content" class="form-control" style="width: auto;" rows="5"/>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                    <button @click="reviewUpdate()" data-bs-dismiss="modal" class="btn btn-primary">수정</button>
                  </div>
              </div>
            </div>
          </div>
          <!-- Button trigger modal -->
          <button v-if="isSameUser" type="button" class="btn btn-danger m-2 btn-sm" data-bs-toggle="modal" data-bs-target="#reviewDeleteModal">
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
                  <button type="button" @click="reviewDelete()" data-bs-dismiss="modal" class="btn btn-danger">삭제</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body">
        <blockquote class="blockquote mb-0">
          <p>{{ review.content }}</p>
          <br>
          <footer class="blockquote-footer">
            <router-link class="text-decoration-none" :to="{ name: 'AccountPK', params: { pk: user.id }}">
                <cite>{{ user.username | capitalize }}</cite>
            </router-link>
            on 
            <router-link class="text-decoration-none" :to="{ name: 'MovieDetail', params: { pk: movie.id }}">
              <cite title="movietitle">{{ movie.title }}</cite>
            </router-link>
            <div class="text-end">
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
                  <th scope="col"><button type="button" class="btn btn-primary m-0 btn-sm" data-bs-toggle="modal" data-bs-target="#commentCreateModal">
                                    댓글 작성
                                  </button>
                                  <!-- Modal -->
                                  <div class="modal fade" id="commentCreateModal" tabindex="-1" aria-labelledby="commentCreateModalLabel" aria-hidden="true">
                                    <div class="modal-dialog">
                                      <div class="modal-content">
                                        <div class="modal-header">
                                          <h5 class="modal-title" id="commentCreateModalLabel">댓글 작성</h5>
                                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                        </div>
                                        <div class="modal-body">
                                            <div class="loginForm d-flex justify-content-center row">
                                              <div class="input-group position-relative col-12">
                                                <div for="content" class="align-middle">내용: </div>
                                                <textarea type="content" id="password" v-model="commentCreating.content" class="form-control" style="width: auto;" rows="5"/>
                                              </div>
                                            </div>
                                          </div>
                                          <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                                            <button @click="commentCreate()" data-bs-dismiss="modal" class="btn btn-primary">작성</button>
                                          </div>
                                      </div>
                                    </div>
                                  </div>
                  </th>
                </tr>
              </thead>
              <tbody v-for="(comment, idx) in review.comment_set" :key="idx">
                <tr>
                  <th scope="row">{{ comment.id }}</th>
                  <td>{{ comment.review }}</td>
                  <td>{{ $store.getters.getUserObjectById(comment.user).username }}</td>
                  <td>{{ comment.content }}</td>
                  <td>{{ comment.created_at | date }}</td>
                  <td>{{ comment.updated_at | date }}</td>
                  <td><button v-if="isSameUserforComment(comment.user)" @click="commentDelete(comment.id)" class="btn btn-sm btn-danger">삭제</button></td>
                </tr>
              </tbody>
            </table>
            <!-- <div v-for="(comment, idx) in review.comment_set" :key="idx" class="border">
              <router-link class="text-decoration-none" :to="{ name: 'AccountPK', params: { pk: comment.user }}">
                {{ $store.getters.getUserObjectById(comment.user).username }}
              </router-link>
              <div class="">{{ comment.content }}</div>
              <div class="">{{ comment.created_at| date }}</div>
            </div> -->
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
      reviewUpdating: {
        title: null,
        movie: this.review.movie,
        content: null,
        user: this.review.user,
      },
      commentCreating: {
        review: this.review.id,
        user: null,
        content: null,
      }
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
    isSameUser() {
      return this.user.id === this.currentUser.id
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
    reviewUpdate: function() {
      this.reviewUpdating.title = this.review.title
      this.reviewUpdating.content = this.review.content
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/`,
        data: this.reviewUpdating,
        headers: this.$store.getters.setToken,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Review', params: {review: res.data, pk: res.data.id}})
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    reviewDelete: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/`,
        headers: this.$store.getters.setToken,
      })
      .then(res => {
        console.log(res)
        // 페이지 새로고침에서 문제가 발생하니까 홈에 들렀다 오기
        this.$router.push({ name: 'Home'})
        .then(()=>{
          this.$router.push({ name: 'ReviewList'})
        })
      })
      .catch(err => {
        console.log(err.response)
      })
    },
    commentCreate: function() {
      this.commentCreating.user =  this.currentUser.id
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/${this.review.id}/comment/`,
        data: this.commentCreating,
        headers: this.$store.getters.setToken,
      })
      .then(res => {
        console.log(res)
        this.reviewRerender()
      })
      .catch(err => {
        console.log(err)
      })
    },
    commentDelete: function(comment_id) {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/comment/${comment_id}/`,
        data: {user: this.currentUser.id},
        headers: this.$store.getters.setToken,
      })
      .then(res => {
        console.log(res)
        this.reviewRerender()
      })
      .catch(err => {
        console.log(err)
      })
    },
    isSameUserforComment(user_id) {
      return user_id === this.currentUser.id
    },
    reviewRerender() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/review/${this.review.id}`,
        headers: this.$store.getters.setToken,
      })
      .then(res => {
        this.review = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }

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
    capitalize: function (value) {
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
    },
    // getMovie: function (value) {
    //   // console.log(value)
    //   return this.movie
    // },
  },
  
  

}
</script>

<style>
.text-decoration-none{
  color: #020715;
}
</style>