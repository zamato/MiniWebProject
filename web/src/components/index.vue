<template>
  <div id='map'>12354677777777</div>
</template>

<script>
//import 'mapbox-gl/dist/mapbox-gl.css'
//import mapboxgl from 'mapbox-gl/dist/mapbox-gl.js'

export default {
  mounted() {
    console.log('mounted');
    /*mapboxgl.accessToken = "<your access token here>";
    var map = new mapboxgl.Map({
      container: "map", // container id
      style: "mapbox://styles/mapbox/streets-v9", // stylesheet location
      center: [-74.5, 40], // starting position [lng, lat]
      zoom: 9 // starting zoom
    });*/
  }
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
#map {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;
}
</style>


