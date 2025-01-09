# -*- coding: utf-8 -*-
import os
import subprocess
from git_auto_commit import git_auto_commit  # Импортируем функцию из твоего скрипта

def run_server():
    try:
        # Запуск Django-сервера
        subprocess.run(["python", "manage.py", "runserver"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске сервера: {e}")
    finally:
        # Выполняем автоматический коммит после завершения сервера
        git_auto_commit()

if __name__ == "__main__":
    run_server()