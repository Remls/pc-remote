from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from commands import commands_list
from commands.remote import answer_remote
from secrets import BOT_TOKEN
import datetime, logging


# Record startup time
with open("docs/start_time.txt", "w") as f:
    f.write(str(datetime.datetime.now()))


updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format="%(asctime)s - %(levelname)s - [%(name)s] %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)


for command in commands_list:
    pass_args = len(commands_list[command]) > 1         # True if 2 or more values present(function to run, if pass_args, [if pass_job_queue])
    pass_job_queue = len(commands_list[command]) == 3   # True if 3 values present (function to run, if pass_args, if pass_job_queue)
    handler = CommandHandler(
        command,
        commands_list[command][0],
        pass_args=pass_args,
        pass_job_queue=pass_job_queue
    )
    dispatcher.add_handler(handler)
logger.info("Listening for {} command{}".format(
    len(commands_list),
    "s" if len(commands_list) > 1 else ""
))

# Register one handler for all text messages
handler = MessageHandler(Filters.text, answer_remote)
dispatcher.add_handler(handler)
logger.info("Registered keyboard remote handler")


updater.start_polling(clean = True)
updater.idle()