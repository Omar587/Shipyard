"""
Author Omar Mohamed
"""

class Shipyard:
    class Container:
        class Package:
            """ Each package object will  have a destination weight owner and id 
            and a next field which will point the other package obejcts in the 
            container"""
            def __init__(self, owner, dest, weight, n_next, ID):
                self._weight = weight
                self._next = n_next                      
                self._elem = None
                self._size = 0
                self._owner = owner
                self._dest = dest
                self.ID = ID
               
               
        def __init__(self, owner, dest, weight, n_next,ID):
            """The purpose of this class is to store the Package made from our package
            class into the container.
            Paramaters: owner, dest are strings weight is an integer
            Returns: None
            """
            self._weight = 0
            self._next = n_next
            #initializes the package object in the container class
            self.pac = self.Package(None, None, None, None,None)            
            self._owner = owner
            self._dest = dest
            self._first = None
            self._size = 0
            self.ID = ID
            self.pac_num = 0
           
        
        def __len__(self):
            return self._size
        
        def isEmpty(self):
            return self._size == 0
    
   
        def add_pack(self, owner, dest, weight,ID):
            """"The purpose of this method is to add a package to a container when 
            the method is called from the shiyard class.  
            Paramater: owner and dest are strings. weight and ID are integers
            Returns: None
            
            """
            #if it is true that the container is empty create a package 
            #everytime a package is added the size of Package is incremented by 1
            #weight is totaled everytime a package is added
            #orders the weight from lightest to largest.
              
            if self.isEmpty() or weight < self.pac._elem._weight:
                self._size += 1
               
                self.pac._elem = self.Package(owner, dest, weight, self.pac._elem,ID)
                                                 
                self._weight += weight
                return
             
            #reference for the Package 
            temp = self.pac._elem
            
            #while the reference points to the next package and the 
            #the weight is greater than the currect package weight. 
            #the current next pointer will point the one we want to add.
            while(temp._next != None and weight >= temp._next._weight):
                temp = temp._next
        
   
            self._size += 1
            temp._next = self.Package(owner, dest, weight, temp._next,ID)
                                           
            self._weight += weight
   
            return
       
     
       
        def remove(self,owner,dest,weight):
            """The purpose of this method is to remove a package  by the owner
            destination and weight. This will be a method used in the shipyard class.
            to access the  packages in the container.
            
            paramater: owner dest are strings. Weight is an integer 
            Returns: None"""
            
            #if the container only has one package then set the package contents 
            #to none 
            temp = self.pac._elem
            if temp._owner == owner and temp._weight == weight and self._size == 1:
                self._weight = self._weight - temp._weight
                temp._owner = None
                temp._weight = None
                temp._dest = None
                temp.ID = None
                return

            
            #if the Packages first item is the one we want to remove then replace
            #the first package with the second package next to the first. 

            if temp._owner == owner and temp._weight == weight:
                self._weight = self._weight - temp._weight
                temp._owner = temp._next._owner
                temp._weight = temp._next._weight
                temp.ID = temp._next.ID
                temp._next = temp._next._next
                self._size -= 1
                return
        
           
            if self.isEmpty():
                raise Empty("Can not remove from an empty container")
           
           
            if self.pac._elem == weight:
                
                self._size -= 1
                
                self.pac._elem = self.pac._elem._next        
            
            #if the package pointer matches to the target then make the pointer 
            #point past the target.
    
            while temp._next != None and owner == temp._next._owner and weight > temp._next._weight:
                temp = temp._next
               
            if temp._next == None:
                return    
            if temp._next._weight!= weight:
                return
           
            temp._next = temp._next._next  
            
            #once again after every time a package is added or removed the size and 
            #weight is incremented accordingly
            self._size = self._size - 1
            self._weight -= weight
            
            
    
           
        def search_by_id(self, package_id):
            """The purpose of this method is to search for a package with an id.
            This will be a method used in the shipyard class.
            to access the  packages in the container
            paramater: package_id INTEGER 
            Returns True or False """
            
            #loops through the list of Packages if the id matches return True
            #else return False
            temp=  self.pac._elem
            while (temp != None) :
                if temp.ID == package_id: 
                    print(f"Package id #{temp.ID} has been found  \nOwner {temp._owner} \nDestination {temp._dest}\nWeight {temp._weight}" )
                    return True
                temp = temp._next
                
               
            return False   
        
        
        def search(self,owner, dest, weight):
            """The purpose of this method is to search for a package with an owner 
            destination and weight. This will be a method used in the shipyard class.
            to access the the packages in the container. 
     
            paramater: owner, dest, string. weight INTEGER 
            Returns True or False """
            
            #loops through the list of Package if the target matches return True
            #else return False            
            temp=  self.pac._elem
            while (temp != None) :
                if temp._dest ==dest and temp._weight == weight and owner == temp._owner: 
                    print(f"Package id #{temp.ID} has been found  \nOwner {temp._owner} \nDestination {temp._dest}\nWeight {temp._weight}" )
                    return True
                temp = temp._next
                
            return False               
            
           
    
        def remove_by_id(self,package_id):
            
            """The purpose of this method is to remove a package  by ID.
            This will be a method used in the shipyard class
            to access the the packages in the container. 
            paramater: package_ID integer 
            Returns: None"""            
            #if the container only has one package then set the package contents 
            #to none 
            
            temp = self.pac._elem
            if temp.ID == package_id and self._size == 1:
                self._weight = self._weight - temp._weight
                temp._owner = None
                temp._weight = None
                temp._dest = None
                temp.ID = None
                return            
  
            #if the Packages first item is the one we want to remove then replace
            #the first package with the second package next to the first. 
            
            if temp.ID == package_id:
                self._weight = self._weight - temp._weight
                temp._owner = temp._next._owner
                temp._weight = temp._next._weight
                temp.ID = temp._next.ID

                temp._next = temp._next._next      
                return
                

       
            if self.isEmpty():
                raise Empty("Can not remove from an empty container")
        
           
            if self.pac._elem == package_id:
                self._size -= 1
                self.pac._elem = self.pac._elem._next  
                
            #loops throught the package list if the id matches stop
            #at the location of that package
            while temp is not None:
                if package_id == temp.ID:
                    break
            #prev is a reference to the current position
                prev = temp
                temp = temp._next
            
            #if the reference is none after the loop that means we found nothing 
            if temp == None:
                return    
            #previous node will point to the references next node 
            prev._next = temp._next
            self._weight = self._weight - temp._weight   
            temp = None
                   
            self._size = self._size - 1
                 
       



        def printAll(self):
            """The purpose of this method is to print all the Package for every 
            container. This will be a method used in the shipyard class
            to access the the packages in the container. 
            Paramater: None  Return: None"""
            
            temp = self.pac._elem
              
            
            while temp != None:
             
                print( f"Package ID #{temp.ID}\nOwner {temp._owner}\nDestination {temp._dest}\nWeight {temp._weight} ")
                print()
                #print(temp._owner, temp._dest, temp._weight, temp.ID )

                temp = temp._next    
            print("----------------------------------------------------")   
            
    def __init__(self):
        """Initilizer for the shipyard class it has a container object stored in the 
        self._cont variable
        Paramater: None returns: None"""
        self._cont = self.Container(None, None, None, None, None)
        self._size = 0
         
    
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
   



    def add(self, owner, dest, weight, ID = 0):
        """The purpose of this method is to  create a container depending on 
        the weight of Package that are passed through. New containers will be made
        if the weight is above 2000 pounds and placed in the shipyard. 
        
        Paramater: owner, dest stirngs. Weight and ID is an integer.
        """
        
        #self._cont.pac_num will be used as and ID generator everytime 
        #a package is made an id is attached to it. The ID is intialized as 0
        self._cont.pac_num = self._cont.pac_num + 3213
       
        #creates a container if there are none in the shipyard
        if self.isEmpty() or dest < self._cont._first._dest:
            self._size += 1
            self._cont._first = self.Container(owner, dest,  weight, self._cont._first, self._cont.pac_num )
            #adds package to first container                                 
            self._cont._first.add_pack(owner, dest, weight, self._cont.pac_num + 322)

            return  

     
        temp = self._cont._first

        #compares destinations and sorts them in alphabetical order.
        while(temp._next != None and  dest > temp._next._dest):
            temp = temp._next
         
                 
         
        if dest == temp._dest:
           #if weight is above 2000 pounds then dont add package to the container
           #make the current container point to the newly created container
           #a package is added to the new container. 
            
            if (temp._weight + weight) > 2000:
                self._size += 1
                temp._next = self.Container(owner, dest,weight, temp._next, self._cont.pac_num + 311)
                                               
                temp._next.add_pack(owner, dest, weight, self._cont.pac_num + 311)
                return                    
            
            #if there container weight is less or equal to 2000 add the package to
            #the container
            if (temp._weight + weight) <= 2000:
                temp.add_pack(owner, dest, weight, self._cont.pac_num + 311)
                return            
        
     
        self._size += 1

        temp._next = self.Container(owner, dest, weight, temp._next,  self._cont.pac_num + 322 )
        temp._next.add_pack(owner, dest, weight, self._cont.pac_num + 311 )

        return
    
 
   
    def remove(self,owner,dest,weight):
        """The purpose of this function is call the remove method from the container class
        this method will identify Package to be removed for from user specified inputs.
        paramamater: owner, dest string   weight: integer
        returns None
        
        """
       
        #reference to the container
        temp = self._cont._first
        
        while temp != None:
            # dot remove(owner,dest,weight) is a method that locates the package in the container
            #if the containers destination matches. Then it will search the container
            #for a package that has the owner destination and weight and remove it
            temp.remove(owner,dest,weight)
            temp = temp._next
            
            
            
            
    def search_by_id(self, package_id):
        """ the purpose of this function is call the search_by_id method from the container class
        this method will identify Packages to be search for from user specified inputs. and will
        display the information about the package. 
        
        paramater: package_id: integer
        returns none""" 
        #reference to the container 
        temp = self._cont._first
        
        #searches each container and searches each package for the ID 
        while temp != None:
            temp.search_by_id(package_id)
            temp = temp._next            
        
   
    def remove_by_id(self, package_id):
        """ the purpose of this function is call the remove_by_id method from the container class
        this method will identify Package to be search for from user specified inputs. and delete 
        the package from the container. 
        paramamater: package_id: integer
        returns none"""         
        #searches each container and searches each package for the ID then removes
        #the package if found
        temp = self._cont._first
       
        while temp != None:
            temp.remove_by_id(package_id)
            temp = temp._next    

    def printContainers(self):
        """The purpose of this method is to display the containers weight
        and destination. Returns None:  Paramater: None
        """
        if self.isEmpty():
            return                
        temp = self._cont._first
        while temp != None:
            print(f"Container id #{temp.ID} destination {temp._dest} weight {temp._weight}")
            temp = temp._next
                 
    def printAll(self) :
        """The purpose of this method is to print out the shipyard manifest 
        so all information about the shipyard will be printed. Such as containers,
        container weight, package ID, weight, owner, destination.  
        Paramater: None   Returns None
        """
        #if there is no containers in the shipyard return None
        if self.isEmpty():
            return         
        temp = self._cont._first              
        
        #while theres containers in the shipyard print the container weight and destinations

        while temp != None:
            
            print("Destination " + str(temp._dest) + " Container weight " + str(temp._weight))
            print()
            #print(temp._dest, temp._weight)
            
            #prints package content
            temp.printAll()
            temp = temp._next
            

    def printDest(self,dest):
           
        #if there is no containers in the shipyard return None
        if self.isEmpty():
            return   
        #reference to package
        temp = self._cont._first              
         
        #while theres containers in the shipyard print the container weight and destinations

        while temp != None:
        #if the destination matches with the references destination then call the 
        #print all method and it will only print all for the matching destination           
            if temp._dest == dest:
                
                print("Destination " + str(temp._dest) + " Container weight " + str(temp._weight))
                print()                
                #prints package content
                temp.printAll()
            temp = temp._next
        
      
    
               
            #print("Container Destination " + str(temp._dest) + " Total weight " + str(pac_weight))
               

    def search(self,owner,dest, weight):
        """The purpose of this method is to search for a package. """
        
        #container is referenced
        temp = self._cont._first
       
        while temp != None:
            #while the container is not none. it will access the Package in the container
            #the search method will be used. What it will do is search for the Package 
            #in the container
            temp.search(owner,dest,weight)
            temp = temp._next      
            
    
   
        

    def ship(self,dest):
        """The purpose of this method is remove all containers going to a specified
        destination.  
        Paramater dest string
        returns: None"""
        #reference to the container
        if self.isEmpty():
            return              
        temp = self._cont._first
        #initlizes count and weight to be 0
        count = 0
        weight = 0
        
        #if the first container is the one we want to remove the container next to it will become
        #the new first container
        if temp._dest == dest:
            self._cont._first = temp._next
            print(f"total weight shipped out for {dest} is {temp._weight}. The count of containers shipped 1")   
            return
        
        if temp != None: 
                while temp._next != None: 
                    #if the destination matches then add the count by 1
                    #add the total weight together
                    if temp._next._dest == dest: 
                        count =  count + 1
                        weight += temp._next._weight
                        #delete the container and the container which is not 
                        #the destination to be shipped out is left in the shipyard
                        temp._next = temp._next._next 
                    else:
                        temp = temp._next    
                        
        print(f"total weight shipped out for {dest} is {weight}. The count of containers shipped {count}")   

                
       
       
   
   

