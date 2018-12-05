
            function activatePlacesSearch(){

                var input = document.getElementById('searchtextfield');

                var autocomplete = new google.maps.places.Autocomplete(input);
                google.maps.event.addListener(autocomplete, 'place_changed', function () {

                    var place = autocomplete.getPlace();
                    var pname = place.name;
                    var plat = place.geometry.location.lat();
                    var plng = place.geometry.location.lng();
                    //alert("For *"+pname+"* Latitude is: *"+plat+"* and Longitude is: *"+plng+"*");
                    document.getElementById("latitude").value=plat;
					          document.getElementById("longitude").value=plng;
                    document.getElementById("placename").value=pname;
					          initMap(pname,plat,plng);
                    //alert(input)
                    $('#myModal').modal('show');

                });
            }

            var np;
            function initMap(pname,plat,plng) {
                var uluru =  {lat: plat, lng: plng};
                var map = new google.maps.Map(
                    document.getElementById('map'), {zoom: 15, center: uluru});
                var marker = new google.maps.Marker({
                    position: uluru,
                    title: pname,
                    draggable: true,
                    map: map
                });
                google.maps.event.addListener(marker, 'dragend', function (event) {
                    var nplat = event.latLng.lat();
                    var nplng = event.latLng.lng();
                    var npname = getplace(nplat,nplng);
                    alert("For *"+npname+"* Latitude is: *"+nplat+"* and Longitude is: *"+nplng+"*");
                });
                function getplace(nplat,nplng) {
                    var latlng = new google.maps.LatLng(nplat, nplng);
                    var geocoder = geocoder = new google.maps.Geocoder();
                    geocoder.geocode({ 'latLng': latlng },
                    function (results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                            if (results[1]) {
                            np = results[1].formatted_address;
                            }
                        }
                    });

                }
            }
