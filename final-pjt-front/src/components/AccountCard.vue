<template>
  <div class="container">
    <div id="userinfo">
      username: {{ user }}
    </div>
    <div id="followinfo">
      follower / following
    </div>
    <div id="myreviews">
      myreviews
    </div>
    <div id="mycomments">
      mycomments
    </div>
    <div id="mylikes">
      mylikes
    </div>
    <div id="myfavorites">
      myfavorites
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccountCard',
  props: {
    user: {},
  },
}
</script>

<style>

</style>