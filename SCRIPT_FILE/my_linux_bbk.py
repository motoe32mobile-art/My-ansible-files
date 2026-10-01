import os 
import csv 
import json
from datetime import * 

date=date.today()
time1=datetime.now()
filepath=time1.strftime("DAILY_REPORTS_%Y-%m-%d%H%M.csv")
jsonfile="my_linux.json"
with open(jsonfile) as jf:
    my_dict=json.load(jf)
os_name=os.popen(my_dict['os_flavour']).read().strip().replace('"','')
print(os_name)

if os_name == 'amzn' or os_name == 'amazon':
    print("amzn/amazon os found we are collecting information, please wait!!!")
    
    #hostname details 
    hostname=os.popen(my_dict["hostname"]).read()
    print(hostname)
    
    #IP address
    ip=os.popen(my_dict["ip_address"]).read()
    print(ip)
    
    #file storage details
    df_details=os.popen(my_dict["df_details"]).read()
    print(df_details)
    
    #Store in varaible into list for interesting CSV data
    header_csv=(my_dict['header_para'])
    header_csv=[str(x) for x in header_csv]
    print(header_csv)

    #Data csv 
    data_csv = [hostname,ip,df_details]
    file1=open(filepath,'a+')
    writer=csv.writer(file1)
    writer.writerow(header_csv)
    writer.writerow(data_csv)
    file1.close()

    print("File import successfully from your current directory"+filepath)
else: 
    print("other os found")

