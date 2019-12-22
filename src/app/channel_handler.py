from core import UserInformation

class ChannelHandler:

    # Append to keep track of where we ccurrently at in the putty application
    self.current_path = []

    def __init__(self, channel, time, to_schedule):
        self.channel = channel
        self.time = time
        self.to_schedule = to_schedule

    def start_loop(self):
        user = UserInformation()
        print("Inside ChannelHandler")
