from mycroft import MycroftSkill, intent_file_handler


class OfficeStopLight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('light.stop.office.intent')
    def handle_light_stop_office(self, message):
        self.speak_dialog('light.stop.office')


def create_skill():
    return OfficeStopLight()

