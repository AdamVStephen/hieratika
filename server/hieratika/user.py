#!/usr/bin/env python
__copyright__ = """
    Copyright 2017 F4E | European Joint Undertaking for ITER and
    the Development of Fusion Energy ('Fusion for Energy').
    Licensed under the EUPL, Version 1.1 or - as soon they will be approved
    by the European Commission - subsequent versions of the EUPL (the "Licence")
    You may not use this work except in compliance with the Licence.
    You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl
 
    Unless required by applicable law or agreed to in writing, 
    software distributed under the Licence is distributed on an "AS IS"
    basis, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the Licence permissions and limitations under the Licence.
"""
__license__ = "EUPL"
__author__ = "Andre' Neto"
__date__ = "17/11/2017"

##
# Standard imports
##

##
# Project imports
##

##
# Logger configuration
##

##
# Class definition
##
class User(object):
    """ Describes a hieratika user.
    """

    def __init__(self, username, groups = [], token = None):
        """ Constructs a User object against a given username.
        
        Args:
            username (string): the username.
            groups (UserGroup[]): the groups to which this user belongs to.
        """
        self.username = username
        self.groups = groups
        self.token = token

    def getUsername(self):
        """ Returns the username
       
        Returns: 
            The username.
        """
        return self.username

    def getGroups(self):
        """ Returns the groups that this user belongs to.

        Returns:
            The groups that this user belongs to.
        """
        return self.groups 

    def getToken(self):
        """ Returns the token associated to a login instance of this user (i.e. to a session).
        
        Returns:
            The user session token.
        """
        return self.token

    def setToken(self, token):
        """ Sets the token associated to a login instance of this user (i.e. to a session).
            
            Args:
                token (str): the token which univocally identifies a user in a given session.
        """
        self.token = token

    def __eq__(self, another):
        """ Two users are equal if they have the same username.
           
        Args:
            self (User): this user instance.
            another (User or str): another user or a string. 
        Returns:
            True if self and another username are equal or if another is a string whose value is the self.getUsername().
        """
        if isinstance(self, another.__class__):
            areEqual = (self.getUsername() == another.getUsername())
        else:
            areEqual = (self.getUsername() == str(another))
        return areEqual

    def __cmp__(self, another):
        """ See __eq__
        """
        return (self == another) 

    def __hash__(self):
        """ The class is univocally identified by the username.

        Returns:
            The username.
        """
        return getUsername()

    def asSerializableDict(self):
        """ 
        Returns:
            A json serializable representation of the User which consists on 
            {'username': getUsername(), 'groups': [getGroups().getName(), ...] }
        """
        user = {
            "username": self.getUsername(),
            "groups": map(str, self.getGroups()),
            "token": self.token
        }
        return user

    def __str__(self):
        """ Returns a string representation of an user.
            
            Returns:
                A string representation of an user which consists of the username followed by all the groups to which the user belongs to.
        """
        groups = "["
        for g in self.groups[:-1]:
            groups += g.getName() + "," 
        if (len(self.groups) > 0):
            groups += self.groups[-1].getName()
        groups += "]" 
         
        return "{0} @ ({1}) : {2}".format(self.username, self.token, groups) 