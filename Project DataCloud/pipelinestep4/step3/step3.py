#createnotification

from plyer import notification

def createNotification(data):
    notification.notify(
        title = 'New Data has arrived',
        message = str(data),
        app_icon = None,
        timeout = 20,
    )