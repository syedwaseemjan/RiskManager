<template>
  <section>

    <div class="card">
      <header class="card-header">
        <p class="card-header-title">
          {{title}}
        </p>
      </header>
      <div class="card-content">
        <div class="content">
          <ul class="row" v-for="risk in getRisks()">
            <router-link tag="li" activeClass='is-active' :to="{ name: 'risk', params: { riskId: risk.id }}"><a>{{ risk.name }}</a></router-link>
          </ul>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'Home',
  data () {
    return {
      title: 'Risk Manager'
    }
  },
  methods: {
    getRisks () {
      return this.$store.state.risks
    }
  },
  mounted () {
    this.$store.dispatch('fetchAllRisks')
  }
}
</script>

<style lang="sass" scoped>

</style>
