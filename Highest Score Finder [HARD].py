class Cricketer:
    def __init__(self, name, runs, wickets):
        self.__name = name  # Private string variable
        self.__runs = runs  # Private integer variable
        self.__wickets = wickets  # Private integer variable

    @property
    def GetName(self):
        return self.__name

    @property
    def GetRuns(self):
        return self.__runs

    @property
    def GetWickets(self):
        return self.__wickets

    def DisplayStats(self):
        print(f"Name: {self.__name}")
        print(f"Runs: {self.__runs}")
        print(f"Wickets: {self.__wickets}")


def FindTopScorer(team_array):
    top_scorer = team_array[0]
    max_runs = team_array[0].GetRuns

    for i in range(1, len(team_array)):
        current_runs = team_array[i].GetRuns
        if current_runs > max_runs:
            max_runs = current_runs
            top_scorer = team_array[i]

    return top_scorer


Team = []

Team.append(Cricketer("Babar Azam", 450, 2))
Team.append(Cricketer("Shaheen Afridi", 50, 35))
Team.append(Cricketer("Mohammad Rizwan", 380, 0))
Team.append(Cricketer("Shadab Khan", 200, 25))
Team.append(Cricketer("Fakhar Zaman", 420, 0))

top = FindTopScorer(Team)

top.DisplayStats()
print(f"{top.GetName} is the top scorer with {top.GetRuns} runs")
