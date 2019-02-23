<template>
  <div>
    <Logout />
    <div class="text-wellcome">
      <h1>Welcome to DjangoVue Chat,
        <span class="text-info">{{ this.username }}</span>
      </h1>
    </div>
    <div class="row row-flex">
      <div class="col-4 flex-item"> users </div>
      <div class="col-8 flex-item">chat </div>
    </div>

    <footer class="footer">
      <p> oliveiravicente.net@gmail.com </p>
    </footer>
  </div>
</template>

<script>
import Logout from '@/components/Logout'

export default {
  data () {
    return {
      username: sessionStorage.getItem('username')
    }
  },
  components: {
    Logout
  },
  mounted () {
    console.log(process.env.ROOT_API)
  }
}
</script>
