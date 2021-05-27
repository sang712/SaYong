<template>
  <div class="container">
    <h1>Signup</h1>
    <div class="signupForm d-flex row justify-content-center">
      <div class="border border-secondary rounded-3">
        <div class="input position-relative">
          <span for="username" class="align-middle">사용자 이름: </span>
          <input type="text" id="username" v-model="credentials.username" class="position-absolute end-0">
        </div>
        <div class="input position-relative">
          <span for="password" class="align-middle">비밀번호: </span>
          <input type="password" id="password" v-model="credentials.password" class="position-absolute end-0">
        </div>
        <div class="input position-relative">
          <span for="passwordConfirm" class="align-middle">비밀번호 확인: </span>
          <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" class="position-absolute end-0">
        </div>
      <button @click="signup(credentials)" class="btn btn-success">가입하기</button>
      </div>
    </div>
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
.signupForm .border{
  width: 400px;
  height: 240px;
  margin: 16px;
  padding: 40px;
}
.signupForm div {
  padding: 8px;
}
.signupForm .input { 
  text-align: left;
}
.signupForm button {
  margin: 8px;
  margin-top: 20px;
  text-align: right;
}
</style>