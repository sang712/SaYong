



# 

i. 팀원 정보 및 업무 분담 내역
ii. 목표 서비스 구현 및 실제 구현 정도
iii. 데이터베이스 모델링 (ERD)
iv. 필수 기능에 대한 설명
v. 배포 서버 URL
vi. 기타 느낀점

브레인스토밍
05.20 아이디어 회의

1. 인증 상태 토큰 만료시 자동 로그아웃 혹은 은행 홈페이지 처럼 1분 전 만료 알림, 연장 버튼 등

2. 영화를 눌렀을 때 리뷰로 갈지, 아니면 전체 리뷰를 보여줄지. 네이버 영화의 경우에는 기본적으로 영화를 눌러서 리뷰를 확인하지만, 메인 페이지에 최신 리뷰를 보여주는 칸이 있다.

3. 다크모드 적용. vuex에서 다크모드 관련 변수를 설정하고 이에 따라 홈페이지 다크모드를 껐다 켰다하는 기능. v-if/else로 적용이 가능할 것 같다. Bootstrap에 관련된 기능이 있는지 확인이 필요하다.

4. 아마 힘들겠지만 웹 접근성 표준 인증을 받을 정도를 ? 아니면 색약, 색맹 등에게 맞춘 색상 조절 기능. 





## 모델 구조

* accounts_user

| id           | field            | 설명                   |
| ------------ | ---------------- | ---------------------- |
| username     | char(150)        | 사용자 이름            |
| password     | char(150)        |                        |
| email        | char(150)        |                        |
| is_superuser | bool             |                        |
| is_staff     | bool             |                        |
| is_active    | bool             |                        |
| last_name    | char(150)        |                        |
| first_name   | char(150)        |                        |
| date_joined  | datetime         |                        |
| las_login    | datetime         |                        |
|              |                  |                        |
| followers    | manytomany(user) | 팔로우 하는 사람       |
| review_set   |                  | 사용자가 남긴 리뷰     |
| comment_set  |                  | 사용자가 남긴 코멘트   |
| like_reviews |                  | 사용자가 좋아요한 리뷰 |
|              |                  |                        |



* community_review

| id          | field      | 설명 |
| ----------- | ---------- | ---- |
| title       | char(100)  |      |
| movie_title | char(150)  |      |
| rank        | integer    |      |
| content     | text       |      |
| created_at  | datetime   |      |
| uploaded_at | datetime   |      |
|             |            |      |
| user        | foreignkey |      |
| like_users  | foreignkey |      |





## URL

### Community

* review

| URL                                | 호출 함수     | 메서드 | 역할                        |
| ---------------------------------- | ------------- | ------ | --------------------------- |
| community/review/                  | review_index  | GET    | 모든 리뷰(글) 보기          |
| community/<movie_pk>/review/       | review_create | POST   | 리뷰(글) 만들기             |
| community/review/<review_pk>/      | review_detail | GET    | 특정 리뷰(글) 보기          |
| community/review/<review_pk>/      | review_detail | PUT    | 리뷰(글) 수정               |
| community/review/<review_pk>/      | review_detail | DELETE | 리뷰(글) 지우기             |
| community/review/<review_pk>/like/ | review_like   | GET    | ‘좋아요’한 사람 보기        |
| community/review/<review_pk>/like/ | review_like   | POST   | ‘좋아요’/’좋아요 취소’ 토글 |

* rating

| URL                           | 호출 함수     | 메서드 | 역할                                    |
| ----------------------------- | ------------- | ------ | --------------------------------------- |
| community/rating/             | rating_index  | GET    | 모든 평점 보기                          |
| community/<movie_pk>/rating/  | rating_create | POST   | 평점 만들기                             |
|                               |               |        | 특정 영화 모든 평점 보기(영화에서 지원) |
| community/rating/<rating_pk>/ | rating_detail | GET    | 특정 평점 보기                          |
| community/rating/<rating_pk>/ | rating_detail | PUT    | 평점 수정                               |
| community/rating/<rating_pk>/ | rating_detail | DELETE | 평점 지우기                             |

* comment

| URL                             | 호출 함수      | 메서드 | 역할                               |
| ------------------------------- | -------------- | ------ | ---------------------------------- |
| community/comment/              | comment_index  | GET    | 모든 댓글 보기                     |
|                                 |                |        | 특정 리뷰 댓글 보기(리뷰에서 지원) |
| community/<review_pk>/comment/  | comment_create | POST   | 댓글 만들기                        |
| community/comment/<comment_pk>/ | comment_detail | GET    | 특정 댓글 보기                     |
| community/comment/<comment_pk>/ | comment_detail | PUT    | 댓글 수정                          |
| community/comment/<comment_pk>/ | comment_detail | DELETE | 댓글 지우기                        |



### Movies

| URL                                       | 호출 함수      | 메서드 | 역할                                         |
| ----------------------------------------- | -------------- | ------ | -------------------------------------------- |
| movies/                                   | movie_index    | GET    | 모든 영화 보기                               |
| movies/<movie_pk>/                        | movie          | GET    | 특정 영화 보기                               |
| admin/                                    |                |        | 관리자 영화 추가 수정 삭제                   |
| movies/recommended/[**kwargs: q=’’&....]/ | recommend      | GET    | 검색어로 영화 추천 받기                      |
| movies/favorite/                          | favorite_index | GET    | 모든 영화 찜(한 목록) 보기                   |
|                                           |                |        | 특정 유저 찜한 영화 목록 보기(유저에서 지원) |
|                                           |                |        | 특정 영화 찜한 유저 목록 보기(영화에서 지원) |
| movies/<movie_pk>/favorite/               | favorite       | POST   | 영화 ‘찜’/’찜 취소’ 토글                     |



### Accounts

| URL                               | 호출 함수 | 메서드     | 역할                     |
| --------------------------------- | --------- | ---------- | ------------------------ |
| accounts/                         | signup    | GET & POST | 계정 생성화면 & 생성하기 |
| accounts/index/                   | index     | GET        | 모든 계정 보기           |
| accounts/<username>/              | profile   | POST       | 계정 정보 보기           |
| accounts/<username>/              | profile   | PUT        | 계정 정보 수정           |
| accounts/<username>/              | profile   | DELETE     | 계정 삭제                |
| accounts/follow/<account_pk>/     |           | GET        | 팔로잉, 팔로워 목록보기  |
| accounts/follow/<account_pk>/     |           | POST       | ‘팔로우’/’언팔로우’ 토글 |
| accounts/api-token-auth/          |           | POST       | JWT 토큰 받기            |
| 버튼 동작(로그아웃, Vue에서 처리) |           | POST       | 로그아웃(JWT 토큰 삭제)  |

