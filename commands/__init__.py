from commands.remote import send_remote
from commands.ping import ping


# List of commands
needs_args = True
needs_job_queue = True
commands_list = {
    "start": [send_remote],
    "ping": [ping]
}
