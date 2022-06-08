from datetime import datetime, time

class DataHandler:
    """
    This class handles the processing of the contest data
    """
    def __init__(self, contest_data: list[dict] = []):
        self.__contest_data = contest_data

    @property
    def contest_data(self):
        return self.__contest_data

    @contest_data.setter
    def contest_data(self, contest_data):
        self.__contest_data = contest_data

    def add_contest_line(self, contest_line):
        """
        Add a line of data to the current DataHandler
        """
        keys = ["ci", "first_surname", "second_surname", "name", "middle_name_initial", "sex", "age", "execution_time"]
        d = dict(zip(keys, contest_line))
        self.__contest_data.append(d)

    @staticmethod
    def match_age_group(age_group, age) -> bool:
        """
        Returns True if the age is inside the age_group
        """
        match age_group:
            case "Juniors":
                return age <= 25
            case "Seniors":
                return age > 25 and age <= 40
            case "Masters":
                return age > 40
            case _:
                return False

    def count_participants_age_group(self, age_group="") -> int:
        """
        Returns the ammount of participants in a given age group
        """
        count = 0
        for contest_line in self.contest_data:
            age = contest_line.get("age")
            if(self.match_age_group(age_group, age)):
                count += 1
        return count

    @staticmethod
    def match_sex(sex_group, sex) -> bool:
        """
        Returns True if the sex is equal to the given sex_group
        """
        match sex_group:
            case "M":
                return sex == "M"
            case "F":
                return sex == "F"
            case _:
                return False

    def count_participants_sex(self, sex_group="") -> int:
        """
        Returns the ammount of participants in a given sex_group
        """
        count = 0
        for contest_line in self.contest_data:
            sex = contest_line.get("sex")
            if(self.match_sex(sex_group, sex)):
                count += 1
        return count

    def get_winner_age_group(self, age_group="") -> dict:
        """
        Returns the dictionary of the winner in a given age_group
        """
        winner_time = time.max
        winner = {}
        for contest_line in self.contest_data:
            age = contest_line.get("age")
            if(self.match_age_group(age_group, age)):
                current_time = contest_line.get("execution_time")
                if current_time < winner_time:
                    winner_time = current_time
                    winner = contest_line
        return winner

    def get_winner_sex(self, sex_group="") -> dict:
        """
        Returns the dictionary of the winner in a given sex_group
        """
        winner_time = time.max
        winner = {}
        for contest_line in self.contest_data:
            sex = contest_line.get("sex")
            if(self.match_sex(sex_group, sex)):
                current_time = contest_line.get("execution_time")
                if current_time < winner_time:
                    winner_time = current_time
                    winner = contest_line
        return winner

    def get_winner_age_group_and_sex(self, age_group="", sex_group="") -> dict:
        """
        Returns the dictionary of the winner in a given age_group and sex_group
        """
        winner_time = time.max
        winner = {}
        for contest_line in self.contest_data:
            age = contest_line.get("age")
            sex = contest_line.get("sex")
            if(self.match_age_group(age_group, age) and self.match_sex(sex_group, sex)):
                current_time = contest_line.get("execution_time")
                if current_time < winner_time:
                    winner_time = current_time
                    winner = contest_line
        return winner

    def get_winner_total(self) -> dict:
        """
        Returns the dictionary of the winner of the contest
        """
        winner_time = time.max
        winner = {}
        for contest_line in self.contest_data:
            current_time = contest_line.get("execution_time")
            if current_time < winner_time:
                winner_time = current_time
                winner = contest_line
        return winner

    def get_average_time_age_group_and_sex(self, age_group="", sex_group="") -> time:
        """
        Returns the average execution time in a given age_group and sex_group
        """
        seconds = 0
        count = 0
        for contest_line in self.contest_data:
            age = contest_line.get("age")
            sex = contest_line.get("sex")
            if(self.match_age_group(age_group, age) and self.match_sex(sex_group, sex)):
                execution_time = contest_line.get("execution_time")
                seconds += execution_time.second + execution_time.minute * 60 + execution_time.hour * 3600
                count += 1  
        return datetime.utcfromtimestamp(seconds//count).strftime("%H:%M:%S")