var map ;
var searchMarker ;
var veganPlaces = [] ;
var zerowastePlaces = [] ;


/* Map 생성 */
function initMap() {
     var defaultOptions = {
          zoom : 12 ,
          center : new google.maps.LatLng(37.5643135 , 127.0016985),
          disableDefaultUI : true ,
          zoomControl : false ,
          gestureHandling : 'greedy' ,
     }
     map = new google.maps.Map(document.getElementById("map"), defaultOptions);
     getData() ;
}

/* AJAX 통신으로 데이터 수신 */

function getData() {
    $('.button').click(function() {
        var button_id = $(this).attr('id') ;
        alert(button_id) ;
        switch(button_id) {
            case 'ZEROWASTE' :
            clearMarkers() ;
            $.ajax({
                url : '../zerowaste_data/' ,
                type : 'post' ,
                dataType : 'json' ,
                data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                success : function(zerowaste_list) {
                    $.each(zerowaste_list, function(key, value) {
                        zerowastePlaces.push(value)
                    });
                    console.log(zerowastePlaces)
                    alert('success')
                    drawMarkers(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });

            case 'ZEROWASTE_ALL' :
            $.ajax({
                url : '../zerowaste_data_all/' ,
                type : 'post' ,
                dataType : 'json' ,
                data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                success : function(zerowaste_list) {
                    $.each(zerowaste_list, function(key, value) {
                        zerowastePlaces.push(value)
                    });
                    console.log(zerowastePlaces)
                    alert('success')
                    drawMarkers(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });

            case 'REFILL_SHOP' :
            $.ajax({
                url : '../zerowaste_data_refill/' ,
                type : 'post' ,
                dataType : 'json' ,
                data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                success : function(zerowaste_list) {
                    $.each(zerowaste_list, function(key, value) {
                        zerowastePlaces.push(value)
                    });
                    console.log(zerowastePlaces)
                    alert('success')
                    drawMarkers(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });

            case 'RECYCLE' :
            $.ajax({
                url : '../zerowaste_data_recycle/' ,
                type : 'post' ,
                dataType : 'json' ,
                data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                success : function(zerowaste_list) {
                    $.each(zerowaste_list, function(key, value) {
                        zerowastePlaces.push(value)
                    });
                    console.log(zerowastePlaces)
                    alert('success')
                    drawMarkers(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });

            case 'ZEROWASTE_ETC' :
            $.ajax({
                url : '../zerowaste_data_etc/' ,
                type : 'post' ,
                dataType : 'json' ,
                data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                success : function(zerowaste_list) {
                    $.each(zerowaste_list, function(key, value) {
                        zerowastePlaces.push(value)
                    });
                    console.log(zerowastePlaces)
                    alert('success')
                    drawMarkers(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });
        }
    }) ;
}





function getData() {
     $('.button').click(function() {
          var button_id = $(this).attr('id') ;
          alert(button_id) ;
          switch(button_id) {
              case 'VEGAN_ALL' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_all/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'KOREAN' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_kor/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'WESTERN' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_wes/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'CHINESE' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_chi/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'JAPANESE' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_jap/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'CAFE' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_cafe/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'BAKERY' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_bake/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });

              case 'VEGAN_ETC' :
              clearMarkers() ;
              $.ajax({
                   url : '../vegan_data_etc/' ,
                   type : 'post' ,
                   dataType : 'json' ,
                   data : { 'csrfmiddlewaretoken' : '{{csrf_token}}' } ,
                   success : function(vegan_list) {
                        $.each(vegan_list, function(key, value) {
                             veganPlaces.push(value)
                        });
                        console.log(veganPlaces)
                        alert('success')
                        drawMarkers(veganPlaces) ;
                        veganPlaces = [] ;
                   } ,
                   error : function(request , status , error) {
                        alert('state - '+request.state)
                        alert('msg - '+request.responseText)
                        alert('error - '+error)
                   }
              });
          }
     });
}









/* Marker 생성 */
var markers = [] ;
function clearMarkers() {
     for(var i = 0 ; i < markers.length ; i++) {
          markers[i].setMap(null);
     }
     markers = [] ;
}

function drawMarkers(zerowastePlaces) {
<!--     var myIcon = new google.maps.MarkerImage("../zerowaste.png") ;-->
     for(var i = 0 ; i < zerowastePlaces.length ; i++) {
          var marker = new google.maps.Marker ({
               map : map ,
               position : new google.maps.LatLng(zerowastePlaces[i].lat , zerowastePlaces[i].lng) ,
<!--               icon : myIcon-->
          });
          marker.name = zerowastePlaces[i].name ;
          marker.number = zerowastePlaces[i].number ;
          marker.address = zerowastePlaces[i].address ;
          marker.category = zerowastePlaces[i].category ;
          marker.about = zerowastePlaces[i].about ;

          markers.push(marker) ;
     }

     for(var j = 0 ; j < markers.length ; j++) {
          google.maps.event.addListener(markers[j] , 'click' , function() {
               map.setCenter(this.getPosition()) ;
               map.setZoom(17) ;

               var contentString = "<div><div id='name'>" + marker.name +
                                                  "</div><br>Tel. " + marker.number +
                                                  "<br>Addr. " + marker.address +
                                                  "<br>Cat. " + marker.category +
                                                  "<br>About. " + marker.about + "</div>"

               var infowindow = new google.maps.InfoWindow({
                    content : contentString ,
               });
               infowindow.open(map , this) ;
          });

          closeInfoWindow = function() {
               infowindow.close() ;
          }

//          google.maps.event.addListener(marker[j] , 'click' , closeInfoWindow) ;
//          google.maps.event.addListener(infowindow , 'closeclick' , function() {
//               zoom : 12 ,
//          }) ;
     }

     alert('marker push') ;
}

function createPopupClass() {
    function Popup(position , content) {
        this.position = position ;
    }
}