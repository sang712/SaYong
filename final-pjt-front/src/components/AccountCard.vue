<template>
  <div class="container card my-3">
    <div class="card-body">

      <ShortAccountCard :user="user"/>
      <div class="accordion" id="accordionPanelsStayOpenExample">
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingOne">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
              별점 목록
            </button>
          </h2>
          <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
            <div class="accordion-body">
              <div class="table" v-if="!user.rating_set.length">별점이 없습니다</div>
              <table class="table" v-else>
                <thead>
                  <tr>
                    <th scope="col">id</th>
                    <th scope="col">user</th>
                    <th scope="col">rank</th>
                    <th scope="col">created_at</th>
                  </tr>
                </thead>
                <tbody v-for="(rating, idx) in user.rating_set" :key="idx">
                  <tr>
                    <th scope="row">{{ rating.id }}</th>
                    <td>{{ $store.getters.getUserObjectById(rating.user).username }}</td>
                    <td>{{ rating.rank }}</td>
                    <td>{{ rating.created_at }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="true" aria-controls="panelsStayOpen-collapseTwo">
              리뷰 목록
            </button>
          </h2>
          <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingTwo">
            <div class="accordion-body">
              <div class="table" v-if="!user.review_set.length">리뷰가 없습니다</div>
              <table class="table" v-else>
                <thead>
                  <tr>
                    <th scope="col">id</th>
                    <th scope="col">title</th>
                    <th scope="col">user</th>
                    <th scope="col">comment_set.length</th>
                    <th scope="col">like_users.length</th>
                    <th scope="col">created_at</th>
                  </tr>
                </thead>
                <tbody v-for="(review, idx) in user.review_set" :key="idx">
                  <tr>
                    <th scope="row">{{ review.id }}</th>
                    <td>{{ review.title }}</td>
                    <td>{{ $store.getters.getUserObjectById(review.user).username }}</td>
                    <td>{{ review.comment_set.length }}</td>
                    <td>{{ review.like_users.length }}</td>
                    <td>{{ review.created_at }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingThree">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="true" aria-controls="panelsStayOpen-collapseThree">
              댓글 목록
            </button>
          </h2>
          <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingThree">
            <div class="accordion-body">
              <div class="table" v-if="!user.comment_set.length">댓글이 없습니다</div>
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
                <tbody v-for="(comment, idx) in user.comment_set" :key="idx">
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
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingFour">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseFour" aria-expanded="true" aria-controls="panelsStayOpen-collapseFour">
              Like Reviews
            </button>
          </h2>
          <div id="panelsStayOpen-collapseFour" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingFour">
            <div class="accordion-body">
              <div class="table" v-if="!user.like_reviews.length">좋아하는 리뷰가 없습니다</div>
              <table class="table" v-else>
                <thead>
                  <tr>
                    <th scope="col">id</th>
                    <th scope="col">title</th>
                    <th scope="col">user</th>
                    <th scope="col">comment_set.length</th>
                    <th scope="col">like_users.length</th>
                    <th scope="col">created_at</th>
                  </tr>
                </thead>
                <tbody v-for="(review, idx) in user.like_reviews" :key="idx">
                  <tr>
                    <th scope="row">{{ review.id }}</th>
                    <td>{{ review.title }}</td>
                    <td>{{ $store.getters.getUserObjectById(review.user).username }}</td>
                    <td>{{ review.comment_set.length }}</td>
                    <td>{{ review.like_users.length }}</td>
                    <td>{{ review.created_at }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingFive">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseFive" aria-expanded="true" aria-controls="panelsStayOpen-collapseFive">
              Favorite Movies
            </button>
          </h2>
          <div id="panelsStayOpen-collapseFive" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingFive">
            <div class="accordion-body">
              <div class="table" v-if="!user.favorite_movies.length">찜한 영화가 없습니다</div>
              <table class="table" v-else>
                <thead>
                  <tr>
                    <th scope="col">id</th>
                    <th scope="col">title</th>
                    <th scope="col">rating_set.length</th>
                    <th scope="col">favorite_users.length</th>
                    <th scope="col">release_date</th>
                  </tr>
                </thead>
                <tbody v-for="(movie, idx) in user.favorite_movies" :key="idx">
                  <tr>
                    <th scope="row">{{ movie.id }}</th>
                    <td>{{ movie.title }}</td>
                    <td>{{ movie.rating_set.length }}</td>
                    <td>{{ movie.favorite_users.length }}</td>
                    <td>{{ movie.release_date }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingSix">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseSix" aria-expanded="true" aria-controls="panelsStayOpen-collapseSix">
              User History
            </button>
          </h2>
          <div id="panelsStayOpen-collapseSix" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingSix">
            <div class="accordion-body">
              <div class="table" v-if="!user.user_history.length">활동내역이 없습니다</div>
              <table class="table" v-else>
                <thead>
                  <tr>
                    <th scope="col">id</th>
                    <!-- <th scope="col">action_type</th> -->
                    <!-- <th scope="col">is_public</th> -->
                    <th scope="col">created_at</th>
                    <th scope="col">message</th>
                  </tr>
                </thead>
                <tbody v-for="(log, idx) in user.user_history" :key="idx">
                  <tr v-if="log.is_public">
                    <th scope="row">{{ log.id }}</th>
                    <!-- <td>{{ log.action_type }}</td> -->
                    <!-- <td>{{ log.is_public }}</td> -->
                    <td>{{ $store.getters.displayDateTime(log.created_at) }}</td>
                    <td>
                      {{ $store.getters.getUserObjectById(log.user).username }}님이 
                      <span v-if="log.following">{{ $store.getters.getUserObjectById(log.following).username }}님을 팔로우했습니다</span>
                      <span v-else-if="log.movie">{{ $store.getters.getMovieObjectById(log.movie).title }}영화를 찜했습니다.</span>
                      <span v-else-if="log.rating">{{ $store.getters.getRatingObjectById(log.rating).movie }}영화에 {{ log.rating }}별점을 줬습니다.</span>
                      <span v-else-if="log.review">
                        <span v-if="log.action_type == 30">{{ }}영화에 대해 {{ log.review }}리뷰를 남겼습니다.</span>
                        <span v-else>{{ }}영화에 대한 {{ log.review }}리뷰를 좋아했습니다.</span>
                      </span>
                      <span v-else-if="log.comment">{{ log.comment }}댓글을 남겼습니다.</span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingSeven">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseSeven" aria-expanded="true" aria-controls="panelsStayOpen-collapseSeven">
              Followers
            </button>
          </h2>
          <div id="panelsStayOpen-collapseSeven" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingSeven">
            <div class="accordion-body">
              <div class="table" v-if="!user.followers.length">팔로워가 없습니다</div>
              <table class="table" v-else>
                Followers: {{ followers.length }}
                <ShortAccountCard v-for="(follower, idx) in followers" :key="idx" :user="follower"/>
              </table>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingEight">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseEight" aria-expanded="true" aria-controls="panelsStayOpen-collapseEight">
              Followings
            </button>
          </h2>
          <div id="panelsStayOpen-collapseEight" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingEight">
            <div class="accordion-body">
              <div class="table" v-if="!user.followings.length">팔로잉이 없습니다</div>
              <table class="table" v-else>
                Followers: {{ followings.length }}
                <ShortAccountCard v-for="(following, idx) in followings" :key="idx" :user="following"/>
              </table>
            </div>
          </div>
        </div>
      </div>
      
      <!-- <a href="#" class="card-link">Card link</a> -->
      <!-- <a href="#" class="card-link">Another link</a> -->
    </div>


  </div>
</template>

<script>
import ShortAccountCard from '@/components/ShortAccountCard.vue'
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'AccountCard',
  components: {
    ShortAccountCard,
  },
  props: {
    user: {},
    pk: {}
  },
  data: function () { return {
    followers: [],
    followings: [],
  }},
  methods: {

  },
  computed: mapState([
    'movies', //'users'
  ]),
  filters: {
  },
  created: function (){
    // console.log(this.user)
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/follow/${this.user.id}/`,
      headers: this.$store.getters.setToken,
    })
      .then(res => {
        // console.log(res)
        this.followers = res.data
      })
      .catch(err => {console.log(err)})
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/${this.user.id}/following/`,
      headers: this.$store.getters.setToken,
    })
      .then(res => {
        // console.log(res)
        this.followings = res.data
      })
      .catch(err => {console.log(err)})
  },
}
</script>

<style>

</style>