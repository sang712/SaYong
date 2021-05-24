<template>
  <div class="reviewList">
    <h2>This is a review page.</h2>
    <button>리뷰 작성하기</button>
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

    })
      .then((res) => {
        console.log(res)
        this.reviews = res.data
      })
  },
  // computed: {
  //   ...mapState([
  //     'movies',
  //   ])
  // },
}
</script>

<style>

</style>