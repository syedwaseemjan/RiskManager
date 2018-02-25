import axios from 'axios'


let env = document.querySelector('[name=env]').getAttribute('value');
env = ((env) ? '/'+env : '');

let $backend = axios.create({
    baseURL: `${env}/api/v1`,
    timeout: 5000,
    headers: {'Content-Type': 'application/json'}
})

$backend.interceptors.response.use(function (response) {
    return response
  }, function (error) {
    console.log(error)
    return Promise.reject(error)
  });

export default {

  fetchAllRisks () {
    
    return $backend.get(`risks`)
      .then(response => response.data)
  },

  fetchRisk (resourceId) {
    return $backend.get(`risks/${resourceId}`)
      .then(response => response.data)
  }
}
