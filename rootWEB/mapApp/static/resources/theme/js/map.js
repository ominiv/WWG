var map ;
var searchMarker ;
var veganPlaces = [] ;
var zerowastePlaces = [] ;

/*--------------------
         Map 생성
 --------------------- */
//function initMap() {
//     var defaultOptions = {
//          zoom : 12 ,
//          center : new google.maps.LatLng(37.5643135 , 127.0016985),
//          disableDefaultUI : true ,
//          zoomControl : false ,
//          gestureHandling : 'greedy' ,
//     }
//     map = new google.maps.Map(document.getElementById("map"), defaultOptions);
//     getData() ;
//}

window.initAutocomplete = function() {
    map = new google.maps.Map(document.getElementById("map") , {
         zoom : 12 ,
         center : new google.maps.LatLng(37.5643135 , 127.0016985),
         disableDefaultUI : true ,
         zoomControl : false ,
         gestureHandling : 'greedy' ,
    }) ;
    getData() ;
    initPopup() ;
}

/* ------------------------------------------
        AJAX 통신으로 데이터 수신
------------------------------------------- */
/* Zerowate */
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
                    console.log(zerowastePlaces) ;
                    drawMarkers(zerowastePlaces) ;
                    makeInfowindow(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });
            break ;

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
                    console.log(zerowastePlaces) ;
                    drawMarkers(zerowastePlaces) ;
                    makeInfowindow(zerowastePlaces) ;
                    zerowastePlaces = [] ;
                } ,
                error : function(request , status , error) {
                alert('state - '+request.state)
                alert('msg - '+request.responseText)
                alert('error - '+error)
                }
            });
            break ;

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
                    console.log(zerowastePlaces) ;
                    drawMarkers(zerowastePlaces) ;
                    makeInfowindow(zerowastePlaces) ;
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
                    console.log(zerowastePlaces) ;
                    drawMarkers(zerowastePlaces) ;
                    makeInfowindow(zerowastePlaces) ;
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
                    console.log(zerowastePlaces) ;
                    drawMarkers(zerowastePlaces) ;
                    makeInfowindow(zerowastePlaces) ;
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

/* Vegan */
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

/* -------------------------------
                Marker 생성
--------------------------------- */
var markers = [] ;
/* list 초기화 */
function clearMarkers() {
     for(var i = 0 ; i < markers.length ; i++) {
          markers[i].setMap(null);
     }
     markers = [] ;
}

let infowindow_contents = [] ;
/* 마커 뿌리기 */
function drawMarkers(zerowastePlaces) {
    infowindow_contents = [] ;

    console.log("makePlaceMarker : " + zerowastePlaces.length) ;
    var myIcon = {
        url : "{% static '/resources/theme/images/zerowaste.png' %}" ,
        size : new google.maps.Size(40 , 40) ,
        origin : new google.maps.Point(0 , 0) ,
        anchor : new google.maps.Point(20 , 40) ,
        scaledSize : new google.maps.Size(40 , 40) ,
    } ;

    for(var i = 0 ; i < zerowastePlaces.length ; i++) {
//        geocoder.geocode({'address' : zerowastePlaces[i].address} ,function(results , status) {
//            if(status == google.maps.GeocoderStatus.OK) {
//                var lat = results[i].geometry.location.lat() ;
//                var lng = results[i].geometry.location.lng() ;
//                map.setCenter(results[i].geometry.location) ;
//
//                var marker = new google.maps.Marker({
//                    map : map ,
//                    icon : myIcon ,
//                    title : zerowastePlaces[i].name ,
//                    position : results[i].geometry.location ,
//                }) ;
//            } else {
//                alert("error : " + status) ;
//            }
//        }) ;
       /* marker 생성 */
        var marker = new google.maps.Marker({
            map : map ,
            icon : myIcon ,
            title : zerowastePlaces[i].name ,
            position : new google.maps.LatLng(zerowastePlaces[i].lat , zerowastePlaces[i].lng) ,
        }) ;

        marker.name = zerowastePlaces[i].name ;
        marker.number = zerowastePlaces[i].number ;
        marker.address = zerowastePlaces[i].address ;
        marker.category = zerowastePlaces[i].category ;
        marker.about = zerowastePlaces[i].about ;

        markers.push(marker) ;
        makeInfowindow(marker) ;
        console.log('markers : ' + marker) ;
    }

    showInfowindow(markers) ;
    alert('showinfowindow marker complete') ;
}

/* info창 */
function makeInfowindow(zerowastePlaces) {
    const temp_content =
    "<div id = 'infoTitle' class = 'info_title'><div class='place_name'>" +
    zerowastePlaces.name +
   "</div><div class='more_detail' onclick='showPlaceDetail(\"" +
    zerowastePlaces.name + "\");'>&#62;</div></div><div class='info_rest'>" +
    zerowastePlaces.address +
    "</div>";

    console.log(temp_content) ;
    infowindow_contents.push(temp_content) ;
}

