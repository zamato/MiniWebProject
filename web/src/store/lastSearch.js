import Vue from 'vue'

const state = {
    lastSearch: []
}

const mutations = {
    UPDATE_LAST_SEARCH(state, payload) {
        state.lastSearch = payload;
    },
    ADD_LAST_SEARCH(state, payload) {
        state.lastSearch.unshift(payload);
    },
    POP_LAST_SEARCH(state) {
        state.lastSearch.pop();
    }

}

const actions = {
    loadLastSearch:({ commit, state }) => {
        if(state.lastSearch.length == 0){
            var data = Vue.cookies.get("lastSearch");
            if(data){
                commit('UPDATE_LAST_SEARCH', JSON.parse(data));
            }
        }
    },
    saveLastSearch:({ commit, state }, text) => {
        if(text.length <= 0) return;

        var index = state.lastSearch.indexOf(text);
        if(index == -1){
            
            if(state.lastSearch.length >= 5){
                commit('POP_LAST_SEARCH');
                commit('ADD_LAST_SEARCH',text);
            }
            else{
                commit('ADD_LAST_SEARCH',text);
            }
            Vue.cookies.set("lastSearch", JSON.stringify(state.lastSearch))   //return this
        }
    }
}

const getters = {
    getLastSearch: state => state.lastSearch
}

export default {
    state,
    getters,
    mutations,
    actions
}
