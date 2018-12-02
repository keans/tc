import os


CONFIG_DIR = os.path.expanduser("~/.config/tc")
if not os.path.exists(CONFIG_DIR):
    # create config directory, if not existing
    os.makedirs(CONFIG_DIR)

# current project
CURRENT_PROJECT = os.path.join(CONFIG_DIR, "current")

# current project
PROJECTS = os.path.join(CONFIG_DIR, "projects.json")
