# -*- coding: utf8 -*-
import Skype4Py
import pika

class Fetch:
    def __init__(self):
        self.skype = Skype4Py.skype.Skype()
        self.client = self.skype.Client
    def run(self):
        # if skype not running, start up it
        if not self.client.IsRunning:
            self.client.Start(Minimized = True, Nosplash = True)
        # register event handlers
        self.skype.OnAttachmentStatus = self.OnAttach
        self.skype.OnMessageStatus = self.OnMessageStatus
        self.skype.Attach()
        '''
        command = ''
        while not command == 'exit':
            command = raw_input('')
            '''
        # shutdown skype client if it's running
        #if skype.Client.IsRunning:
        #    skype.Client.Shutdown()

    def OnAttach(self, status):
        if status == Skype4Py.apiAttachAvailable:
            self.skype.Attach()
        if status == Skype4Py.apiAttachSuccess:

            self.client.Focus()

            beforeMoodText = self.skype.CurrentUserProfile.MoodText
            afterMoodText = "This text is updated by self.skype.CurrentUserProfile.MoodText = afterMoodText using Skype4Py api"
            self.skype.CurrentUserProfile.MoodText = afterMoodText
            print "The moodtext is change from '%s' to '%s' " % (beforeMoodText, afterMoodText)

            '''
            bookmarkedChats = getBookmarkedChats(skype)
            for chat in bookmarkedChats:
            print chat.Name
            '''


            # Dialogs
            #self.client.OpenAddContactDialog("bluest.org")
            #self.client.OpenAuthorizationDialog("bluest.org")
            #self.client.OpenBlockedUsersDialog()
            #self.client.OpenConferenceDialog()
            #self.client.OenDialog()
            #self.client.OpenFileTransferDialog("bluest.org", "d:")

            # Open a calls page of Option dialog
            '''
OPEN OPTIONS
This command opens the options configuration window.

Syntax:

    -> OPEN OPTIONS <page>
    <- OPEN OPTIONS <page> 

Parameters

    <page>, possible values:
        general
        privacy
        notifications
        soundalerts
        sounddevices
        hotkeys
        connection
        voicemail
        callforward
        video
        advanced 
        '''
            # self.client.OpenOptionsDialog('privacy')
            # self.client.OpenProfileDialog()
            # self.client.OpenSearchDialog()
            # OPEN SENDCONTACTS <username> [ <username2> <username3>]
            # self.client.OpenSendContactsDialog('bluest.org bizrsolson')

            # self.client.OpenSmsDialog('1')
            #self.client.OpenVideoTestDialog()
            #self.client.OpenMessageDialog("bluest.org")

            # OPEN USERINFO <skypename>
            #self.client.OpenUserInfoDialog('developerworks')

            # Tabs
            #self.client.OpenDialpadTab()
            #self.client.OpenLiveTab()
            #self.client.OpenContactsTab()
            #self.client.OpenCallHistoryTab()

            # Wizards
            #self.client.OpenGettingStartedWizard()
            #self.client.OpenImportContactsWizard()

            # MenuItem
            #menuitem = self.client.CreateMenuItem('TEST01', Skype4Py.pluginContextTools, 'Caption text')


            self.skype.SendMessage("bluest.org", "Skype4Py测试消息")

            for chat in self.skype.BookmarkedChats:
                print "Name %s" % chat.Name
                print "FullName %s" % chat.Adder.FullName
                print "About %s" % chat.Adder.About
                print "Birthday %s" % chat.Adder.Birthday
                print "BuddyStatus %s" % chat.Adder.BuddyStatus
                print "City %s" % chat.Adder.City
                print "Country %s" % chat.Adder.Country
                print "CountryCode %s" % chat.Adder.CountryCode
                print "DisplayName %s" % chat.Adder.DisplayName
                print "Handle %s" % chat.Adder.Handle
                print "FullName %s" % chat.Adder.FullName
                print "HasCallEquipment %s" % chat.Adder.HasCallEquipment
                print "Homepage %s" % chat.Adder.Homepage

    # Get bookmarked chats
    # DEPRECATED,Use BookmarkedChats property of skype object
    def getBookmarkedChats(self, skype):
        allchats = skype.Chats
        # Bookmarked Chat list
        bookmarked = []
        for chat in allchats:
            if chat.Bookmarked:
                bookmarked.append(chat)
        return bookmarked
    def OnMessageStatus(self, message, status):
        ""

def callback():
    ''

if __name__ == '__main__':
    fetch = Fetch()
    fetch.run()
