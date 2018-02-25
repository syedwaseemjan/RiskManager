import Vue from 'vue'
import backend from './backend'

export default {

  fetchAllRisks: function  (context) {
    backend.fetchAllRisks().then((responseData) => {
      console.log(responseData)
      context.commit('setRisks', responseData)
    })
  },

  fetchRisk: function  (context, resourceId) {
  	backend.fetchRisk(resourceId).then((responseData) => {
  		context.commit('setRisk', responseData)
  	})
  }
}
