<template>
  <div class="my-3 container">
    <AccountCard v-for="(user, idx) in users" :user="user" :key="idx"/>
  </div>
</template>

<script>
import AccountCard from '@/components/AccountCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Account',
  components: {
    AccountCard,
  },
  data: function () {return {
    // users: [],
  }},
  // props: {
  //   users: [],
  // },
  computed: {
    ...mapState([
      'users'
    ])
  },
}
</script>

<style>

</style>