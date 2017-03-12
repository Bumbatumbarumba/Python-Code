class SocialAddressBook:
    def __init__(self):
        """Creates empty address book"""
        self.addressBook = {}
        self.friendDict = {}
        ...
    def addName(self, name, address):
        """Adds name to address book, with address and
        no friends"""
        self.addressBook[name] = address
        ...
    def addFriend(self, name, friend):
        """Adds friend to the set of friends of name"""
        if name in self.friendDict:
            self.friendDict[name].add(friend)
        else:
            self.friendDict[name] = {friend}
        ...
    def address(self, name):
        """Returns the address of name"""
        return 'Name: ' + str(name) + ' | Address: ' + str(self.addressBook[name])
        ...
    def friends(self, name, degree):
        """
        self.name = name
        if degree <= 0:
            return set()
        else:
            FriendList = self.fri[name]
            n = 1
            while n < degree:
                for name in FriendList:
                    if name in self.fri:
                        FriendList = FriendList|self.fri[name]
                    else:
                        pass
                n = n+1
            if self.name in FriendList:
                FriendList.discard(self.name)
            return FriendList
        """

        self.name = name
        if degree <= 0:
            return set()
        else:
            FriendList = self.friendDict[name]
            n = 1
            while n < degree:
                for name in FriendList:
                    if name in self.friendDict:
                        FriendList = FriendList|self.friendDict[name]
                    else:
                        pass
                n = n+1
            if self.name in FriendList:
                FriendList.discard(self.name)
            return FriendList
