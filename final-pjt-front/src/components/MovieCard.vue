<template>
  <div class="m-3" style="width: 18rem;">
    <div class="card bg-light">
      <img :src=movie.poster_path class="card-img" alt="...">
      <div class="card-img-overlay">
        <!-- 카드위에 오버레이 될 내용 -->
      </div>
      <h5 class="card-title m-2 mx-3 text-start">{{ movie.title }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  data: function () {
    return {

    }
  },
  props: {
    movie: Object,
    // title: '',
    // explanation: '',
  }
}
</script>

<style>

</style>