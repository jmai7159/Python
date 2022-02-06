#Jonathan Mai
#Mod 04 Tutorial

import os
import getpass

#Change directory to Desktop
desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(desktop)

#Write Headers
with open('alert_data.csv','w') as headers:
    headers.write('Date,Time,Priority,Classification,Description,Source IP,Destination IP\n')
    
#Read data, split all information and assign to variables
with open('alert.fast.maccdc2012_00000.pcap','r') as data_file:
    for i in data_file:
        split1 = i.split('[**]')
        
        date_time = split1[0] #date/time
        
        attack_date = date_time[:5] #date
        
        attack_time = date_time[6:11] #time
        
        split2 = split1[1].split('] ')
        description = split2[1].strip() #description
        
        split3 = split1[2].split('] [')
        classification = split3[0]
        classification = classification.strip(' [')
        classification = classification[16:] #classification
        
        
        classification_priority_source_destination = split3[1]        
        classification_priority_source_destination = classification_priority_source_destination.split(' ')
        
        priority = classification_priority_source_destination[1] #priority
        priority = priority.strip('] ')
        
        source = classification_priority_source_destination[3].strip() #source

        destination = classification_priority_source_destination[5].strip('\n') #destination

        #Append the information to a CSV file
        with open('alert_data.csv','a') as data:            
            data.write(attack_date + ',' + attack_time + ',' + priority + ',' + classification + ',' + description + ',' + source + ',' + destination + '\n')



print("Operations Complete. Press enter to exit.")
input()
   









