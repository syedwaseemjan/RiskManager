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
            <div><p>Details: {{getDetails()}}</p></div><br>
            <div class="field" v-for="question in getQuestions()">
              <label class="label">{{ question.text }}</label>
              <div class="control">
                <input v-if="question.type_.name != 'enum'" :type="question.type_.name" class="input">
                <div class="select" v-if="question.type_.name == 'enum'">
                  <select>
                    <option v-for="opt in question.options" :value="opt.id">
                      {{ opt.text }}
                    </option>
                  </select>
                </div>
              </div>
            </div>

            <div class="field is-grouped">
              <div class="control">
                <button class="button is-link">Submit</button>
              </div>
              <div class="control">
                <button class="button is-text">Cancel</button>
              </div>
            </div>
        </div>
      </div>
    </div>

  </section>
</template>

<script>

export default {
  name: 'Risk',
  data () {
    return {
      title: 'Risk Manager'
    }
  },
  methods: {
    getDetails () {
      let risk = this.$store.getters.getRisk
      if (risk) {
        return risk.details
      }
      return null
    },
    getQuestions () {
      let risk = this.$store.getters.getRisk
      if (risk) {
        return risk.questions
      }
      return null
    }
  },
  mounted () {
    this.$store.dispatch('fetchRisk', this.$route.params.riskId)
  }
}
</script>

<style lang="sass" scoped>

</style>
