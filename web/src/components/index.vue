<template>
    <div class="w-100 h-100">
        <search></search>
        <l-map :zoom="zoom" :center="center" @update:zoom="onUpdateZoom">
            <l-control-zoom :position="'bottomright'"/>
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker :lat-lng="marker"></l-marker>
            <div v-for="item in markerTwitter"><l-marker :lat-lng="item.coordinates" :icon="item.icon"></l-marker></div>
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
            twIcon:require("@/assets/icon/twitter.png"),
            twIconPoint: L.icon({
                iconUrl: require("@/assets/icon/twitterPoint.png"),
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
        },
        onUpdateZoom(zoom){
            this.zoom = zoom;
            this.buildMarker(this.getMarkers, zoom);
        },
        buildMarker(value, zoom){
            this.markerTwitter.splice(0,this.markerTwitter.length);
            for (let i = 0; i < value.length; i++){
                var data = value[i];
                var icon = null;
                if(zoom > 12){
                    icon = new L.DivIcon({
                        html: '<span class="speech-bubble labelIcon"><img class="twIcon" src='+this.twIcon+'>'+data.text+'</span>'
                    });
                }
                else{
                    icon = this.twIconPoint;
                }
                
                var temp = {
                    coordinates: L.latLng(data.coordinates[0], data.coordinates[1]),
                    icon: icon
                }
                this.markerTwitter.push(temp);
            }
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
            
            this.buildMarker(value , this.zoom);
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

        /*var data = {
            coordinates: [13.73245446, 100.58543444],
            text:'tesetstesasdadasdadasdadasdasdasdadasdadzdsdasdaste'
        };
        console.log(data.text, LMap.mapObject);

        var icon = new L.DivIcon({
            className: 'my-div-icon',
            html: '<span class="speech-bubble labelIcon"><img class="twIcon" src='+this.twIcon+'>'+data.text+'</span>'
        })

        var temp = {
            coordinates: L.latLng(data.coordinates[0], data.coordinates[1]),
            icon: icon
        }
        this.markerTwitter.push(temp);*/


    }
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
}
.twIcon {
    width: 40px;
    height: 40px;
    float: left;
    margin-right: 8px;
}

.labelIcon {
    font-size: 16px;
    position: absolute;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, 100%);
    transform: translate(-50%, -100%);
    max-width: 300px;
    word-wrap: break-word;
    padding: 10px;
}

.speech-bubble {
	background: #ffffff;
	border-radius: .4em;
}

.speech-bubble:after {
	content: '';
	position: absolute;
	bottom: 0;
	left: 50%;
	width: 0;
	height: 0;
	border: 15px solid transparent;
	border-top-color: #ffffff;
	border-bottom: 0;
	margin-left: -15px;
	margin-bottom: -15px;
}
</style>


