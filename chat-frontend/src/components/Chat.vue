<template>
  <div>
    <Logoff />
    <div>
      <h1>Welcome to DjangoVue Chat, {{ this.username }} </h1>
    </div>
  </div>
</template>

<script>
import Logoff from '@/components/Logoff'

export default {
  data () {
    return {
      username: sessionStorage.getItem('username')
    }
  },
  components: {
    Logoff
  }
}
</script>
