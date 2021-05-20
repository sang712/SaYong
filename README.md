# 

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

