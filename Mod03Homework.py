#Jonathan Mai
#Mod 03 Homework

#List of names
name_list = ['Constance Castillo', 'Kerry Goodwin',
 'Dorothy Carson', 'Craig Williams', 'Daryl Guzman', 'Sherman Stewart',
 'Marvin Collier', 'Javier Wilkerson', 'Lena Olson', 'Claudia George',
 'Erik Elliott', 'Traci Peters', 'Jack Burke', 'Jody Turner',
 'Kristy Jenkins', 'Melissa Griffin', 'Shelia Ballard', 'Armando Weaver',
 'Elsie Fitzgerald', 'Ben Evans', 'Lucy Baker', 'Kerry Anderson',
 'Kendra Tran', 'Arnold Wells', 'Anita Aguilar', 'Earnest Reeves',
 'Irving Stone', 'Alice Moore', 'Leigh Parsons', 'Mandy Perez',
 'Rolando Paul', 'Delores Pierce', 'Zachary Webster', 'Eddie Ward',
 'Alvin Soto', 'Ross Welch', 'Tanya Padilla', 'Rachel Logan',
 'Angelica Richards', 'Shelley Lucas', 'Alison Porter', 'Lionel Buchanan',
 'Luis Norman', 'Milton Robinson', 'Ervin Bryant', 'Tabitha Reid',
 'Randal Graves', 'Calvin Murphy', 'Blanca Bell', 'Dean Walters',
 'Elias Klein', 'Madeline White', 'Marty Lewis', 'Beatrice Santiago',
 'Willis Tucker', 'Diane Lloyd', 'Al Harrison', 'Barbara Lawson',
 'Jamie Page', 'Conrad Reynolds', 'Darnell Goodman', 'Derrick Mckenzie',
 'Erika Miller', 'Tasha Todd', 'Aaron Nunez', 'Julio Gomez',
 'Tommie Hunter', 'Darlene Russell', 'Monica Abbott', 'Cassandra Vargas',
 'Gail Obrien', 'Doug Morales', 'Ian James', 'Jean Moran',
 'Carla Ross', 'Marjorie Hanson', 'Clark Sullivan', 'Rick Torres',
 'Byron Hardy', 'Ken Chandler', 'Brendan Carr', 'Richard Francis',
 'Tyler Mitchell', 'Edwin Stevens', 'Paul Santos', 'Jesus Griffith',
 'Maggie Maldonado', 'Isaac Allen', 'Vanessa Thompson', 'Jeremy Barton',
 'Joey Butler', 'Randy Holmes', 'Loretta Pittman', 'Essie Johnston',
 'Felix Weber', 'Gary Hawkins', 'Vivian Bowers', 'Dennis Jefferson',
 'Dale Arnold', 'Joseph Christensen', 'Billie Norton', 'Darla Pope',
 'Tommie Dixon', 'Toby Beck', 'Jodi Payne', 'Marjorie Lowe',
 'Fernando Ballard', 'Jesse Maldonado', 'Elsa Burke', 'Jeanne Vargas',
 'Alton Francis', 'Donald Mitchell', 'Dianna Perry', 'Kristi Stephens',
 'Virgil Goodwin', 'Edmund Newton', 'Luther Huff', 'Hannah Anderson',
 'Emmett Gill', 'Clayton Wallace', 'Tracy Mendez', 'Connie Reeves',
 'Jeanette Hansen', 'Carole Fox', 'Carmen Fowler', 'Alex Diaz',
 'Rick Waters', 'Willis Warren', 'Krista Ferguson', 'Debra Russell',
 'Ellis Christensen', 'Freda Johnston', 'Janis Carpenter', 'Rosemary Sherman',
 'Earnest Peters', 'Kelly West', 'Jorge Caldwell', 'Moses Norris',
 'Erica Riley', 'Ray Gordon', 'Abel Poole', 'Cary Boone',
 'Grant Gomez', 'Denise Chapman', 'Vernon Moran', 'Ben Walker',
 'Francis Benson', 'Andrea Sullivan', 'Wayne Rice', 'Jamie Mason',
 'Jane Figueroa', 'Pat Wade', 'Rudy Bates', 'Clyde Harris',
 'Andre Mathis', 'Carlton Oliver', 'Merle Lee', 'Amber Wright',
 'Russell Becker', 'Natalie Wheeler', 'Maryann Miller', 'Lucia Byrd',
 'Jenny Zimmerman', 'Kari Mccarthy', 'Jeannette Cain', 'Ian Walsh',
 'Herman Martin', 'Ginger Farmer', 'Catherine Williamson', 'Lorena Henderson',
 'Molly Watkins', 'Sherman Ford', 'Adam Gross', 'Alfred Padilla',
 'Dwayne Gibson', 'Shawn Hall', 'Anthony Rios', 'Kelly Thomas',
 'Allan Owens', 'Duane Malone', 'Chris George', 'Dana Holt',
 'Muriel Santiago', 'Shelley Osborne', 'Clinton Ross', 'Kelley Parsons',
 'Sophia Lewis', 'Sylvia Cooper', 'Regina Aguilar', 'Sheila Castillo',
 'Sheri Mcdonald', 'Lynn Hodges', 'Patrick Medina', 'Arlene Tate',
 'Minnie Weber', 'Geneva Pena', 'Byron Collier', 'Veronica Higgins',
 'Leo Roy', 'Nelson Lopez']


