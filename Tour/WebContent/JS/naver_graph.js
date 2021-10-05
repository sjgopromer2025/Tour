
function n_drawBar(word,fre)
{
	var chart = $('#container_graph').highcharts();
	
	
	wordarr = word.split(",");
	frearr = fre.split(',').map(Number);
	
	var text= 'Naver '+ $("select[name=loc]").val() + " 키워드 그래프 ";
	
	wordarr.pop();
	frearr.pop();
	
	if (chart) 
	{
	 // 차트가 있을경우 제거한다.
		chart.destroy();
	}
    // 도넛 그래프
	var chart = { type: 'column'};
	
	var title = { text: text };
	
    var xAxis = {
    		categories: wordarr,
    };
    
    var series= [{
        name: "빈도",
        data: frearr
       }
     ];    
    
    var yAxis = {
	      min: 0,
	      title: {
    	  text: '빈도',
          align: 'high'
	      },
	labels: {
         overflow: 'justify'
	}
    };
    
    
    
    
    var plotOptions = {
        series: {        cursor: 'pointer',
            point: {
                events: {
                    click: function () {
                        //alert('Category: ' + this.category + ', value: ' + this.y);
                    }
                }
            }
        }
    };
    
    
    
    var json = {};   
    
    json.chart = chart; 
    json.title = title;   
    json.xAxis = xAxis;
    json.yAxis = yAxis;  
    json.series = series;
    json.plotOptions = plotOptions;
    $('#container_graph').highcharts(json);
    
    
}