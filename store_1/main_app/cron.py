from django_cron import CronJobBase, Schedule
from django.core.cache import cache

class ClearCacheCronJob(CronJobBase):
    RUN_EVERY_MINS = 10  # Раз в неделю (10080 минут)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.clear_cache_cron_job'

    def do(self):
        cache.clear()
        print("Кеш успешно очищен!")

# Не работает.