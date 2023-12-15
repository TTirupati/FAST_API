 
import json
f = open('data.json')

data = json.load(f)
 
print(type(data))

specimen_data=data['specimen']

#print(specimen_data)
specimen_root_lst=['OBR_21_2','OBR_14','OBR_7','OBR_15_1','OBR_15_3']
for key,value in specimen_data.items():
    print("key :",key) #S8-000001;1,S8-000001;2
    # print("value :",value)
    for k,v in value.items():#S8-000001;1;A;S1
        inserted_lst=[]
        print("key2 :",k)
        #print("value :",v['OBR']) #obr and obx
        data_obr=v['OBR']
        print(data_obr.keys())
        obr_keys=list(data_obr.keys())
        for searh_obr in specimen_root_lst:
            if searh_obr in obr_keys:
                inserted_lst.append(data_obr[searh_obr]['value'])
            # else:
            #     child_keys=list(data_obr[searh_obr].keys())
            #     print(child_keys)


        print("**********************************************************************************")


    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



 