class Empty(Exception):
    pass


def test():
    """Test function that displays all required methods. Assumption made, if a package
    or container is not in the system. The methods will return None and do nothing.
    status will be displayed only if the item is there. Since the specs didn't ask for it."""
    s= Shipyard()
    
    s.add("tony", "Mexico", 221)
    s.add("lilly", "Mexico", 323)          
    s.add("Tom", "Brazil", 293)
    s.add("Rob", "Brazil", 192)
    s.add("Bill", "Alberta", 34)
    s.add("sally", "Alberta", 34)
    s.add("chuck", "Alberta", 23)
    s.add("mike", "Alberta", 323)
    s.add("Ali", "Ghana", 45)
    s.add("mike", "Ny", 582)
    s.add("bob", "Spain", 1932)
    s.add("molly", "Spain", 120)
    s.add("rick", "Spain", 1900)
  
    
    """prints the id weight destination and owner. The packkages are ordered from 
    smallest to largest. The containers are in alphabetical order"""    
    
    s.printAll()
    print()
    print("**Next Test print container information **" )
    print()
    s.printContainers()  
    print()
    print("**Next Test search by id**")
    print()
    s.search_by_id(13163)
    print()
    print("**Next Test print destination for Mexico**")
    print()
    s.printDest("Mexico")
    print()
    print("** Next Test search by owner destination and weight")
    print()
    s.search("molly", "Spain", 120)
    print()
    print("**Next Test remove by id. Id 16387 will be removed from the Alberta container")
    print("**Print packages in the Alberta Container after removal** ")
    print()
    #To see if the id has been removed we must print out the shipyard manifest again
    #as you can see the package was removed and is no longer in the container Alberta.
    s.remove_by_id(16387)
    s.printDest("Alberta")
    print()
    print("**Next Test remove by owner destination weight lets remove (Tom, Brazil, 293)**")
    print("**Print packages in the Brazil container after removal** ")
    s.remove("Tom", "Brazil", 293)
    #once again print the shipyard manifest to confirm if the package has been removed
    print()
    s.printDest("Brazil")
    #note that the weight of the containers decreased when the package is removed
    #also the remove method displays it can remove a Package from anywhere in the list
    #front behind or middle
    print()
    print("**Next Test ship out the containers. Containers spain will be removed**")
    print("**Containers and packages remaining after removals** ")
    print()
    #we initially had 3 containers going to spain. With the ship method all three
    #of the containers are shipped out and removed from the shipyard. The total
    #weight shipped is added.
    s.ship("Spain")
    print()
    s.printAll()
    print()
    
  

   
