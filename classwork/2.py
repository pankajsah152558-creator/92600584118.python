event_manager/
│── __init__.py
│── registration.py
│── scheduling.py
└── reporting.py
main.py

# In-memory storage for registered participants
participants = []

def register_participant(name, email, category):
    """Registers a participant and adds them to the list."""
    participant_id = len(participants) + 1
    record = {
        "id": participant_id,
        "name": name,
        "email": email,
        "category": category
    }
    participants.append(record)
    print(f"[Success] Registered {name} (ID: {participant_id})")
    return record

def get_all_participants():
    """Returns the list of all registered participants."""
    return participants

schedule = []

def add_event(title, time, location):
    """Adds a new event to the schedule."""
    event = {
        "title": title,
        "time": time,
        "location": location
    }
    schedule.append(event)
    print(f"[Scheduled] {title} at {time} in {location}")
    return event

def get_schedule():
    """Returns the scheduled events."""
    return schedule

from .registration import get_all_participants

def generate_summary_report():
    """Displays a formatted summary report of participants."""
    registered = get_all_participants()
    
    print("\n" + "=" * 40)
    print("      EVENT PARTICIPATION REPORT      ")
    print("=" * 40)
    print(f"Total Registrations: {len(registered)}\n")
    
    if not registered:
        print("No participants registered yet.")
        return

    print(f"{'ID':<5} | {'Name':<20} | {'Category':<10}")
    print("-" * 40)
    for p in registered:
        print(f"{p['id']:<5} | {p['name']:<20} | {p['category']:<10}")
    print("=" * 40 + "\n")
    
    from .registration import register_participant, get_all_participants
from .scheduling import add_event, get_schedule
from .reporting import generate_summary_report

# Importing directly from the package submodules
from event_manager.registration import register_participant
from event_manager.scheduling import add_event
from event_manager.reporting import generate_summary_report

def main():
    print("--- College Event Management System ---\n")

    # 1. Register Participants
    print("--- Registering Participants ---")
    register_participant("Alice Smith", "alice@college.edu", "Student")
    register_participant("Prof. John Doe", "jdoe@college.edu", "Faculty")
    register_participant("Bob Johnson", "bob@college.edu", "Student")

    # 2. Schedule Event Sessions
    print("\n--- Scheduling Events ---")
    add_event("Keynote Speech", "10:00 AM", "Auditorium A")
    add_event("Codeathon", "01:30 PM", "Lab 3")

    # 3. Generate Report
    generate_summary_report()

if __name__ == "__main__":
    main()
