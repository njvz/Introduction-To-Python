#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
# 
# Nathan Van Zandt

class Date:
    """ a class that stores and manipulates dates that are
        represented by a day, month, and year.
    """
    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month 
        self.day  = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s


    def is_leap_year(self):
        """ returns True if the called object is
            in a leap year, and False otherwise
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False


    def copy(self):
        """ returns a new object with the same month, day, and year
            as the called object (self)
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####

    def advance_one(self) : 
        """ takes object self and changes self so it represents 
            one calender day after the original day 
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      
      
        if self.is_leap_year() == True:
            days_in_month[2] = 29 
        if self.month == 12 and self.day == days_in_month[12] :
            self.year += 1
        if self.day != days_in_month[self.month]:
            self.day += 1  
        else:
            self.day = 1
            if self.month != 12: 
                self.month +=1 
            else : 
                self.month = 1
        

    def advance_n(self, n):
        """ takes object self and integer n and changes self so that  
            it represents n calender days after the original
        """
        print(self)
        if n > 0 :
            while n > 0 :
                self.advance_one()
                print(self)
                n -= 1 
                

    def __eq__(self, other):
       """ takes object self and another date and if they have the same day, month, and year, attributes, return true
           else, return false     
       """
       month = False
       day = False
       year = False
       
       if self.month == other.month :
           month = True 
       if self.day == other.day : 
           day = True 
       if self.year == other.year : 
           year = True 
       if month == True and day == True and year == True :
           return True
       else : 
           return False
       

    def is_before(self, other):
        """ takes object self and day other and returns true if self  
            is before other, false otherwise                
        """
        if self.year < other.year :
            return True           
        elif self.month < other.month and self.year == other.year : 
            return True 
        elif self.day < other.day and self.month == other.month: 
            return True 
        else : 
            return False
        

    def is_after(self, other):
        """ takes object self and day other and returns true if self  
            is after other, false otherwise    
        """ 
        if self.year > other.year :
            return True       
        elif self.month > other.month and self.year == other.year: 
            return True 
        elif self.day > other.day and self.month == other.month: 
            return True 
        else : 
            return False
        

    def days_between(self, other):
        """ takes object self and day other and returns number of days between self 
            and other 
        """
        counter = 0
        copyself = self.copy()
        copyother = other.copy()
        if copyself.__eq__(copyother) == True:
            return 0
        elif copyself.is_after(copyother) == True :
            while copyself.__eq__(copyother) == False : 
                copyother.advance_one()
                counter += 1
            return counter
        elif copyself.is_before(copyother) == True : 
            while copyself.__eq__(copyother) == False :
                copyself.advance_one()
                counter -= 1
            return counter 
        
        
    def day_name(self):
        """ takes object self that represents a date and returns the day of the week  
            that self represents
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        d1 = Date(11, 9, 2020) #monday
        if self.days_between(d1) % 7 == 0:
            return day_names[0]
        elif self.days_between(d1) % 7 == 1:
            return day_names[1]
        elif self.days_between(d1) % 7 == 2:
            return day_names[2]
        elif self.days_between(d1) % 7 == 3:
            return day_names[3]
        elif self.days_between(d1) % 7 == 4:
            return day_names[4]
        elif self.days_between(d1) % 7 == 5:
            return day_names[5]
        else : 
            return day_names[6]
        
           
            
            
        
    
   
            
            
        
        
        
        
        
        
        
        
        
        
        
        