<template>
  <div>
    <p>영화 상세페이지</p>
    <div class="card mb-3 container">
      <div class="row g-0 justify-content-between">
        <div class="col-md-4 row p-0">
          <img :src=movie.poster_path class="col-12 p-0" alt="movie_poster">
          <!-- MovieCard.vue의 찜 버튼이 추가되면 여기에도 추가하기 -->
        </div>
        <div class="col-md-8">
          <div class="card-body text-start">
            <h1 class="card-title">{{ movie.title }}</h1>
            <span>{{ movie.release_date| year }} | </span>
            <span>{{ movieGenres }}</span>
            <br>
            <span class="card-text">평균 점수 : {{ movie.vote_average }} | </span>
            <span>
              내 점수 : 
              <StarRating :grade="gradeNumber" :maxStars="10" :hascounter="true" :movie="movie" :user="user"/>
            </span>
            <hr>
            <h4>줄거리</h4>
            <p v-if="movie.overview" class="card-text">{{ movie.overview }}</p>
            <p v-else>등록된 줄거리가 없습니다.</p>
          </div>
        </div>
<!-- 여기서부터 영화와 관련된 객체들(별점, 리뷰, 찜한 사람)을 작성 -->
        <div class="my-3">
          <div class="accordion" id="accordionPanelsStayOpenExample">
            <div class="accordion-item">
              <h2 class="accordion-header" id="panelsStayOpen-headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
                  별점 목록
                </button>
              </h2>
              <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
                <div class="accordion-body">
                  <div class="table" v-if="!ratings.some(rating => {return rating.movie === movie.id})">별점이 없습니다</div>
                  <table class="table" v-else>
                    <thead>
                      <tr>
                        <th scope="col">id</th>
                        <th scope="col">user</th>
                        <th scope="col">rank</th>
                        <th scope="col">created_at</th>
                      </tr>
                    </thead>
                    <tbody v-for="(rating, idx) in ratings" :key="idx">
                      <tr v-if="rating.movie === movie.id">
                        <th scope="row">{{ rating.id }}</th>
                        <td>{{ $store.getters.getUserObjectById(rating.user).username }}</td>
                        <td>{{ rating.rank }}</td>
                        <td>{{ rating.created_at }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="true" aria-controls="panelsStayOpen-collapseTwo">
                  리뷰 목록
                </button>
              </h2>
              <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingTwo">
                <div class="accordion-body">
                  <div class="table" v-if="!reviews.some(review => {return review.movie === movie.id})">리뷰가 없습니다</div>
                  <table class="table" v-else>
                    <thead>
                      <tr>
                        <th scope="col">id</th>
                        <th scope="col">title</th>
                        <th scope="col">user</th>
                        <th scope="col">comment_set.length</th>
                        <th scope="col">like_users.length</th>
                        <th scope="col">created_at</th>
                      </tr>
                    </thead>
                    <tbody v-for="(review, idx) in reviews" :key="idx">
                      <tr v-if="review.movie === movie.id">
                        <th scope="row">{{ review.id }}</th>
                        <td>{{ review.title }}</td>
                        <td>{{ $store.getters.getUserObjectById(review.user).username }}</td>
                        <td>{{ review.comment_set.length }}</td>
                        <td>{{ review.like_users.length }}</td>
                        <td>{{ review.created_at }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header" id="panelsStayOpen-headingThree">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="true" aria-controls="panelsStayOpen-collapseThree">
                  찜한 사람 목록
                </button>
              </h2>
              <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingThree">
                <div class="accordion-body">
                  <div class="table" v-if="!movie.favorite_users.length">찜한 사람이 없습니다</div>
                  <div v-else v-for="(favorite_user, idx) in movie.favorite_users" :key="idx">
                    <ShortAccountCard :user="$store.getters.getUserObjectById(favorite_user)"/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div>
          <!-- Button trigger modal -->
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#reviewAddModal">
            리뷰 작성
          </button>
          <!-- Modal -->
          <div class="modal fade" id="reviewAddModal" tabindex="-1" aria-labelledby="reviewAddModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="reviewAddModalLabel">리뷰 작성</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <div class="loginForm d-flex justify-content-center row">
                    <div class="input-group position-relative col-12">
                      <div for="title" class="align-middle">리뷰 제목: </div>
                      <input type="text" id="title" v-model="reviewCreating.title" class="mr-2 form-control" style="width: auto;">
                    </div>
                    <div class="input-group position-relative col-12">
                      <div for="content" class="align-middle">내용: </div>
                      <textarea type="content" id="password" v-model="reviewCreating.content" class="form-control" style="width: auto;" rows="5"/>
                    </div>
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
                  <button @click="reviewCreate()" data-bs-dismiss="modal" class="btn btn-primary">등록</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapState } from 'vuex'
import StarRating from '@/components/StarRating.vue'
import ShortAccountCard from '@/components/ShortAccountCard.vue'

export default {
  name: 'MovieDetail',
  components: {
    StarRating,
    ShortAccountCard,
  },
  data: function() {
    return {
      movie: [],
      movieGenres: [],
      gradeNumber: 0,
      reviewCreating: {
        title: null,
        movie: null,
        content: null,
        user: null,
      },
      message: '',
    }
  },
  props: {
    'pk': Number,
    'user': Object,
  },
  methods: {
    reviewCreate: function() {
      this.reviewCreating.user = this.user.id
      this.reviewCreating.movie = this.pk
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/${this.movie.id}/review/`,
        data: this.reviewCreating,
        headers: this.setToken,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Review', params: {review: res.data, pk: res.data.id}})
      })
      .catch(err => {
        console.log("제목또는 내용이 비어있습니다.",err.response.data)
      })
    },
  },
  created() {
    this.movie = this.movies.find((movie) => {
      return (movie.id===Number(this.pk))
    })
    this.movieGenres = this.movie.genres.map(genre => {
      return genre.name
    }).join('/')
    const ratingList = this.movie.rating_set.filter(rating => {
      return rating.user === this.user.id
    })
    this.gradeNumber = ratingList.reduce((acc, num) => {
      return acc*0 + num.rank
    }, 0)
  },
  computed: {
    ...mapState([
      'movies',
      'genres',
      'ratings',
      'reviews',
    ]),
    ...mapGetters([
      'setToken',
    ])
  },
  filters: {
    year: function(value) {
      return value.substring(0,4)
    },
    popularity: (value) => {
      return value * 1000
    }
  }
}
</script>

<style>

</style>