<template>
  <div>
    <div>
      <span>{{ review.title }}</span>
      | <span>{{ review.user }}</span>
      | <span class="text-end">{{ review.created_at| date }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Review',
  props: {
    review: Object,
  },
  filters: {
    date(value) {
      console.log(value)
      console.log(typeof value)
      return value.substring(0,10) + " " + value.substring(11,13) + "시 " + value.substring(14,16) + "분"
    },
    getUser(value) { // user.pk로 사람의 정보를 가져오는 함수
      console.log(value)
    }
  }
}
</script>

<style>

</style>