class RemoteControl:

    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()