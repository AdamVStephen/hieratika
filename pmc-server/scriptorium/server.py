#!/usr/bin/python

##
# Standard imports
##
from abc import ABCMeta, abstractmethod
import timeit

##
# Project imports
##
class ScriptoriumServer():
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()
        self.tokens = {}

    def isTokenValid(self, tokenId):
        """Returns true if the token is valid (i.e. if it was created against a valid login).
           If the token is valid the last time at which this token was checked is updated.

           Args:
               tokenId (str): the token to verify.           
 
           Returns:
               True if the token is valid.
        """
        ok = (tokenId in self.tokens)
        if (ok):
            self.tokens[tokenId]["lastInteraction"] = int(time.time())
        return ok

    def login(self, username):
        """Tries to log a new user into the system.
           If successful a token will be associated to this user and registered into the system, so a subsequent call to
           isTokenValid, with this token, will return True.

           Returns:
              A token described as a 32-character hexadecimal string or an empty string if the login fails.
        """
        ok = authenticate(username)
        if (ok):
            log.info("{0} logged in successfully".format(username))
            loginToken = uuid.uuid4().hex
            self.tokens[loginToken] = {"user": username, "lastInteraction": int(time.time())}
        else:
            log.warning("{0} is not registered as a valid user".format(username))
            loginToken = ""
           
        return loginToken

    @abstractmethod
    def load(self, config):
        """ Configures the server.
            TODO
        """
        pass

    @abstractmethod 
    def authenticate(self, username):
        """ Authenticates a user into the system.
            Returns:
                True if the user is successfully authenticated.
        """
        pass



    @abstractmethod
    def getPlantInfo(self, pageName, requestedVariables):
        """ Returns all the variables information related to any set of plants.
            See getVariableInfo for details about the variable information.  

        Args:
           pageName (str): name of the page (which corresponds to the name of the configuration).
           variables ([str]): identifiers of the variables to be queried.
        Returns:
            A list with information about all the plant variables 
        """
        pass

    @abstractmethod
    def getSchedules(self, username, pageName):
        """ TODO
        
        Args:
            username(str): TODO
            pageName(str): TODO

        Returns:
            TODO
        """
        pass

    @abstractmethod
    def getUsers(self, request):
        """
        Returns:
            All the system users.
        """
        pass

    @abstractmethod
    def getPages(self, request):
        """
        Returns:
            All the pages that are available.
        """
        pass

    @abstractmethod
    def getPage(self, pageName):
        """Gets the page associated to a given name

           Args:
               token (str): the page name to query.

           Returns:
               The Page or None if the name is not found.
        """
        pass

    @abstractmethod
    def getSchedule(self, scheduleId):
        """ TODO define schedule structure

        Args:
            scheduleId (str): unique schedule identifier.
        Returns:
            Information about the requested schedule.
        """
        pass

    @abstractmethod
    def getScheduleVariables(self, scheduleId):
        """ Gets all the variables values associated to a given schedule.
        
        Args:
            scheduleId(str): unique schedule identifier.
        Returns:
            An array of {variableId:variableValue} pairs  
        pass
        """

    @abstractmethod
    def updateSchedule(self, tid, scheduleId, variables):
        """ Updates the variable values for a given schedule. Note that these changes are not to be sync into the storage medium.
    
        Args:
            tid (str): unique identifier of the calling thread/process
            scheduleId (str): unique schedule identifier
            variables [{variableId:theVariableId, value:theVariableValue}]:  list of variables to be updated.

        Returns:
            The list of variables that were updated in the form [{id:value}]
        """
        pass

    @abstractmethod
    def createSchedule(self, name, description, username, pageName):
        """ Creates a new schedule.
            TODO
        """
        pass
