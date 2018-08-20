import Vue from 'vue'
import Vuex from 'vuex'
import TwitterMarker from './twitterMarker'
import LastSearch from './lastSearch'
Vue.use(Vuex)
const debug = process.env.NODE_ENV !== 'production'
export default new Vuex.Store({
  modules: {
    TwitterMarker,
    LastSearch
  },
  strict: debug
})
