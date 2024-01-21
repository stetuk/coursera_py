import json  
# python objects can store in json format  
value ={    
        "a": "1",  
        "b": "2",  
        "c": "4",  
        "d": "8"  
}  
# the json file to save the output data   
save_file = open("savedata.json", "w")  
json.dump(value, save_file, indent = 6)  
save_file.close()  