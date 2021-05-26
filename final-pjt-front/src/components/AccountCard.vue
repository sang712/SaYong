<template>
  <div class="container card my-3">
    <div class="card-body">

      <ShortAccountCard :user="user"/>
      
      <div class="card">
        <div class="card-header">Ratings</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.rating_set" :key="idx">
          <li class="list-group-item">
            <!-- {{ item }} -->
            {{ item.movie }}번 영화- {{item.rank}}점
          </li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Reviews</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.review_set" :key="idx">
          <li class="list-group-item">
            <!-- {{ item }} -->
            {{ item.movie}}번 영화- {{item.title}}리뷰
          </li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Comments</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.comment_set" :key="idx">
          <li class="list-group-item">
            {{ item.review }}번 리뷰 |
            {{ item.id }}번 댓글 |
            {{ item.content }} |
            {{ item.updated_at }} 수정
          </li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Liked Reviews</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.like_reviews" :key="idx">
          <li class="list-group-item">
            {{ item.id }}번 리뷰 | 
            {{ item.title }}
          </li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Favorite Movies</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.favorite_movies" :key="idx">
          <li class="list-group-item">
            {{ item.title }}
          </li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">User History</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.user_history" :key="idx">
          <li class="list-group-item" v-if="item.is_public">
            <!-- {{item}} -->
            {{ item.user }}님이 
            <span v-if="item.following">{{ item.following }}님을 팔로우했습니다</span>
            <span v-else-if="item.movie">{{ item.movie }}영화를 찜했습니다.</span>
            <span v-else-if="item.rating">{{ }}영화에 {{ item.rating }}별점을 줬습니다.</span>
            <span v-else-if="item.review">
              <span v-if="item.action_type == 30">{{ }}영화에 대해 {{ item.review }}리뷰를 남겼습니다.</span>
              <span v-else>{{ }}영화에 대한 {{ item.review }}리뷰를 좋아했습니다.</span>
            </span>
            <span v-else-if="item.comment">{{ item.comment }}댓글을 남겼습니다.</span>

          </li>
        </ul>
      </div>

      <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Another link</a>
    </div>

    <div id="followers" class="bg-light my-1">
      <div v-if="followers===[]">Followers: 0</div>
      <div v-else class="border container">
        Followers: {{ followers.length }}
        <ShortAccountCard v-for="(follower, idx) in followers" :key="idx" :user="follower"/>
      </div>
    </div>
    <div id="followings" class="bg-light my-1">
      <div v-if="followings===[]">Followings: 0</div>
      <div v-else class="border container">
        Followings: {{ followings.length }}
        <ShortAccountCard v-for="(following, idx) in followings" :key="idx" :user="following"/>
      </div>
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
    axios.get(`http://127.0.0.1:8000/accounts/follow/${this.user.id}/`)
      .then(res => {
        // console.log(res)
        this.followers = res.data
      })
      .catch(err => {console.log(err)})
    axios.get(`http://127.0.0.1:8000/accounts/${this.user.id}/following/`)
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