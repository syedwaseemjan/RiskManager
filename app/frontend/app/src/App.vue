<template>
<div>

    <nav>
        <router-view name="subnavbar"></router-view>
    </nav>

    <section class="section">
      <transition name="fade">
        <div class="container">

          <router-view name="main"></router-view>

        </div>
      </transition>
    </section>

</div>
</template>

<script>

export default {
  name: '',
  computed: {
    isLoading () {
      return this.$store.state.isLoading
    }
  }
}
</script>

<style lang="sass">
// Main.sass is imported into all Components using Webpack Data Parameter

</style>
