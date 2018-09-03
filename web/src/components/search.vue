<template>
    <div id="searchBlock" class="d-flex justify-content-center mt-4">
        <div class="input-group mx-3 mb-3 searchContent d-flex flex-column">
            <div class="d-flex">
                <input id="searchInput" type="text" class="form-control" placeholder="Search" aria-describedby="button-addon2" v-model="inputData" @keyup.enter="onSearch(inputData)" @keypress="filterText" @focus="isFocusInput=true" @blur="onUnFocus">
                <div class="input-group-append">
                    <button class="btn btn-light" type="button" id="button-addon2" @click="onSearch(inputData)">Search</button>
                </div>
            </div>
            <div v-if="isFocusInput" class="form-group">
                <div v-for="item in getLastSearch" class="optionSearch p-2 d-flex align-items-center" @click="onSearch(item)">{{item}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  data() {
    return {
      inputData: "",
      isFocusInput: false,
      lastSearch: []
    };
  },
  methods: {
    ...mapActions([
        'searchData',
        'saveLastSearch',
        'loadLastSearch'
    ]),
    filterText(evt){
        var theEvent = evt || window.event;
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode( key );
        var regex = /\S/;
        if( !regex.test(key) ) {
            theEvent.returnValue = false;
            if(theEvent.preventDefault) theEvent.preventDefault();
        }
    },
    onUnFocus(){
        var vue = this;
        setTimeout(()=>{
            vue.isFocusInput = false;
        },200)
    },
    onSearch(text) {
        this.inputData = text;
        //unfocus
        document.getElementById("searchInput").focus();
        // search
        if(text.length > 0){
            this.searchData(text);
            this.saveLastSearch(text);
        }
    }
  },
  computed:{
    ...mapGetters([
        'getLastSearch'
    ])
  },
  created(){
        this.loadLastSearch();
  }
};
</script>

<style scoped>
    #searchBlock {
        position: absolute;
        z-index: 999;
        width: 100%;
    }
    #searchBlock .searchContent {
        max-width: 500px;
    }
    #searchBlock input {
        box-shadow: none;
    }
    #searchBlock button {
        margin-left: 1px;
    }
   
    #searchBlock .optionSearch {
        height: 40px;
        background-color: white;
    }
    #searchBlock .optionSearch:hover {
        background-color: gray;
    }
</style>




