function loadMap(place,data){
	$.ajax({
		url: "../ajax/loadmap.jsp",
		type: "post",
		dataType: "html",
		data: "place="+place+"&data="+data,
		success : function(data) 
		{
			data = data.trim();
			//alert(data);
			drawMarker(data)
		},
		error: function(request, status, error) 
		{
			alert("error!!!");
		}
	});	
	
}



function drawMarker(data) {
	data_arr = data.split("<<SEP>>");
	var place = data_arr[0].split(",");
	var x = data_arr[1].split(",").map(Number);
	var y = data_arr[2].split(",").map(Number);
	
	//alert(place);
	//alert(x);
	//alert(y);
	var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
    mapOption = 
    { 
        center: new kakao.maps.LatLng(x[2],y[2]), // 지도의 중심좌표
        level: 8 // 지도의 확대 레벨
    };

	var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
	
	// 마커를 표시할 위치와 title 객체 배열입니다 
	var positions = [];
	
	for (i = 0; i < place.length;i++)
	{
		var t =  {
		        title : place[i], 
		        latlng: new kakao.maps.LatLng(x[i],y[i])
		    };
		//alert(t['title']);
		positions.push(t);
	}	
	
	//alert(positions.length);
	
	// 마커 이미지의 이미지 주소입니다
	var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
	// 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35); 
    // 마커 이미지를 생성합니다    
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    
	for (var i = 0; i < positions.length; i ++) {
	    
	    
	    
	    // 마커를 생성합니다
	    var marker = new kakao.maps.Marker({
	        map: map, // 마커를 표시할 지도
	        position: positions[i].latlng, // 마커를 표시할 위치
	        title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
	        image : markerImage // 마커 이미지 
	    });
	    var infowindow = new kakao.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:6px 0;">'+positions[i].title+'</div>'
        });
        infowindow.open(map, marker);
	}
	
	var linePath = [];
	/*
	for (i = 0; i < place.length;i++)
	{
		linePath.push(  new daum.maps.LatLng(x[i], y[i]));
	}

	
	// 지도에 표시할 선을 생성합니다
	var polyline = new daum.maps.Polyline({
	    path: linePath, // 선을 구성하는 좌표배열 입니다
	    strokeWeight: 5, // 선의 두께 입니다
	    strokeColor: '#FFAE00', // 선의 색깔입니다
	    strokeOpacity: 0.7, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
	    strokeStyle: 'solid' // 선의 스타일입니다
	});
	*/
	
	polyline.setMap(map);

}
