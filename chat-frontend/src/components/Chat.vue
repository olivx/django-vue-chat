<template>
  <h1>Welcome to DjangoVue Chat, {{ this.username }} </h1>
</template>

<script>
export default {
  data () {
    return {
      username: sessionStorage.getItem('username')
    }
  }
}
</script>