/* marker 클릭 시 popup */
function showInfowindow(markers) {
    for(let i = 0 ; i < markers.length ; i++ ) {
        google.maps.event.addListener(markers[i] , "click" , async function() {
            alert('marker click') ;
            if(infowindow_contents[i]) {
                await removePopup() ;
                await createPopup(markers[i].position , infowindow_contents[i]) ;

                /* 상세보기 */
                const moreDetail = document.getElementById("moreDetail") ;
                if( moreDetail ) {
                    moreDetail.addEventListener("click" , function() {
                        console.log("click") ;
                        showPlaceDetail(markers[i].title) ;
                    }) ;
                }
                console.log("marker : " + markers[i].title) ;
            }
        }) ;
    }
}

let Popup , popup ;
/* google 지도 로드될 때 실행되는 initAutocomplete() 에서 호출 */
export function initPopup() {
    Popup = createPopupClass() ;
}

/* 마커 클릭시 호출 */
export function createPopup(position , content) {
    popup = new Popup(position , content) ;
    alert("click") ;
    popup.setMap(map) ;

    map.addListener("click" , function() {
        removePopup() ;
        initMarker() ;
    }) ;
}

/* 마커 클릭시 이전 팝업창 삭제 */
export function removePopup() {
    if (popup != undefined) {
        popup.setMap(null) ;
    }
}

/* ----------------------------------
            Customized Popup
------------------------------------ */
/* custom popup 생성을 위한 클래스 */
/* https://after-newmoon.tistory.com/52?category=864821 */
function createPopupClass() {
    function Popup(position , content) {
        this.position = position ;

        this.contentNode = document.createElement("div") ;
        this.contentNode.className = "popup_wrap" ;

        var popupInfo = document.createElement("div") ;
        popupInfo.className = "popup" ;
        this.contentNode.appendChild(popupInfo) ;
        popupInfo.innerHTML = content ;

        var popupAnchor = document.createElement("div") ;
        popupAnchor.className = "popup-anchor" ;
        this.contentNode.appendChild(popupAnchor) ;

        google.maps.OverlayView.preventMapHitsAndGesturesFrom(this.contentNode) ;
    }

    Popup.prototype = Object.create(google.maps.OverlayView.prototype) ;

    /* popup이 지도에 추가될 때 호출 */
    Popup.prototype.onAdd = function() {
        this.getPanes().floatPane.appendChild(this.contentNode) ;
    } ;

    /* popup이 지도에 삭제될 때 호출 */
    Popup.prototype.onRemove = function() {
        if (this.contentNode.parentElement) {
            this.contentNode.parentElement.removeChild(this.contentNode) ;
        }
    } ;

    /* popup을 그릴 때 호출 */
    Popup.prototype.draw = function() {
        var divPosition = this.getProjection().fromLatLngToDivPixel(this.position) ;
        /* 시야에서 멀어질 경우 popup hide */
        var display = Math.abs(divPosition.x) < 4000 && Math.abs(divPosition.y) < 4000 ?
        " block" :
        "none" ;

        if (display === "block") {
            this.contentNode.style.left = divPosition.x + "px" ;
            this.contentNode.style.top = divPosition.y - 20 + "px" ;
        }

        if(this.contentNode.style.display !== display) {
            this.contentNode.style.display = display ;
        }
    } ;

    return Popup ;
}

let placeInfo = [] ;
/* place detail */
async function getPlaceDetail(temp_places) {
    let temp_placeInfo = [] ;

    await temp_places.forEach(function (temp_place) {
        const request = {
            placeId : temp_place.place_id ,
            fields : [
            "name" ,
            "formatted_address" ,
            "formatted_phone_number" ,
            "formatted_category" ,
            "formatted_about" ,
            ] ,
        } ;

        service.getDetails(request , function(place , status) {
            if(status === google.maps.places.PlacesServiceStatus.OK) {
                placeInfo.push(place) ;
            } else {
                console.log(status) ;
                temp_placeInfo.push(temp_place) ;
            }
        }) ;
    }) ;

    if(temp_placeInfo.length != 0) {
        console.log("try again") ;
        setTimeout(getPlaceDetail , 2000 , temp_placeInfo) ;
        temp_placeInfo = [] ;
    }
}

function hidePlaceDetail() {
    detailBlock.classList.add("blind") ;
}

window.showPlaceDetail = function(clicked_place_name) {
    removePopup() ;

    placeInfo.forEach(async function(place) {
        if(clicked_place_name == place.name) {
            if(detailBlock.classList.contains("blind")) {
                detailBlock.classList.remove("blind") ;
            }

            document.getElementById("name").innerHTML =
            "<h1>" + place.name + "</h1>" ;

            document.getElementById("address").innerHTML = place.formatted_address ;
            document.getElementById("number").innerHTML = place.formatted_phone_number ;
            document.getElementById('category').innerHTML = place.formatted_category ;
            document.getElementById('about').innerHTML = place.formatted_about ;
        }
    }) ;

    if (closeBtn) {
        closeBtn.addEventListener("click" , function() {
            detailBlock.classList.add("blind") ;
            initMarker() ;
        }) ;
    }
} ;