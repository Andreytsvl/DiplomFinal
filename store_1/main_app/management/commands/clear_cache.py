import logging
from django.core.management.base import BaseCommand
from django.core.cache import cache

# Настройка логгера
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Очищает весь кеш Django и логирует результат'

    def handle(self, *args, **kwargs):
        try:
            # Очищаем кеш
            cache.clear()
            message = 'Кеш успешно очищен!'
            logger.info(message)  # Логируем успех
            self.stdout.write(self.style.SUCCESS(message))
        except Exception as e:
            # Логируем ошибку, если что-то пошло не так
            error_message = f'Ошибка при очистке кеша: {e}'
            logger.error(error_message)
            self.stdout.write(self.style.ERROR(error_message))

#python manage.py clear_cache