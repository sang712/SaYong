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
    // users: [],
  }},
  created: function () {
    this.user = this.users.filter(user => {
      return user.id==this.pk
    })[0]
    // console.log(this.user)
    
    // axios.get(`http://127.0.0.1:8000/accounts/${this.pk}/`)
    //   .then(res => {
    //     this.user = res.data
    //     console.log(this.user)
    //   })
    //   .catch(err => {console.log(err)})
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