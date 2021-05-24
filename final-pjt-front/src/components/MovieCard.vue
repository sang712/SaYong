<template>
  <div class="m-0 py-1 col-2">
     <!-- style="width: 18rem;"> -->
     <!-- pk를 그대로 넣으면 영화가 한 개씩 밀려 임시적으로 -1한 값으로 영화를 불러옴 -->
    <router-link :to="{ name: 'MovieDetail', params: { pk: movie.id-1 } }">
      <div class="card bg-light" style="height: 100%;">
        <img :src=movie.poster_path class="card-img" alt="...">
        <div class="card-img-overlay">
          <!-- 카드위에 오버레이 될 내용 여기에 좋아요 버튼 추가-->
        </div>
        <p class="card-title m-2 mx-3 text-start">{{ movie.title }}</p>
      </div>
    </router-link>
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