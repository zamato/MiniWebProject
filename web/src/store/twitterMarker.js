import Vue from 'vue'

const state = {
    curLoc: [],
    marker: []
}

const mutations = {
    SEARCH_DATA (state, payload) {
        state.marker = payload;
    },
    SEARCH_LOCAL (state, payload) {
        state.curLoc = payload;
    }
}

const actions = {
    searchData:({ commit }, inputData) => {
        Vue.http.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + inputData + "&key=AIzaSyBGIA6vuByllFOeHv0buIlHy9UZqOsSM04")
        .then(
            result => {
                //check if data nodata what should i do
                if(result.body.results.length > 0){
                    commit('SEARCH_LOCAL', result.body.results[0].geometry.location);

                    Vue.http.post("http://localhost:5000/api/v1/getInfoTwitter",{ text: inputData, geo: result.body.results[0].geometry.location })
                    .then(
                        result => {
                            commit('SEARCH_DATA', result.body);
                        },
                        error => {
                            console.log(error);
                        }
                    );
                }
                
            },
            error => {
                console.log(error);
            }
        );
    }
}

const getters = {
    getLocation: state => state.curLoc,
    getMarkers: state => state.marker
}

export default {
    state,
    getters,
    mutations,
    actions
}
