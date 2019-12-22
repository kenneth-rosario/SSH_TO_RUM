import getpass

class UserInformation:

    def __init__(self):
        self.last_4_ssn = getpass.getpass(prompt="Last 4 digits of you SSN")
        self.student_number = getpass.getpass(prompt="Student Number")
        self.date_of_birth = getpass.getpass(prompt="Date of birth in the format MMDDYYYY")
        self.access_code = getpass.getpass(prompt="Enter your 4 code access_code")

    def get_info_for_channel(self):
        return f"{self.last_4_ssn}{self.student_number}{self.date_of_birth}{self.access_code}"
