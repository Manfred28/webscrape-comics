from plyer import notification

def send_notification(episodes_downloaded, comic_name):
    if episodes_downloaded > 0:
        notification.notify(
        title = comic_name,
        message = str(episodes_downloaded) + " Episode(s) Downloaded"
        )