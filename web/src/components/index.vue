<template>
    <div class="w-100 h-100">
        <search></search>
        <l-map :zoom="zoom" :center="center">
            <l-control-zoom :position="'bottomright'"/>
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker :lat-lng="marker"></l-marker>
            <div v-for="item in markerTwitter"><l-marker :lat-lng="item" :icon="twIcon"></l-marker></div>
        </l-map>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LControlZoom } from "vue2-leaflet";
import Search from "./search.vue";
import { mapGetters } from 'vuex';

export default {
    data(){
        return {
            twIcon: L.icon({
                iconUrl: require("@/assets/icon/twitter.png"),
                shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
                iconSize: [40, 40],
                iconAnchor: [20, 20]
            }),
            zoom:15,
            center: L.latLng(0, 0),
            url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            marker: L.latLng(0, 0),
            markerTwitter: []

        }
    },
    components: { 
        LMap,
        LTileLayer,
        LMarker,
        LControlZoom,
        Search
    },
    methods:{
        initCurrentPosition(position){
            this.center = L.latLng(position.coords.latitude, position.coords.longitude);
            this.marker = L.latLng(position.coords.latitude, position.coords.longitude);
        }
    },
    computed: {
        ...mapGetters([
            'getLocation',
            'getMarkers'
        ])
    },
    watch:{
        getMarkers(value){
            this.markerTwitter.splice();

            for (let i = 0; i < value.length; i++) 
                this.markerTwitter.push(L.latLng(value[i][0], value[i][1]));
            
        },
        getLocation(value){
            this.center = L.latLng(value.lat, value.lng);
            this.marker = L.latLng(value.lat, value.lng);
            
        }
    },
    created(){
        //=====================Fix Marker=======================================
        delete L.Icon.Default.prototype._getIconUrl

        L.Icon.Default.mergeOptions({
            iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
            iconUrl: require("leaflet/dist/images/marker-icon.png"),
            shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
        });
        //========================================================================
        //=====================Close Defalut Zoom=======================================
        L.Map.mergeOptions({
            zoomControl: false
        })
        //========================================================================
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