def main():
    loop = True
    s = Shipyard()
    while loop:
        #adds to the container
        choice = user_choice()
        if choice == 1:
            owner = input("Enter owner: ") 
            owner = correct_alpha(owner)          
            dest = input("Enter destination: ")  
            dest = correct_alpha(dest)
            weight = input("Enter weight: ")
            weight = correct_int(weight)
            s.add(owner , dest.capitalize() , int(weight))
        
        #prints out the destination
        if choice == 2:
            dest = input("Enter a destination: ")
            print()
            dest = correct_alpha(dest)
            s.printDest(dest.capitalize())
        
        #prints shipyard manifest     
        if choice == 3:
            s.printAll()
        
        #prints all container information    
        if choice == 4:
            s.printContainers()
        
        #searches for package by id    
        if choice == 5:
            pack_id = input("Enter a package id to search: ")
            pack_id = correct_int(pack_id)
            s.search_by_id(pack_id)
        
        #ships out all containers give a single destination     
        if choice == 6:
            dest = input("Enter a destination to ship: ")
            dest = correct_alpha(dest.capitalize())
            s.ship(dest)
        
        #To see if an item has been removed print out the shipping manifest 
        if choice == 7:
            pack_id =  input("Enter an id to remove a package: ")
            pack_id = correct_int(pack_id)
            s.remove_by_id(pack_id)
            
            
        
        #exits the menu    
        if choice == 8:
            loop = False
 



def user_choice():
    """The purpose of this function is to make sure the user enters the correct
    inputs. and print out a menu for the user look at.  
    Paramater: None   Returns integer """
    print()
    print("1. Insert new package \n2. Print shipping manifest for destination \n3. Print shipyard manifest")
    print("4. Print container information \n5. Status of Package(search) \n6. Ship out Containers \n7. Remove Package \n8. Quit"  )
    print()
    
      
    choice = input("Please select one of the options 8 to quit: ")
    print()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > 8:
        choice = input("Please select one of the options 8 to quit: ")   
        print()
    return int(choice)

  
                    
def correct_int(choice):
    """the purpose of this function is to validate an input:
    paramater choice: intger  returns integer"""
    
    while not choice.isdigit():
        choice = input("Please try again enter an integer number: ")   
    return int(choice)

def correct_alpha(choice):
    """the purpose of this function is to validate an input:
    paramater choice: string  returns string"""    
    while not choice.isalpha():
        choice = input("Please try again enter an alpha character:  ")   
    return  choice    
    
     
if __name__ == "__main__":
    main()
