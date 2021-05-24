<template>
  <div>
    <h5 class="card-title" id="username">{{ user.username }}</h5>
    <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
    <span class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</span>

    <div class="my-1 card-group d-flex justify-content-center">
      <div class="card w-100">
        <div class="card-body">
          <p class="card-title">별점</p>
          <p class="card-text">{{ user.rating_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body">
          <p class="card-title">리뷰</p>
          <p class="card-text">{{ user.review_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body">
          <p class="card-title">댓글</p>
          <p class="card-text">{{ user.comment_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body">
          <p class="card-title">팔로워</p>
          <p class="card-text" v-if="followers===[]">0</p>
          <p class="card-text" v-else>{{ followers.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body">
          <p class="card-title">팔로잉</p>
          <p class="card-text" v-if="followings===[]">0</p>
          <p class="card-text" v-else>{{ followings.length }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ShortAccountCard',
  props: {
    user: {},
    followers: Array,
    followings: Array,
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