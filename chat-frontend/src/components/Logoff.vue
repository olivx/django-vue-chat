<template>
  <div class="row">
    <div class="pull-right">
      <a class="link" href="#" @click="logoff">
        Logoff
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Logoff',
  methods: {
    logoff () {
      sessionStorage.removeItem('auth_token')
      this.$router.push('/auth')
    }
  }
}
</script>

<style scoped>
  .pull-right {
    flex: 1;
    min-width: 30%;
    max-width: 30%;
    padding: 5px;
  }
  .row {
    padding: 10px;
    display: flex;
    flex-flow: row-reverse;
    background-color: #fbfbfb;
  }
</style>