#Find first name by letter.
def allfirst():
    matches = 0
    search_name = input("\nWhat letter does the first name begin with? ")
    search_name = search_name.upper()
    print("")
    
    #Step through the list and match the letter to the name.
    for i in range(len(name_list)):
        
        #If a match is found, print the name and increment the counter.
        if name_list[i].startswith(search_name) == True:
            print(name_list[i])
            matches = matches + 1
            
    #If no matches are found, print message.
    if matches == 0:
        print("No first names were found starting with the letter " + search_name + ".")
    print("")


#Find last name by letter.
def alllast():
    matches = 0
    search_name = input("\nWhat letter does the last name begin with? ")
    search_name = search_name.upper()
    print("")
    
    #Step through the list and match the letter to the name.
    for i in range(len(name_list)):

        #Create separate list to split and check last names.
        lastname_check = name_list[i].split()

        #If a match is found, print the name and increment the counter.
        if lastname_check[1].startswith(search_name) == True:
            print(lastname_check[1] + ", " + lastname_check[0])
            matches = matches + 1

    #If no matches are found, print message.
    if matches == 0:
        print("No last names were found starting with the letter " + search_name + ".")
    print("")


#Add a name
def addname():
    #Request input of first name and last name.
    add_firstname = input("\nEnter the new first name: ")
    add_lastname = input("Enter the new last name: ")

    #Add the name to the list.
    name_list.append(add_firstname.title() + ' ' + add_lastname.title())

    #Get the name from the index of where the name was added.
    print("\n" + name_list[-1] + " has been added.\n")
        

#Delete a name
def deletename():
    #Request input of the name to delete.
    delete_name = input("\nEnter the full name to delete: ")

    #Try to delete the name.
    try:
        name_list.remove(delete_name.title())

        #Check if the name was deleted.
        if delete_name not in name_list:
            print("\n" + delete_name + " has been removed.\n")
       
    #If the name could not be found, print message
    except:
        print("\nThat name was not found.\n")
        
  
#Body
while True:
    #Define the menu
        print(
'''Please select from the following options:
    1. List all first names beginning with a chosen letter
    2. List all last names beginning with a chosen letter
    3. Add a name
    4. Delete a name
    5. Exit
    ''')
        #Get user option
        option_choice = input("Option#: ")

        #Menu navigation
        if str(option_choice) == "1":
            allfirst()
        elif str(option_choice) == "2":
            alllast()
        elif str(option_choice) == "3":
            addname()
        elif str(option_choice) == "4":
            deletename()
        elif str(option_choice) == "5":
            break
        else:
            continue
    
        
































