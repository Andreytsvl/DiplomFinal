import os
import logging
from git import Repo
from datetime import datetime
#import atexit
from logging.handlers import RotatingFileHandler


# Создаём папку logs, если её нет
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

handler = RotatingFileHandler(
    os.path.join(log_dir, 'git_auto_commit.log'),
    maxBytes=1024 * 1024 * 5,  # 5 МБ
    backupCount=3,  # Хранить 3 файла логов
)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    #filename=os.path.join(log_dir, 'git_auto_commit.log'),  # Логи будут сохраняться в этот файл
    #filemode='a',  # Режим добавления (append) Если есть хендлер, эти строки не нужны.
    handlers=[handler],
)

logger = logging.getLogger(__name__)



# Путь к репозиторию
repo_path = r'C:\Users\User\Desktop\DiplomProject\DiplomProject'

# Инициализация репозитория
repo = Repo(repo_path)


def git_auto_commit():
    try:
        # Логируем начало выполнения
        logger.info("Начало выполнения скрипта git_auto_commit.")

        # Проверяем, есть ли изменения
        if repo.is_dirty():
            # Добавляем все изменения
            repo.git.add('--all')
            logger.info("Все изменения добавлены в индекс Git.")

            # Создаём сообщение для коммита
            commit_message = f"Auto-commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            logger.info(f"Сообщение коммита: {commit_message}")

            # Создаём коммит
            repo.index.commit(commit_message)
            logger.info("Коммит успешно создан.")

            # Отправляем изменения в удалённый репозиторий
            origin = repo.remote(name='origin')
            current_branch = repo.active_branch.name
            origin.push(refspec=f'{current_branch}:{current_branch}')
            logger.info(f"Изменения отправлены в ветку {current_branch} на GitHub.")

            logger.info("Скрипт успешно завершён.")
        else:
            logger.info("Нет изменений для коммита.")
    except Exception as e:
        # Логируем ошибку
        logger.error(f"Ошибка: {e}", exc_info=True)

#atexit.register(git_auto_commit)

if __name__ == "__main__":
    pass
    git_auto_commit()
    #Запуск от команды python git_auto_commit.py