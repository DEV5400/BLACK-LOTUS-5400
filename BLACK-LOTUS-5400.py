from datetime import datetime
import json
import os

class Player:
    RANK_THRESHOLDS = {
        "OVERLORD": 54000000000,
        "Omega": 5000000,
        "Infinity": 4000000,
        "Mu": 3000000,
        "Delta": 600000,
        "Supreme-Commander": 580000,
        "Supreme-General": 530000,
        "Supreme-Colonel": 480000,
        "Supreme-Major": 470000,
        "Supreme-Captain": 460000,
        "Supreme-Lieutenant": 455000,
        "Supreme-Sergeant": 450000,
        "Supreme-Corporal": 445000,
        "Special Supreme": 440000,
        "Supreme Soldier": 430000,
        "Arch-Commander": 420000,
        "Arch-General": 380000,
        "Arch-Colonel": 340000,
        "Arch-Major": 310000,
        "Arch-Captain": 300000,
        "Arch-Lieutenant": 295000,
        "Arch-Sergeant": 290000,
        "Arch-Corporal": 285000,
        "Special Arch": 280000,
        "Arch Soldier": 270000,
        "Mega-Commander": 260000,
        "Mega-General": 220000,
        "Mega-Colonel": 180000,
        "Mega-Major": 160000,
        "Mega-Captain": 155000,
        "Mega-Lieutenant": 150000,
        "Mega-Sergeant": 145000,
        "Mega-Corporal": 140000,
        "Special Mega": 135000,
        "Mega Soldier": 130000,
        "Vector-Commander": 120000,
        "Vector-General": 110000,
        "Vector-Colonel": 90000,
        "Vector-Major": 70000,
        "Vector-Captain": 60000,
        "Vector-Lieutenant": 55000,
        "Vector-Sergeant": 50000,
        "Vector-Corporal": 45000,
        "Special Vector": 40000,
        "Vector Soldier": 35000,
        "Recruit-Commander": 34000,
        "Recruit-General": 30000,
        "Recruit-Colonel": 24000,
        "Recruit-Major": 20000,
        "Recruit-Captain": 15000,
        "Recruit-Lieutenant": 12000,
        "Recruit-Sergeant": 7000,
        "Recruit-Corporal": 5000,
        "Special Recruit": 3000,
        "Recruit Soldier": 1000,
    }

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.rank = None
        self.log = []
        self.tasks = {}
        self.completed_tasks = set()
        self.load_data()

    def load_data(self):
        file_name = f"{self.name}_data.json"
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                data = json.load(f)
                self.points = data.get("points", 0)
                self.rank = data.get("rank")
                self.log = data.get("log", [])
                self.tasks = data.get("tasks", {})
                self.completed_tasks = set(data.get("completed_tasks", []))

    def _log_activity(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log.append(f"{timestamp} - {message}")

    def _check_promotion(self):
        for rank, threshold in self.RANK_THRESHOLDS.items():
            if self.points >= threshold:
                self.promote(rank)

    def promote(self, new_rank):
        self.rank = new_rank
        self._log_activity(f"Congratulations, {self.name}! You've been promoted to {new_rank}.")

    def update_rank(self):
        self._check_promotion()

    def earn_points(self, points, reason):
        self.points += points
        self._log_activity(f"Earned {points:.2f} points via {reason}.")
        print(f"{self.name} earned {points:.2f} points via {reason}.")
        self.update_rank()

    def lose_points(self, points, reason):
        self.points = max(0, self.points - points)
        self._log_activity(f"Lost {points:.2f} points via {reason}.")
        print(f"{self.name} lost {points:.2f} points via {reason}.")
        self.update_rank()

    def display_log(self):
        print("Activity Log:")
        for entry in self.log:
            print(entry)

    def save_log_to_txt(self):
        file_name = f"{self.name}_log.txt"
        with open(file_name, "w") as f:
            f.write("Activity Log:\n")
            f.writelines('\n'.join(self.log))
        print(f"Activity log saved to {file_name}")

    def display_rank(self):
        print(f"Current rank of {self.name}: {self.rank}")
        print(f"Current points: {self.points:.2f}")

    def tasks_menu(self):
        while True:
            print("\nTasks Menu:")
            print("1. Add New Task")
            print("2. Complete Task")
            print("3. View Completed Tasks")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.complete_task()
            elif choice == "3":
                self.view_completed_tasks()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def add_task(self):
        task_name = input("Enter task name: ")
        try:
            task_points = float(input("Enter task points: "))
            self.tasks[task_name] = task_points
            print(f"Task '{task_name}' added with {task_points:.2f} points.")
            self._log_activity(f"Added task '{task_name}' with {task_points:.2f} points.")
            self.save_data()
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number for task points.")

    def complete_task(self):
        print("Tasks:")
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

        try:
            choice = int(input("Enter the number corresponding to the completed task: "))
            if 1 <= choice <= len(self.tasks):
                completed_task = list(self.tasks.keys())[choice - 1]
                points_earned = self.tasks[completed_task]
                self.earn_points(points_earned, f"completion of task '{completed_task}'")
                self._log_activity(f"Completed task '{completed_task}' with {points_earned:.2f} points.")
                self.completed_tasks.add(completed_task)
                self.save_data()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    def view_completed_tasks(self):
        print("Completed Tasks:")
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            for task in self.completed_tasks:
                print(task)

    def save_data(self):
        data = {
            "name": self.name,
            "points": self.points,
            "rank": self.rank,
            "log": self.log,
            "tasks": self.tasks,
            "completed_tasks": list(self.completed_tasks)
        }
        with open(f"{self.name}_data.json", "w") as f:
            json.dump(data, f)

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name, 1000.0)

    while True:
        print("\nOptions:")
        print("1. Credit Points")
        print("2. Display Log")
        print("3. Save Log to TXT")
        print("4. Display Rank")
        print("5. Tasks")
        print("6. Save and Exit")
        print("7. Show Log File Location")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                points_change = float(input("Enter points earned/lost: "))
                reason = input("Enter the reason: ")
                if points_change >= 0:
                    player.earn_points(points_change, reason)
                else:
                    player.lose_points(-points_change, reason)
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number for points.")
        elif choice == "2":
            player.display_log()
        elif choice == "3":
            player.save_log_to_txt()
        elif choice == "4":
            player.display_rank()
        elif choice == "5":
            player.tasks_menu()
        elif choice == "6":
            player.save_data()
            print("Data saved. Exiting...")
            break
        elif choice == "7":
            log_file_name = f"{player.name}_log.txt"
            log_file_path = os.path.abspath(log_file_name)
            print(f"Log file is saved at: {log_file_path}")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
