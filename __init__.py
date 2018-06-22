from mycroft import MycroftSkill, intent_file_handler


class WhoMess(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mess.who.intent')
    def handle_mess_who(self, message):
        self.speak_dialog('mess.who')


def create_skill():
    return WhoMess()

