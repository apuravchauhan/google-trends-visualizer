import trendProcessor as tp
import json

folder = input("Enter folder location (default: data) : ")
folder = 'data' if folder=='' else folder
dateHeader = input("Enter colum containing date (default: Month) : ")
dateHeader = 'Month' if dateHeader=='' else dateHeader
output = input("Enter output file name (default: index.html)")
output = 'index.html' if output=='' else output
viz = tp.TrendProcessor(folder,dateHeader)

template = '<!DOCTYPE html>\
<html lang="en">\
<head>\
  <meta charset="UTF-8">\
  <meta name="author" content="Apurav Chauhan">\
  <title>Trends Visualization | Apurav Chauhan</title>\
  <link rel="stylesheet" href="static/style.css">\
  <script>\
      var columns = XcolsX;var gData = XdataX;\
  </script>\
</head>\
<body>\
  <script src="static/highcharts.js"></script>\
  <script src="static/highcharts-3d.js"></script>\
  <div id="container"></div>\
  <script src="static/script.js"></script>\
</body>\
</html>'
template = template.replace('XcolsX',json.dumps(viz.columns)).replace('XdataX',json.dumps(viz.data))

with open(output,'w') as f:
  f.write(template)

print('Visualization successfully generated to index.html.')
print('Feedback tweets welcome @apuravchauhan')
