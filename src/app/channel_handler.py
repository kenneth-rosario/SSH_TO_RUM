from core import UserInformation
import core.constants as constants
import time

class ChannelHandler:

    # Append to keep track of where we ccurrently at in the putty application
    current_path = int()

    def __init__(self, channel, time, to_schedule, semester):
        self.channel = channel
        self.time = time
        self.to_schedule = to_schedule
        self.semester = semester

    def start_loop(self):
        user = UserInformation()
        current_path = constants.MAIN_MENU
        server_output = str()
        course_counter = 0

        # Use open ssh channel inside loop
        while course_counter < len(self.to_schedule):

            if self.channel.recv_ready():
                time.sleep(2)
                server_output = self.channel.recv(9999).decode('latin-1')
                print(server_output)
            else:
                time.sleep(0.5)
                continue

            if self.current_path == constants.MAIN_MENU:
                self.channel.send("2")
                time.sleep(1)
                self.current_path = constants.PERSONAL_INFO_PROMPT

            elif self.current_path == constants.PERSONAL_INFO_PROMPT:
                self.channel.send(user.get_info_for_channel())
                self.current_path = constants.SEMESTER_CHOOSE
                time.sleep(1.5)

            elif self.current_path == constants.SEMESTER_CHOOSE:
                self.channel.send(self.semester)
                self.current_path = constants.SEMESTER_ENROLLMENT_OPTIONS

            elif self.current_path == constants.SEMESTER_ENROLLMENT_OPTIONS:
                self.channel.send("A")
                self.current_path = constants.COURSE_ENROLLMENT_INPUT

            elif self.current_path == constants.COURSE_ENROLLMENT_INPUT:
                self.channel.send(self.to_schedule[course_counter].get_class_code() + '\n')
                self.current_path = constants.COURSE_SECTION_INPUT

            elif self.current_path == constants.COURSE_SECTION_INPUT:
                self.channel.send(self.to_schedule[course_counter].get_section() + '\n')
                self.current_path = constants.COURSE_ENROLLMENT_INPUT
                course_counter += 1
                time.sleep(1)

        if self.channel.recv_ready():
            server_output = self.channel.recv(9999).decode('latin-1')
            print(server_output)
