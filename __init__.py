from mycroft import MycroftSkill, intent_file_handler


class IntroduceYou(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('you.introduce.intent')
    def handle_you_introduce(self, message):
        self.speak_dialog('you.introduce')


def create_skill():
    return IntroduceYou()

