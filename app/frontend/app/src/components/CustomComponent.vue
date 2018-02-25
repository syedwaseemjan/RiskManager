<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{header}}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          {{content}}
          <div>{{ resource }}</div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'CustomComponent',
  props: ['header', 'content'],
  data () {
    return {
    }
  },
  watch: {
    viewToggleOther (bool) {
      this.setToggle('other', bool)
    }
  },
  methods: {
    setToggle: function (name, bool) {
      console.log('Toggle Called')
      // this.$store.commit('setToggle', [name, bool])
    }
  },
  computed: {
    resource () {
      // To display `resourceOne` value from the backend
      return this.$store.state.resource
    }
  },
  mounted () {
    this.$store.dispatch('fetchAllRisks')
  }
}
</script>

<style lang="sass" scoped>


</style>
