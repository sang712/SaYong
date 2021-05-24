<template>
  <div>
    <h1>Login</h1>
    <div>
      <span for="username">사용자 이름: </span>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <span for="password">비밀번호: </span>
      <input @keyup.enter="login(credentials)" type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        this.$store.dispatch('login') // 로그인 완료
        this.$router.push({ name: 'Home' })
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>