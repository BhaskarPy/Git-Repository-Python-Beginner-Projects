from plyer import notification
title="Hello There"
msg="Welcome to Know Bot"
notification.notify(
    title=title,
    message=msg,
    app_icon=None,
    timeout=10,
    toast=False
)
