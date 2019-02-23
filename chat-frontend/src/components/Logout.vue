<template>
  <div class="row">
    <div class="pull-right">
      <button @click="logout" class="btn btn-outline-info">
        Log out
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Logout',
  methods: {
    logout () {
      let token = sessionStorage.getItem('auth_token')
      let headersToken = {Authorization: `Token ${token}`}
      axios.post(`${process.env.ROOT_API}/auth/token/logout/`, {}, {headers: headersToken})
        .then(resp => {
          sessionStorage.removeItem('auth_token')
          this.$router.push('/auth')
        })
        .catch(resp => {
          console.log(resp)
        })
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
