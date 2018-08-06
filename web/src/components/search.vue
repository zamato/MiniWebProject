<template>
    <div id="searchBlock" class="d-flex justify-content-center mt-4">
        <div class="input-group mb-3 searchContent">
            <input type="text" class="form-control" placeholder="Search" aria-describedby="button-addon2" v-model="inputData" @keyup.enter="onSearch">
            <div class="input-group-append">
                <button class="btn btn-light" type="button" id="button-addon2" @click="onSearch" >Search</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      inputData: ""
    };
  },
  methods: {
    onSearch() {
      // search
      this.$http
        .get("https://maps.googleapis.com/maps/api/geocode/json?address=" + this.inputData + "&key=AIzaSyBGIA6vuByllFOeHv0buIlHy9UZqOsSM04")
        .then(
          result => {
            console.log(result);
            this.$http.post(
              "http://localhost:5000/api/v1/getInfoTwitter",{
                  text: this.inputData,
                  geo: result.body.results[0].geometry.location
              },
              result => {
                  console.log(result);
              },
              error => {
                  console.log(error);
              }
            );
          },
          error => {
            console.log(error);
          }
        );
    }
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
</style>




