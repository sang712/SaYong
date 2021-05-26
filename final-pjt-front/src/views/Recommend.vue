<template>
  <div class="recommend">
    <h1 class="pageTitle">이런 영화는 어떠신가요?</h1>
    <MovieCollection v-if="recommendCollection.movies.length" :movies="recommendCollection.movies" :collectionTitle="recommendCollection.collectionTitle" :recommend="true"/>
    <h4 v-else class="my-3 text-center">아직 찜을 하신 영화가 없네요. 한 번 찜을 하러 가 볼까요?</h4>
    <MovieCollection :movies="popularCollection.movies" :collectionTitle="popularCollection.collectionTitle" :recommend="true"/>
    <MovieCollection :movies="actionCollection.movies" :collectionTitle="actionCollection.collectionTitle" :recommend="true"/>
    <MovieCollection :movies="adventureCollection.movies" :collectionTitle="adventureCollection.collectionTitle" :recommend="true"/>
  </div>
</template>

<script>
import MovieCollection from '@/components/MovieCollection.vue'
import { mapState } from 'vuex'

import _ from 'lodash'

export default {
  name: 'Recommend',
  components: {
    MovieCollection,
  },
  data: function () {
    return {
      popularCollection: {movies: [], collectionTitle: '지금 가장 핫한 인기 영화!'},
      recentCollection: {movies: [], collectionTitle: '가장 최신 영화를 만나보세요!'},
      actionCollection: {movies: [], collectionTitle: '스펙타클한 일상! 액션 영화'},
      adventureCollection: {movies: [], collectionTitle: '모험을 떠나고 싶다면! 어드벤처 영화'},
      fantasyCollection: {movies: [], collectionTitle: '상상의 나래를 펼쳐볼까요? 판타지 영화'},
      animationCollection: {movies: [], collectionTitle: ''},
      dramaCollection: {movies: [], collectionTitle: '뭉클한 감동을 느끼고 싶다면 드라마 영화'},
      horrorCollection: {movies: [], collectionTitle: ''},
      comedyCollection: {movies: [], collectionTitle: ''},
      historyCollection: {movies: [], collectionTitle: ''},
      westernCollection: {movies: [], collectionTitle: ''},
      thrillerCollection: {movies: [], collectionTitle: '가슴 졸이는 긴장감 스릴러 영화'},
      crimeCollection: {movies: [], collectionTitle: ''},
      documentaryCollection: {movies: [], collectionTitle: ''},
      sfCollection: {movies: [], collectionTitle: ''},
      mysteryCollection: {movies: [], collectionTitle: ''},
      musicCollection: {movies: [], collectionTitle: '신나게 즐기자! 음악 영화'},
      romanceCollection: {movies: [], collectionTitle: '뚜 뚜루뚜~ 뚜 뚜루뚜~ 로맨스 영화♥'},
      familyCollection: {movies: [], collectionTitle: '가슴 따뜻한 가족애를 느껴보세요 가족 영화'},
      warCollection: {movies: [], collectionTitle: '긴박한 당시의 상황을 그대로, 전쟁 영화'},
      tvCollection: {movies: [], collectionTitle: '우리 이제 TV에서 만나요! TV 영화'},
      recommendCollection: {movies: [], collectionTitle: '좋아요 하신 영화를 기반으로 추천했어요.'}
    }
  },
  computed: {
    ...mapState([
      'movies',
      'user'
    ])
  },
  mounted() {
    this.popularCollection.movies = _.shuffle(this.movies.slice(0,15))
    this.adventureCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 12})}))
    this.fantasyCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 14})}))
    this.animationCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 16})}))
    this.dramaCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 18})}))
    this.horrorCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 27})}))
    this.actionCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 28})}))
    this.comedyCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 35})}))
    this.historyCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 36})}))
    this.westernCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 37})}))
    this.thrillerCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 53})}))
    this.crimeCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 80})}))
    this.documentaryCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 99})}))
    this.sfCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 878})}))
    this.mysteryCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 9648})}))
    this.musicCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 10402})}))
    this.romanceCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 10749})}))
    this.familyCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 10751})}))
    this.warCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 10752})}))
    this.tvCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === 10770})}))
    const counter = [
      {'id': 12, count: 0},
      {'id': 14, count: 0},
      {'id': 16, count: 0},
      {'id': 18, count: 0},
      {'id': 27, count: 0},
      {'id': 28, count: 0},
      {'id': 35, count: 0},
      {'id': 36, count: 0},
      {'id': 37, count: 0},
      {'id': 53, count: 0},
      {'id': 80, count: 0},
      {'id': 99, count: 0},
      {'id': 878, count: 0},
      {'id': 9648, count: 0},
      {'id': 10402, count: 0},
      {'id': 10749, count: 0},
      {'id': 10751, count: 0},
      {'id': 10752, count: 0},
      {'id': 10770, count: 0},]
    this.user.favorite_movies.forEach(movie => {
      movie.genres.forEach(genre => {
        counter.find(genre2 => {
          return genre2.id == genre.id}).count += 1
      })
    })
    let theGenre = counter.reduce((prev, curr) => {
      if (prev.count < curr.count) {
        return curr
      }
      return prev
    })
    console.log(theGenre)
    this.recommendCollection.movies = _.shuffle(this.movies.filter(movie => {return movie.genres.some(genre=>{return genre.id === theGenre.id})}))
      this.user.favorite_movies.forEach(favorite_movie => {
        _.remove(this.recommendCollection.movies, movie => {
          return movie.id === favorite_movie.id
      })
    })
  },
}

</script>

<style>
.pageTitle {
  margin-top: 15px;
}
</style>