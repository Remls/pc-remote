import datetime
from config import BOT_VERSION


def ping(bot, update):
    time_seen = datetime.datetime.now()
    time_sent = update.message.date
    # Precision of times in update object is to the nearest second
    # So there may be times where it rounds up and gives a later time
    # In that case, time_sent is set back 0.5 seconds to give a more plausible value
    if time_sent > time_seen:
        time_sent = time_sent - datetime.timedelta(milliseconds=500)
    time_diff = int((time_seen - time_sent) / datetime.timedelta(milliseconds=1))
    if time_diff >= 1000:
        time_diff = time_diff / 1000
        time_seen_display = "+{:.2f}s".format(time_diff)
    else:
        time_seen_display = "+{}ms".format(time_diff)

    # Get uptime
    start_time = None
    with open("docs/start_time.txt") as f:
        start_time = datetime.datetime.strptime(f.read(), "%Y-%m-%d %H:%M:%S.%f")
    uptime = str(time_seen - start_time).split(".")[0]
    
    update.message.reply_markdown(
        text = ("*PC Remote v{}*\n"
                "*Uptime:* {}\n\n"
                "*Sent:* {}\n"
                "*Seen:* {}").format(
                    BOT_VERSION,
                    uptime,
                    time_sent.strftime("%I:%M:%S %p").lower(),
                    time_seen_display
                ),
        quote = False
    )
