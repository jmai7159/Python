#Jonathan Mai
#Project 1

import os
import getpass
import zipfile
import sys
import urllib.request
import shutil





#Change default path to the user's desktop
desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(desktop)





#Start up code
def startup():
    #If Zip file exists, check if the URL file exists
    if (os.path.exists(os.path.join('C:\\Users',getpass.getuser(),'Desktop', 'Project Files.zip'))):
        #If the URL file exists, remove it and unpack the project zip file.
        if (os.path.exists(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs'))):
            shutil.rmtree('URLs')
            unpacker = zipfile.ZipFile('.\\Project Files.zip')
            unpacker.extractall()
            unpacker.close
        #Unpack the zip file if URL file is not found
        else:
            unpacker = zipfile.ZipFile('.\\Project Files.zip')
            unpacker.extractall()
            unpacker.close
    #If the zip file is not found, print message and exit system
    else:
        print('''Please put Project Files.zip on the desktop then restart the script

Press Enter to exit the script''')
        input()
        sys.exit()
              



              
#Process mixed URLs
def option1():
    print("Processing... please be patient\n\n")
    #Go to the directory where the Mixed URLs file can be found
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Mixed URLs'))
    with open('Mixed URLS.txt','r') as task1:
        #Read the text file, split and strip the URL for testing
        for line in task1:
            split1 = line.split('\t')
            split1[3] = split1[3].strip('\n')
            url = split1[3]

            #Test the URL. If the URL is good, add all information to a temporary good data file                                
            try:
                result = urllib.request.urlopen(url,timeout=3).getcode()
                os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Temp'))
                with open('tempgooddata.txt','a') as good_data:
                    good_data.write(split1[0] + '\t' + split1[1] + '\t' + split1[2] + '\t' + split1[3] + '\n')
                    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Mixed URLs'))
            #If the URL is bad, add all information to a new Bad URL file.
            except:
                os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Bad URLs'))
                with open('Bad URLs 2.txt','a') as bad_data:
                    bad_data.write(split1[0] + '\t' + split1[1] + '\t' + split1[2] + '\t' + split1[3] + '\n')
                    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Mixed URLs'))

    #Change directories to the temp file and append the new good data to the master URL file.
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Temp'))   
    with open('tempgooddata.txt', 'r') as task2:
        for line in task2:
            os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs'))
            with open('URL Master File.txt', 'a') as new_good_data:
                new_good_data.write(line)
                os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Temp'))

    #Remove the temp file and move the mixed URLs file to the processed URLs file.
    os.remove('tempgooddata.txt')
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Mixed URLs'))
    shutil.move('Mixed URLS.txt',(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Mixed URLs', 'Processed Mixed URLS')))
    
                
                
                    
                           
#Process Bad URLs
def option2():
    print("Processing... please be patient\n\n")

    #Go to the directory where the bad URLs file can be found
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Bad URLs'))

    #Read the bad URLs file, split and strip the needed information and insert into a list
    with open('Bad URLs.txt','r') as task3:
        bad_list = []
        for line in task3:
            split2 = line.split('\t')
            split2[3] = split2[3].strip('\n')
            bad_list.append(split2)
            
    #Return to the master URL file, split and strip the needed information and insert into a list
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs'))
    with open('URL Master File.txt','r') as task4:
        master_list = []
        next(task4)
        for line in task4:
            split3 = line.split('\t')
            split3[3] = split3[3].strip('\n')
            master_list.append(split3)

    #Compare the lists and remove any matching bad URLs from the master list  
    for i in master_list:
        for j in bad_list:
            if j == i:               
                master_list.remove(i)
                
    #Rewrite the new URLs after they have been processed by the bad URL list to the master URL file             
    with open('URL Master File.txt','w') as task5:
        task5.write('Primary Category\tSecondary Category\tTitle\tURL\n')
        for i in range(0, len(master_list)):
            task5.write(master_list[i][0] + '\t' + master_list[i][1] + '\t' + master_list[i][2] + '\t' + master_list[i][3] + '\n')

    #Move the processed Bad URLs to the processed file folder.
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Bad URLs'))
    shutil.move('Bad URLs.txt', (os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs','Bad URLs','Processed Bad URLs')))
    
            
        
        

def option3():
    #Change the directory to the URL file and make lists for matches and titles
    os.chdir(os.path.join('C:\\Users',getpass.getuser(),'Desktop','URLs')) 
    titles = []
    title_match = []
    #Read the URL master file, split and strip the needed information to the title list
    with open('URL Master File.txt','r') as task6:
        next(task6)
        for line in task6:
            split4 = line.split('\t')
            split4[3] = split4[3].strip('\n')
            titles.append(split4)

    #Ask for user input to search
    title_search = input("Enter all of part of a title: ")
    title_search = title_search.upper()

    #Compare the current title in the list to the user input
    for i in range(0, len(titles)):
        title_check = titles[i][2].upper()

        #If the title matches the user input, assign the information to a combined found variable
        if title_search in title_check:
            found_title = titles[i][2].strip()
            found_URL = titles[i][3].strip()
            combined_found = found_title + '\n' + found_URL + '\n\n'

            #If the title is not already in the list of matching titles, add it to the list
            if combined_found not in title_match:
                title_match.append(combined_found)
          
    #Sort the list of matches and add spacing.      
    title_match.sort()
    print()
    
    #Print the list of title matches
    for i in range(len(title_match)):
        print(title_match[i])
            

                    
startup()

while True:
    #Define the menu
        print(
'''----- MAIN MENU -----

Please select from the following options:

    1. Process Mixed URLs
    2. Process Bad URLs
    3. Look up URLs by Title
    4. Exit
    ''')
        #Get user option
        option_choice = input("Option#: ")

        if str(option_choice) == "1":
            option1()
        elif str(option_choice) == "2":
            option2()
        elif str(option_choice) == "3":
            option3()
        elif str(option_choice) == "4":
            break
        else:
            print("\nThat is not a valid option, please try again.\n")


























