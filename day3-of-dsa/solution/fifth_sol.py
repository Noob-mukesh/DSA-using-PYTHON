from dataclasses import  dataclass
@dataclass
class Team:
    name:list
    
    def display_name(self,find_name):
        if find_name in self.name:
            return f"{find_name} name is present "
        else:
            
            return f"{find_name} name is absent"
cricket_team=Team(["mukesh","kohli","rohit"])
name_search=input("provide name to search in team present or absent:- ")
print(cricket_team.display_name(name_search))