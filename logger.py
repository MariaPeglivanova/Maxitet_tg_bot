class Logger:
    def __init__(self, log_file="log.txt"):
        self.log_file = log_file

    def log(self, user_id, command):
        with open(self.log_file, "a") as file:
            file.write(f"{user_id} использовал {command}\n")
