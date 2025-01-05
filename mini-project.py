class MiniProjectMission:
    """
    Represents a mini-project mission in a course.
    """

    def __init__(self, mission_type, description):
        """
        Initializes a MiniProjectMission object.

        Args:
            mission_type: The type of mission ("Application" or "Accumulative").
            description: A brief description of the mission.
        """
        self.mission_type = mission_type
        self.description = description
        self.tools = []  # List to store required tools

    def add_tool(self, tool):
        """Adds a tool to the list of required tools."""
        self.tools.append(tool)

    def get_mission_type(self):
        """Returns the type of the mission."""
        return self.mission_type

    def get_description(self):
        """Returns the description of the mission."""
        return self.description

    def get_tools(self):
        """Returns a list of required tools."""
        return self.tools

    def __str__(self):
        """Returns a string representation of the mission."""
        return f"Mission Type: {self.mission_type}\nDescription: {self.description}\nTools: {', '.join(self.tools)}"


if __name__ == "__main__":
    # Example usage
    mission1 = MiniProjectMission("Application", "Build a simple calculator")
    mission1.add_tool("Python")
    mission1.add_tool("Calculator library (optional)")

    mission2 = MiniProjectMission("Accumulative", "Design a user interface for the course project")
    mission2.add_tool("Figma")
    mission2.add_tool("Adobe XD")

    print(mission1)
    print("\n")
    print(mission2)