import csv
import json
import os
import glob


class TrendProcessor:
    def __init__(self, folder, dateHeader):
        self.data = []
        self.folder = folder
        self.seriesOrder = {}
        self.columns=[]
        self.dateHeader = dateHeader
        for idx, file in enumerate(glob.glob(folder+'/*.csv')):
            head,tail = os.path.split(file)
            self.columns.append(tail.split('.csv')[0])
            if(idx == 0):
                self.processBase(file)
            else:
                self.processMore(file)

    def processBase(self, file):
        reader = csv.DictReader(open(file))
        headerProcessed = False
        for row in reader:
            obj = {self.dateHeader: '', 'gseries': []}
            idx = 0
            for k, v in row.items():
                if(k == self.dateHeader):
                    obj[self.dateHeader] = v
                else:
                    clearName = k.split(':')[0]
                    if(headerProcessed == False):
                        self.seriesOrder[clearName] = idx
                        idx += 1
                    val = float(v) if v!='<1' else 0    
                    subseries = {'name': clearName, 'data': [val]}
                    obj['gseries'].append(subseries)
            headerProcessed = True
            self.data.append(obj)

    def processMore(self, file):
        reader = csv.DictReader(open(file))
        idx = 0
        for row in reader:
            for k, v in row.items():
                if(k != self.dateHeader):
                    clearName = k.split(':')[0]
                    existingObj = self.data[idx]['gseries'][self.seriesOrder[clearName]]
                    val = float(v) if v!='<1' else 0    
                    existingObj['data'].append(val)
            idx += 1



