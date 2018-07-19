<template>
    <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <l-marker :lat-lng="marker"></l-marker>
    </l-map>
</template>

<script>
//=====================Fix Marker=======================================
delete L.Icon.Default.prototype._getIconUrl

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
    iconUrl: require("leaflet/dist/images/marker-icon.png"),
    shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
})
//========================================================================

import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";


export default {
    data(){
        return {
            zoom:15,
            center: L.latLng(0, 0),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(0, 0)
        }
    },
    components: { 
        LMap,
        LTileLayer,
        LMarker
    },
    methods:{
        initCurrentPosition(position){
            this.center = L.latLng(position.coords.latitude, position.coords.longitude);
            this.marker = L.latLng(position.coords.latitude, position.coords.longitude);
        }
    },
    created(){
        // One-shot position request.
        navigator.geolocation.getCurrentPosition(this.initCurrentPosition);
    }
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
}
</style>


