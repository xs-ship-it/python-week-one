class User:
    """
    Class that generates new instances of contacts.
    """
    user_list=[]
    def __init__(self,account_name,user_name,password):
     
      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
    
    contact_list = [] # Empty contact list
 
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 
    @classmethod
    def find_by_account_name(cls,user_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user          
    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user-name: user_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False