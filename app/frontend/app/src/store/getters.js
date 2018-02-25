export default {

  getRisk: (state) => {
    return state.risk
  },
  getRisks: (state) => {
    return state.risks
  },
  getterWithArg: (state) => (value) => {
    return state.resourceOne + value
  }
}
