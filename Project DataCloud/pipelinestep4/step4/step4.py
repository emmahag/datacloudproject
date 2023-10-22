#filter notification

irrelevant = False
def filterNotification(notifications):
    for notif in notifications:
        if notif == irrelevant:
            notifications.delete(notif)
            print("filtered")
            
    return notifications