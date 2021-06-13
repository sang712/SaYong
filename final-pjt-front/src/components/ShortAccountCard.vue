<template>
  <div>
    <router-link class="text-decoration-none" :to="{ name: 'AccountPK', params: { pk: user.id }}">
      <h5 class="card-title fw-bold text-primary" id="username">{{ $store.getters.capitalize(user.username) }}</h5>
    </router-link>
    <!-- 팔로워 팔로잉 정보를 어떻게 받아오느냐에 따라 주석을 선택적으로 풀면 된다. -->
    <!-- <button class="btn btn-primary w-100" @click="follow" v-show="isCurrentUserFollowsUser">팔로우 취소</button> -->
    <button class="btn btn-primary w-100" @click="$store.dispatch('follow',user.id)" v-show="isCurrentUserFollowsUser">팔로우 취소</button>
    <!-- <button class="btn btn-primary w-100" @click="follow" v-show="!isCurrentUserFollowsUser">팔로우</button> -->
    <button class="btn btn-primary w-100" @click="$store.dispatch('follow',user.id)" v-show="!isCurrentUserFollowsUser">팔로우</button>
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
// import axios from 'axios'

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
    // 현재 접속자가 상대방 유저를 팔로우하는가? (T/F) // 여기에서는 상대방의 팔로워를 탐색하지만, 현재 접속자의 팔로잉을 탐색할수도 있다.
    isCurrentUserFollowsUser() {
      // console.log(this.user.followers, this.$store.state.user.id)
      if (this.user.followers.length) {
        return this.user.followers.some(follower => follower.id === this.$store.state.user.id)
      }
      else {
        return false
      }
    },
  },
  // 팔로워 팔로잉 정보를 채워준다. data 주석처리와 같이 간다.
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
    

    // follow 메소드, Vuex Store actions로 이동되었다.
    // follow: function () {
    //   axios({
    //     method: 'POST',
    //     url: `http://127.0.0.1:8000/accounts/follow/${this.user.id}/`,
    //     headers: this.$store.getters.setToken,
    //   })
    //     .then(res=>{
    //       this.user.followers = res.data
    //     })
    //     .catch(err=>{console.log(err)})
    // },
  },
  filters: {
    // capitalize는 vuex store getters로 대체되었다.
    // capitalize: function (value) {
    //   if (!value) return ''
    //   value = value.toString()
    //   return value.charAt(0).toUpperCase() + value.slice(1)
    // }
  },
}
</script>

<style>

</style>