import json
import os

def get_user_medicine_file(username):
    return f"data/{username}_meds.json"

def load_medicines(username):
    path = get_user_medicine_file(username)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_medicines(username, meds):
    path = get_user_medicine_file(username)
    with open(path, "w") as f:
        json.dump(meds, f, indent=2)

def add_medicine(username, name, dosage, frequency, notes="", times=None):
    meds = load_medicines(username)
    meds.append({
        "name": name,
        "dosage": dosage,
        "frequency": frequency,
        "notes": notes,
        "times": times or []
    })
    save_medicines(username, meds)


def view_medicines(username):
    meds = load_medicines(username)
    if not meds:
        print("No medicines added yet.")
        return
    for i, med in enumerate(meds, start=1):
        print(f"{i}. {med['name']} - {med['dosage']} - {med['frequency']}")
        if med['notes']:
            print(f"   Notes: {med['notes']}")

def delete_medicine(username, index):
    meds = load_medicines(username)
    if 0 <= index < len(meds):
        removed = meds.pop(index)
        save_medicines(username, meds)
        return True, f"Removed {removed['name']}."
    else:
        return False, "Invalid index."
