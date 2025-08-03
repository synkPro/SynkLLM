#Uncomment below to have file CRUD operations for all entities - Not working now
# import os
# from utils.file_utils import load_data, save_data

# DATA_DIR = "data"

# def get_file_path(entity):
#     return os.path.join(DATA_DIR, f"{entity}.json")

# def create(entity, data):
#     file_path = get_file_path(entity)
#     print(f"Creating for {file_path} for {entity}: {data}")
#     existing = load_data(file_path)
#     existing.append(data)
#     save_data(file_path, existing)
#     return {"status": "success", "message": f"{entity} created"}

# def retrieve(entity, filters):
#     file_path = get_file_path(entity)
#     items = load_data(file_path)
#     if not filters:
#         return items
#     # simple exact-match filtering
#     return [item for item in items if all(item.get(k) == v for k, v in filters.items())]

# def update(entity, filters, new_data):
#     file_path = get_file_path(entity)
#     items = load_data(file_path)
#     updated = 0
#     for item in items:
#         if all(item.get(k) == v for k, v in filters.items()):
#             item.update(new_data)
#             updated += 1
#     save_data(file_path, items)
#     return {"status": "success", "updated": updated}

# def delete(entity, filters):
#     file_path = get_file_path(entity)
#     items = load_data(file_path)
#     original_count = len(items)
#     items = [item for item in items if not all(item.get(k) == v for k, v in filters.items())]
#     save_data(file_path, items)
#     return {"status": "success", "deleted": original_count - len(items)}

# def handle_request(intent, entity, data, filters):
#     if intent == "create":
#         return create(entity, data)
#     elif intent == "retrieve":
#         return retrieve(entity, filters)
#     elif intent == "update":
#         return update(entity, filters, data)
#     elif intent == "delete":
#         return delete(entity, filters)
#     else:
#         return {"status": "error", "message": "Unknown intent or entity"}
    

#Uncomment below to have simple CRUD operations for all entities
def create_task(data):
    print(f"Creating task: {data}")
    return {"status": "success", "message": "Task created"}

def get_task(filters):
    print(f"Fetching tasks with filters: {filters}")
    return {"status": "success", "tasks": []}

def create_note(data):
    print(f"Creating note: {data}")
    return {"status": "success", "message": "Note created"}

def get_note(filters):
    print(f"Fetching notes with filters: {filters}")
    return {"status": "success", "notes": []}

def create_event(data):
    print(f"Creating event: {data}")
    return {"status": "success", "message": "Event created"}

def get_event(filters):
    print(f"Fetching events with filters: {filters}")
    return {"status": "success", "events": []}

def create_user(data):
    print(f"Creating user: {data}")
    return {"status": "success", "message": "User created"}

def get_user(filters):
    print(f"Fetching user with filters: {filters}")
    return {"status": "success", "user": []}

def handle_request(intent, entity, data, filters):
    if intent == "create":
        if entity == "tasks":
            return create_task(data)
        elif entity == "events":
            return create_event(data)
        elif entity == "notes":
            return create_note(data)
        elif entity == "users":
            return create_user(data)
    elif intent == "retrieve":
        if entity == "tasks":
            return get_task(filters)
        elif entity == "events":
            return get_event(filters)
        elif entity == "notes":
            return get_note(filters)
        elif entity == "users":
            return get_user(filters)
    elif intent == "update":
        return {"status": "success", "message": f"{entity.capitalize()} updated"}
    elif intent == "delete":
        return {"status": "success", "message": f"{entity.capitalize()} deleted"}
    else:
        return {"status": "error", "message": "Unknown intent or entity"}