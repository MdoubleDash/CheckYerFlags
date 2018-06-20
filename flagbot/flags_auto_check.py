"""Background process for checking flag counts"""
from threading import Thread
from flagbot import flags
from flagbot.logger import auto_logger


class AutoFlagThread(Thread):
    def __init__(self, event, utils, config, priority, room, thread_list, next_rank = None):
        Thread.__init__(self)
        self.stopped = event
        self.utils = utils
        self.config = config
        self.priority = priority
        self.users = []
        self.room = room
        self.thread_list = thread_list
        self.next_rank = next_rank

    def run(self):
        if self.priority == 1:
            #High priority
            while not self.stopped.wait(300):
                self.check_flags_hp()
        else:
            self.check_flags_lp()
            while not self.stopped.wait(1800):
                self.check_flags_lp()

    def check_flags_lp(self):
        cu = self.room.get_current_users()
        self.users = self.utils.checkable_user_ids(cu)
        for u in self.users:
            flagdata = flags.check_flags(None, None, self.config, u.id, False)
            flags_to_next_rank = flagdata["next_rank"]["count"] - flagdata["flag_count"]
            auto_logger.info(f"[LP] {u.name} needs {flags_to_next_rank} more flags for their next rank.")
            if flags_to_next_rank <= 10:
                self.swap_priority(u, flagdata["next_rank"])
                auto_logger.info(f"[Moved] User {u.name} is {flags_to_next_rank} flags away from their next rank and is therefore moved to the high priority queue")

    def check_flags_hp(self):
        if len(self.users) > 0:
            for u in self.users:
                flagdata = flags.check_flags(None, None, self.config, u.id, False)
                flags_to_next_rank = flagdata["next_rank"]["count"] - flagdata["flag_count"]
                flags_from_current_rank = flagdata["flag_count"] - flagdata["current_rank"]["count"]
                if flags_to_next_rank <= 0 and flags_from_current_rank > 10:
                    self.swap_priority(u, flagdata["next_rank"])
                    self.utils.post_message(f"{u.name} has reached the rank {flagdata['next_rank']['title']} ({flagdata['next_rank']['description']}) for {flagdata['next_rank']['count']} helpful flags. Congratulations!")
                    auto_logger.info(f"[Moved] User {u.name} has reached their next rank and is therefore moved to the low priority queue")
                elif flags_from_current_rank <= 10:
                    self.swap_priority(u, flagdata["next_rank"])
                    self.utils.post_message(f"{u.name} has reached the rank {flagdata['current_rank']['title']} ({flagdata['current_rank']['description']}) for {flagdata['current_rank']['count']} helpful flags. Congratulations!")
                    auto_logger.info(f"[Moved] User {u.name} has reached their next rank and therefore moved to the low priority queue")
                else:
                    auto_logger.info(f"[HP] {u.name} needs {flags_to_next_rank} more flags for their next rank.")

    def swap_priority(self, user, next_rank):
        if self.priority == 1:
            #From high priority to low priority
            try:
                self.users.remove(user)
                self.thread_list[0].users.append(user)
            except ValueError:
                pass
        else:
            #From low priority to high priority
            try:
                self.users.remove(user)
                self.thread_list[1].users.append(user)
                self.thread_list[0].next_rank = next_rank
            except ValueError:
                pass