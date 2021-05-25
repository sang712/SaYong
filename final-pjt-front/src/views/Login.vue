<template>
  <div class="d-flex flex-column justify-content-center">
    <h1>Login</h1>
    <div v-if="needToLogin" class="d-flex justify-content-center">
      <div class="needToLogin alert alert-danger">
        로그인이 필요한 요청입니다. 
      </div>
    </div>
    <div class="loginForm d-flex justify-content-center">
      <div class="border border-secondary rounded-3">
        <div class="input position-relative">
          <span for="username" class="align-middle">사용자 이름: </span>
          <input type="text" id="username" v-model="credentials.username" class="position-absolute end-0">
        </div>
        <div class="input position-relative">
          <span for="password" class="align-middle">비밀번호: </span>
          <input @keyup.enter="login(credentials)" type="password" id="password" v-model="credentials.password" class="position-absolute end-0">
        </div>
        <button @click="login(credentials)" class="btn btn-success">로그인</button>
      </div>
    </div>
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
      needToLogin: false,
      }
    }
  },
  props: {
    needToLogin: Boolean,
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
        localStorage.setItem('username', this.credentials.username)
        this.$store.dispatch('login') // 로그인 완료
        this.$store.dispatch('getUser')
      })
      .then(() => {
        this.$router.push({name: 'Home'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.needToLogin {
  width: 400px;
  margin: 8px;
}
.loginForm .border{
  width: 400px;
  height: 220px;
  margin: 16px;
  padding: 40px;
}
.loginForm div {
  padding: 8px;
}
.loginForm .input { 
  text-align: left;
}
.loginForm button {
  margin: 8px;
  text-align: right;
}
</style>