<template>
  <div class="container card my-3">
    <div class="card-body">
      <!-- <ShortAccountCard :user="user" :followers="followers" :followings="followings"/> -->
      <ShortAccountCard :user="user"/>
      
      <div class="card">
        <div class="card-header">Ratings</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.rating_set" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Reviews</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.review_set" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Comments</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.comment_set" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Liked Reviews</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.like_reviews" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">Favorite Movies</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.favorite_movies" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <div class="card">
        <div class="card-header">User History</div>
        <ul class="list-group list-group-flush" v-for="(item, idx) in user.user_history" :key="idx">
          <li class="list-group-item">{{ item }}</li>
        </ul>
      </div>

      <a href="#" class="card-link">Card link</a>
      <a href="#" class="card-link">Another link</a>
    </div>

    <div id="followers" class="bg-light">
      <div v-if="followers===[]">Followers: 0</div>
      <div v-else>
        Followers: {{ followers.length }}
        <ShortAccountCard v-for="(follower, idx) in followers" :key="idx" :user="follower"/>
      </div>
    </div>
    <div id="followings" class="bg-light">
      <div v-if="followings===[]">Followings: 0</div>
      <div v-else>
        Followings: {{ followings.length }}
        <ShortAccountCard v-for="(following, idx) in followings" :key="idx" :user="following"/>
      </div>
    </div>

  </div>
</template>

<script>
import ShortAccountCard from '@/components/ShortAccountCard.vue'
import axios from 'axios'

export default {
  name: 'AccountCard',
  components: {
    ShortAccountCard,
  },
  props: {
    user: {},
  },
  data: function () { return {
    followers: [],
    followings: [],
  }},
  methods: {

  },
  created: function (){
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