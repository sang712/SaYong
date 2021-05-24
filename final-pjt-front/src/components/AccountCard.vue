<template>
  <div class="container">
    <div id="userinfo">
      username: {{ user }}
    </div>
    <div id="followerinfo">
      follower: {{ followerinfo }}
    </div>
    <div id="followinginfo">
      following: {{ followinginfo }}
    </div>
    <div id="myreviews">
      myreviews
    </div>
    <div id="mycomments">
      mycomments
    </div>
    <div id="mylikes">
      mylikes
    </div>
    <div id="myfavorites">
      myfavorites
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AccountCard',
  props: {
    user: {},
  },
  data: function () { return {
    followerinfo: {},
    followinginfo: {},
  }},
  methods: {

  },
  created: function (){
    axios.get(`http://127.0.0.1:8000/accounts/follow/${this.user.id}/`)
      .then(res => {
        console.log(res)
        this.followerinfo = res.data
      })
      .catch(err => {console.log(err)})
  },
}
</script>

<style>

</style>