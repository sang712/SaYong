<template>
  <div class="reviewList">
    <h2>This is a review page.</h2>
    <Review v-for="(review, idx) in reviews" :review="reviews[idx]" :key="idx"/>
  </div>
</template>

<script>
import axios from 'axios'
import Review from '@/components/Review.vue'

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
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/community/review/',

    })
    .then((res) => {
      console.log(res)
      this.reviews = res.data
    })
  }
}
</script>

<style>

</style>