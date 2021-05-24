<template>
  <div id="app">
    <div id="nav" class="bg-light">
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> -->
      <nav class="navbar navbar-expand-lg navbar-light bg-light d-flex justify-content-between">
        <div class="container-fluid">
          <!-- <a class="navbar-brand" href="#">Navbar</a> -->
          <div class="p-2">
            <router-link to="/">메인페이지</router-link>
          </div>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item p-2">
                <router-link :to="{ name: 'About' }">추천페이지</router-link>
              </li>
              <li class="nav-item p-2">
                <router-link :to="{ name: 'ReviewList' }">리뷰페이지</router-link>
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li v-if="this.$store.state.isLogin" class="nav-item p-2">
                <router-link :to="{ name: 'Account' }">내 프로필</router-link>
              </li>
              <li v-else class="nav-item p-2">
                <router-link :to="{ name: 'Signup' }">회원가입</router-link>
              </li>
              <li v-if="!this.$store.state.isLogin" class="nav-item p-2">
                <router-link :to="{ name: 'Login' }">로그인</router-link>
              </li>

            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success p-0" type="submit">검색</button>
            </form>
          </div>
        </div>
      </nav>
    </div>
    <!-- 홈으로 이어짐 -->
    <router-view/>
    <div id="footer" class="bg-secondary" style="height: 200px;">
      <div class="container">
        Footer
      </div>
      <div class="container">
        법률정보 | 이용약관 | 회사소개
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  created() {
    this.$store.dispatch('getMovieList')
    this.$store.dispatch('getUserList')
    this.$store.dispatch('getGenreList')
    this.$store.dispatch('isLogin') // 로그인 상태확인
  },
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #020715;
}

#nav {
  padding: 0px;
}

#nav a {
  font-weight: bold;
  color: #020715;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
