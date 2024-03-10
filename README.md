# BLACK-LOTUS-5400
## Black Lotus Quest Management System

Black Lotus is a Python-based quest management system designed to manage player quests, points, and ranks. This system allows users to interactively credit or deduct points, track quests, view activity logs, and monitor their rank progression.

## Requirements
- Python 3.x

## Usage
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the Python script (`black_lotus.py`).
3. Run the script using the command `python black_lotus.py`.
4. Follow the on-screen prompts to interact with the Black Lotus quest management system.

## Functionality
- **Credit Points:** Allows users to credit points to their account or deduct points from their account.
- **Display Log:** Displays the activity log of the player.
- **Save Log to TXT:** Saves the activity log to a text file.
- **Display Rank:** Displays the current rank and points of the player.
- **Quests:** Allows users to add new quests, complete quests, and view completed quests.
- **Save and Exit:** Saves all player data and exits the program.
- **Show Log File Location:** Displays the location of the saved log file.

## Quest Class
- The `Quest` class manages quest data, including points, rank, activity log, and completion status.
- Quests are completed by players, and upon completion, players earn points.
- Quest data is stored in JSON format.

## Notes
- Player data is saved in JSON files (`<player_name>_data.json`).
- Activity logs are saved in TXT files (`<player_name>_log.txt`).
- Make sure to enter valid inputs when prompted.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
