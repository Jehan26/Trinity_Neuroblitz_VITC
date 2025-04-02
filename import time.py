import time
import threading
import requests
from queue import PriorityQueue

BASE_URL = "https://fleetbots-production.up.railway.app/api"
VALID_TASKS = ["Soil Analysis", "Irrigation", "Weeding", "Crop Monitoring"]
VALID_DIRECTIONS = ["forward", "backward", "left", "right"]
LOW_MOISTURE_THRESHOLD = 30.0
HIGH_TEMPERATURE_THRESHOLD = 35.0
LOW_BATTERY_THRESHOLD = 20

def start_session():
    """Start a new API session and return session ID"""
    url = f"{BASE_URL}/session/start"
    try:
        response = requests.post(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"[Session] {data.get('message')}")
        return data.get("session_id")
    except requests.RequestException as e:
        print(f"[Error] Starting session: {e}")
        return None

def get_fleet_status(session_id):
    """Get status of entire fleet"""
    url = f"{BASE_URL}/fleet/status?session_id={session_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[Error] Fetching fleet status: {e}")
        return None

def assign_task(rover_id, session_id, task):
    """Assign task to a specific rover"""
    task = task.title()
    if task not in VALID_TASKS:
        print(f"[Error] Invalid task. Choose from {VALID_TASKS}")
        return None

    url = f"{BASE_URL}/rover/{rover_id}/task"
    params = {"session_id": session_id, "task": task}
    
    try:
        response = requests.post(url, params=params, timeout=5)
        response.raise_for_status()
        print(f"[Task] {task} assigned to {rover_id}")
        return response.json()
    except requests.RequestException as e:
        print(f"[Error] Assigning task to {rover_id}: {e}")
        return None

class TaskScheduler:
    """Priority-based task scheduler"""
    def __init__(self):
        self.task_queue = PriorityQueue()

    def add_task(self, rover_id, task_type, priority):
        """Add task with priority"""
        self.task_queue.put((priority, time.time(), rover_id, task_type))
        print(f"[Task] {task_type} added for {rover_id} with priority {priority}")

    def process_tasks(self, session_id):
        """Process the tasks in priority order"""
        while not self.task_queue.empty():
            _, _, rover_id, task = self.task_queue.get()
            assign_task(rover_id, session_id, task)

def main():
    """Entry point for the application"""
    print("\n=== Agricultural Fleet Management System ===")
    
    session_id = start_session()
    if not session_id:
        print("[Error] Failed to initialize system")
        return

    scheduler = TaskScheduler()

    print("\nCommand Menu:")
    print("  task [rover] [task] - Assign task to a rover")
    print("  status - Show fleet status")
    print("  exit - Quit program")

    while True:
        try:
            cmd = input("\n> ").strip().lower()
            parts = cmd.split()

            if not parts:
                continue

            if cmd == 'exit':
                print("Shutting down system...")
                break

            elif cmd == 'status':
                get_fleet_status(session_id)

            elif len(parts) > 2 and parts[0] == 'task':
                assign_task(parts[1], session_id, " ".join(parts[2:]))

            else:
                print("[Error] Invalid command. Type 'exit' to quit.")

        except KeyboardInterrupt:
            print("\nShutting down...")
            break

if __name__ == "__main__":
    main()