import Vue from 'vue'

export default {

  setRisk: function (state, value) {
    state.risk = value.data
  },
  setRisks: function (state, value) {
    state.risks = value.data
  }
}

