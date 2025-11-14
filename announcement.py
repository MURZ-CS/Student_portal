# announcements.py

announcements = {}
counter = 1

def post_announcement(title, message, audience="all"):
    global counter
    announcements[counter] = {"title": title, "message": message, "audience": audience}
    counter += 1
    return "Announcement posted."

def view_announcements(audience=None):
    if audience:
        return {k:v for k,v in announcements.items() if v["audience"] == audience or v["audience"]=="all"}
    return announcements

def delete_announcement(announcement_id):
    if announcement_id in announcements:
        del announcements[announcement_id]
        return "Announcement deleted."
    return "ID not found."
