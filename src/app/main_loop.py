from core import SSHConnection
from core import Course
from .channel_handler import ChannelHandler
import time

class MainLoop:

    def __init__(self):
        self.client = SSHConnection()
        self.loop_started = False
        self.channel = None
        self.classes = []

    def start_loop(self):
        if self.loop_started:
            raise ValueError("This instance is already in another loop, create a new instance")

        user_classes = []

        print("########################### WARNING ################################")
        print("This automated class scheduler does not guarantee to work \n \
            make sure CLASSES YOU INPUT DO NOT CONFLICT WITH EACH OTHER AND \n \
            THAT YOU HAVE ALL THE PREREQUISITES AND COREQUISITES. \n \
            IF CORREQUISITES EXIST MAKE SURE TO FIRST INPUT THE CLASS WITHOUT \n \
            THE COREQUISITES ")
        print("#####################################################################")
        print("Enter Classes that you would like to schedule in the following format : {COURSE 4 Letter CODE WITH 4 digit number}-{SECTION}")
        user_input = ""
        while user_input != "exit":

            user_input = str(input("Enter the next class or write exit to exit : "))

            if user_input == 'exit':
                continue

            if  self.validate_class(user_input):
                splitted = user_input.split('-')
                user_classes.append(Course(class_code=splitted[0], section=splitted[1]))
            else:
                print(f"Error processing class {user_input} make sure to follow correct naming convention")

        self.client.connect()
        self.loop_started = True

        semester = input("1st Semester or Second Semester (1/2) ?")

        channel_handler  = ChannelHandler(channel = self.client.get_channel(), time = None, to_schedule = user_classes, semester=semester)

        # Handle Channel Interaction
        channel_handler.start_loop()

        self.client.close()

    def validate_class(self, user_input):
        if user_input == "exit":
            return False

        if(len(user_input) < 8):
            return False

        splitted = user_input.split('-')

        return len(splitted[0]) == 8 and len(splitted[1]) == 3
