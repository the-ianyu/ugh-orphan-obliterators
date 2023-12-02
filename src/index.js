import { createClient } from '@google/maps';
import GetLocation from 'public/currentlocation.js'

export default async function getRoutes() {
    console.log("success");
    const googleMapsClient = require('@google/maps').createClient({
        key: 'key',
        Promise: Promise,
    });

    let templat, templong;
    if ($w('#origin').valid == true) {
        templat = $w('#origin').value.latitude;
        templong = $w('#origin').value.longitude;
    } else {
        templat = GetLocation()[0];
        templong = GetLocation()[1];
    }
    console.log([templat, templong]);
    const map = new googleMapsClient.createMap({
        div: '#map',
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    });

    const directionsRenderer = googleMapsClient.createDirectionsRenderer({
        map: map,
    });

    const origin = `${templat},${templong}`;
    const destination = `${$w('#destination').value.latitude},${$w('#destination').value.longitude}`;

    const request = {
        origin: origin,
        destination: destination,
        travelMode: 'driving',
        provideRouteAlternatives: true,
    };

    googleMapsClient
        .directions(request)
        .asPromise()
        .then((response) => {
            const { status, json } = response;
            if (status === 200) {
                directionsRenderer.render(json);
            } else {
                console.error('Directions request failed. Status: ' + status);
            }
        })
        .catch((error) => {
            console.error('Error occurred while fetching directions:', error);
        });
}
