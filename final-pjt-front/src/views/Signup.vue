<template>
  <div class="container">
    <h1>Signup</h1>
    <div class="d-flex row justify-content-center">
      <div>
        <span for="username">사용자 이름: </span>
        <input type="text" id="username" v-model="credentials.username">
      </div>
      <div>
        <span for="password">비밀번호: </span>
        <input type="password" id="password" v-model="credentials.password">
      </div>
      <div>
        <span for="passwordConfirm">사용자 이름: </span>
        <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
      </div>
    </div>
      <button @click="signup(credentials)">가입하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
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