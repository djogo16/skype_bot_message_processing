from hivebatch import load_hive_data
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(load_hive_data, 'interval', hours=1)
scheduler.start()

