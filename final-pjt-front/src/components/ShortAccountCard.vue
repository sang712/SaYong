<template>
  <div>
    <router-link class="text-decoration-none" :to="{ name: 'AccountPK', params: { pk: user.id }}">
      <h5 class="card-title fw-bold text-primary" id="username">{{ user.username | capitalize }}</h5>
    </router-link>
    <!-- <h6 class="card-subtitle mb-2 text-muted">이메일주소? 이름?</h6> -->
    <button class="btn btn-primary w-100" @click="follow" v-show="isCurrentUserFollowsUser">팔로우 취소</button>
    <button class="btn btn-primary w-100" @click="follow" v-show="!isCurrentUserFollowsUser">팔로우</button>
    <div class="my-1 card-group d-flex justify-content-center">
      <div class="card w-100">
        <div class="card-body" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
          <p class="card-title">별점</p>
          <p class="card-text">{{ user.rating_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="true" aria-controls="panelsStayOpen-collapseTwo">
          <p class="card-title">리뷰</p>
          <p class="card-text">{{ user.review_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="true" aria-controls="panelsStayOpen-collapseThree">
          <p class="card-title">댓글</p>
          <p class="card-text">{{ user.comment_set.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseSeven" aria-expanded="true" aria-controls="panelsStayOpen-collapseSeven">
          <p class="card-title">팔로워</p>
          <p class="card-text" v-if="user.followers===[]">0</p>
          <p class="card-text" v-else>{{ user.followers.length }}</p>
        </div>
      </div>
      <div class="card w-100">
        <div class="card-body" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseEight" aria-expanded="true" aria-controls="panelsStayOpen-collapseEight">
          <p class="card-title">팔로잉</p>
          <p class="card-text" v-if="user.followings===[]">0</p>
          <p class="card-text" v-else>{{ user.followings.length }}</p>
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
  },
  data: function () {return {
    // followers: Array,
    // followings: Array,
  }},
  computed: {
    isCurrentUserFollowsUser() {
      console.log(this.user.followers, this.$store.state.user.id)
      if (this.user.followers.length) {
        return this.user.followers.some(follower => follower.id === this.$store.state.user.id)
      }
      else {
        return false
      }
    },
  },
  // created: function (){
  //   axios.get(`http://127.0.0.1:8000/accounts/follow/${this.user.id}/`)
  //     .then(res => {
  //       // console.log(res)
  //       this.followers = res.data
  //     })
  //     .catch(err => {console.log(err)})
  //   axios.get(`http://127.0.0.1:8000/accounts/${this.user.id}/following/`)
  //     .then(res => {
  //       // console.log(res)
  //       this.followings = res.data
  //     })
  //     .catch(err => {console.log(err)})
  // },
  methods: {
    follow: function () {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/accounts/follow/${this.user.id}/`,
        headers: this.$store.getters.setToken,
      })
        .then(res=>{
          this.user.followers = res.data
        })
        .catch(err=>{console.log(err)})
    },
  },
  filters: {
  capitalize: function (value) {
    if (!value) return ''
    value = value.toString()
    return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
}
</script>

<style>

</style>