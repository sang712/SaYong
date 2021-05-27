<template>
  <div class="reviewList">
    <h1 class="pageTitle">지금까지 작성된 리뷰를 확인해보세요!</h1>
    
    <Review v-for="(review, idx) in reviews" :review="review" :key="idx"/>
  </div>
</template>

<script>
import axios from 'axios'
import Review from '@/components/Review.vue'
// import { mapState } from 'vuex'

export default {
  name: 'ReviewList',
  components: {
    Review,
  },
  data: function () {
    return {
      reviews: [],
    }
  },
  created: function() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/review/',
      headers: this.$store.getters.setToken,
    })
    .then((res) => {
      // console.log(res)
      this.reviews = res.data
    })
  // },
  // computed: function () {
  //   axios({
  //     method: 'get',
  //     url: 'http://127.0.0.1:8000/community/review/',
  //     headers: this.$store.getters.setToken,
  //   })
  //   .then((res) => {
  //     // console.log(res)
  //     this.reviews = res.data
  //   })
  },
}
</script>

<style>
.pageTitle {
  margin-top: 15px;
}
</style>