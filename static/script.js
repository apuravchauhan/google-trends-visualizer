var pallete =[
['#dff0ea', '#3792d5', '#574f7d','#dedede','#4f3a65'],
['#D0EFB1','#88f444','#9DC3C2','#77A6B6','#4D7298'],
['#E3E4DB','#8F6593','#9DC3C2','#3B252C','#DECCCC'],
['#FF5487','#F4BCCD','#A03E5C','#7A5560','#C1ACB2'],
['#ca5fa6','#f36886','#ffaf65','#fdef96','#fa8282']
];
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}
var chart = Highcharts.chart('container', {
  colors:pallete[getRandomInt(pallete.length)],


  chart: {
    type: 'column',
    plotBorderColor: '#000000',
    backgroundColor: '#323233',
    options3d: {
      enabled: true,
      alpha: 20,
      beta: 15,
      viewDistance: 25,
      depth: 20
    }
  },
  credits: {
    text: 'apuravchauhan.com',
    href: 'http://apuravchauhan.com'
},
  title: {
    text: 'Year',
    style: {
      fontSize: '26px',
      color: '#E0E0E3'
    }
},
subtitle: {
    text: 'Search Trends',
    style: {
      color: '#E0E0E3'
      }
},
  xAxis: {
    gridLineColor: '#4f4f52',
    categories: columns,
    labels: {
      skew3d: true,
      style: {
        fontSize: '26px',
        color: '#E0E0E3'

      }
    }
  },
  yAxis: {
    gridLineColor: '#4f4f52',
    allowDecimals: false,
    min: 0,
    labels: {
      style: {
        color: '#E0E0E3'

      }
    },
    title: {
      text: 'Community Interest',
      skew3d: true,
      style: {
        fontSize: '20px',
        color: '#E0E0E3'
      }
    }
  },

  tooltip: {
    headerFormat: '<b>{point.key}</b><br>',
    pointFormat: '<span style="color:{series.color}">\u25CF</span> {series.name}: {point.y} / {point.stackTotal}'
  },

  plotOptions: {
    column: {
      depth: 20
    }
  },
  legend: {
    itemStyle: {
        color: '#E0E0E3'
    },
    itemHoverStyle: {
        color: '#FFF'
    },
    itemHiddenStyle: {
        color: '#606063'
    }
}

});
var index=0;
var interval = setInterval(function () {
  //Highcharts.charts[0].series[0].setCategories([3, 3, 3, 3, 3])
  chart.setTitle({text:gData[index]['Month']});
  chart.update({
   series: gData[index++]['gseries']
},true,true);
if(index>=gData.length){
  clearInterval(interval);
}
}, 100);