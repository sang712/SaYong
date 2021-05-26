<template>
  <span class="rating">
    <span v-if="hascounter" class="info counter">
      <span class="score-rating">{{ stars }}</span>
    </span>
    <span class="list">
      <li @click="rate(star)" v-for="star in maxStars" :class="{ 'active': star <= stars }" :key="star.stars" class="star">
      <i :class="star <= stars ? 'fas fa-star' : 'far fa-star'"></i> 
      </li>
    </span>
  </span>
</template>
<script>
import axios from 'axios'
export default {
  name: 'StarRating',
  props: ['grade', 'maxStars', 'hascounter', 'movie', 'user'],
  data() {
    return {
      stars: this.grade
    }
  },
  methods: {
    rate(star) {
      if (typeof star === 'number' && star <= this.maxStars && star >= 0) {
        this.stars = this.stars === star ? star - 1 : star
      }
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/${this.movie.id}/rating/`,
        headers: this.$store.getters.setToken,
        data: {
          rank: star,
          movie: this.movie.id,
          user: this.user.id,
        }
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
}
</script>

<style>
.rating {
  /* display: flex;
  flex-direction: column;
  align-items: center; */
  padding: 0px;
  color: #b7b7b7;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 6px 33px rgba(19, 18, 18, 0.09);
}
.rating .list {
  padding: 0;
  margin: 0 0 0 10px ;
}
.rating .list:hover .star {
  color: #ffe100;
}
.rating .list .star {
  display: inline-block;
  font-size: 18px;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
}
.rating .list .star:hover ~ .star:not(.active) {
  color: inherit;
}
.rating .list .star:first-child {
  margin-left: 0;
}
.rating .list .star.active {
  color: #ffe100;
}
.rating .info {
  color: #020715;
  margin-top: 0px;
  font-size: 16px;
  text-align: right;
  /* display: table; */
}
/* .rating .info .divider {
  margin: 0 5px;
  font-size: 30px;
}
.rating .info .score-max {
  font-size: 12px;
  vertical-align: sub;
} */
</style>