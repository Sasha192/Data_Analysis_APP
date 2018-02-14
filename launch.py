import numpy as np
import pandas as pd
from spyre import server
import my_script


class App(server.App):
    title = "Simple App"

    inputs = [
    		{
    			"type" : "dropdown",
	    		"label" : "Province",
	    		"options" : [{"label": i,"value": i} for i in my_script.city_list()],
	    		"key" : "province"},
    		{
	    		"type" : "dropdown",
	    		"label" : "Indexes",
	    		"options" : [
	   				{"label" : "VHI", "value" : "VHI"},
	    			{"label" : "TCI", "value" : "TCI"},
	    			{"label":"VCI","value" : "VCI"}],
    			"key" : "index"},
    		{
				"type":'slider',
				"label": 'Min',
				"key": 'freq1',
				"value" : 0,
				"min" : 0,
				"max" : 53
			},
			{
				"type":'slider',
				"label": 'Max',
				"key": 'freq2',
				"value" : 53,
				"min" : 0,
				"max" : 53
			}]
    controls = [
   			{
				"type" : "button",
				"label" : "Update",
				"id" : "update_data"}]
    outputs = [
    		{
    			"type" : "table",
    			"id" : "table_id",
    			"control_id" : "update_data"},
    		{
    			"type" : "html",
    			"id" : "some_html",
    			"control_id" : "update_data"
    		}]


    def getHTML(self,params):
    	min = params['freq1']
    	max = params['freq2']
    	if min > max: 
    		return "Incorrect condition"
    	return None

    def getData(self, params):
    	prov = params['province']
    	ind = params['index']
    	min = params['freq1']
    	max = params['freq2']
    	if min > max:
    		return None
    	df = my_script.data_frame_filter(province = prov, index = ind, min = min, max= max)
    	return df


app = App()
app.launch()  