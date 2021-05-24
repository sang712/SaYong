<template>
  <div>
    <div>
      <span>{{ review.title }}</span>
      | <span>{{ review.user }}</span>
      | <span class="text-end">{{ review.created_at| date }}</span>
      | <span>{{ review.movie| getMovie }}</span>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'Review',
  props: {
    review: Object,
    user: Object,
    movie: Object,
  },
  filters: {
    date: function(value) {
      console.log(value)
      console.log(typeof value)
      return value.substring(0,10) + " " + value.substring(11,13) + "시 " + value.substring(14,16) + "분"
    },
    getUser: function(value) { // user.pk로 사람의 정보를 가져오는 함수
      console.log(value)
    },
    getMovie: function(value) {
      return this.movie[value]
    },
  },
  computed: {
    ...mapState([
      'movies',
    ])
  }
}
</script>

<style>

</style>