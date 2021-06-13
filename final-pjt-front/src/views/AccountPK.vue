<template>
  <div class="my-3 container">
    <!-- 똑같은 문제!!! created로 user 갱신되기 전에 component로 보내버리네?? -->
    <AccountCard :user="user" />
  </div>
</template>

<script>
import AccountCard from '@/components/AccountCard.vue'
// import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'AccountPK',
  components: {
    AccountCard,
  },
  props: {
    pk: {},
  },
  data: function () { return {
    user: {},
  }},
  created: function () {
    // this.user = this.users.filter(user => {
    //   return user.id==this.pk
    // })[0]
    this.user = this.$store.getters.getUserObjectById(this.pk)
  },
  computed: {
    ...mapState([
      'users'
    ])
  },
}
</script>

<style>

</style>