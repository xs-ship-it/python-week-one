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