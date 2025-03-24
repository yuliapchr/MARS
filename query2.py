from data.jobs import Jobs
from data import db_session
import datetime


db_session.global_init('database/mars_explorer.db')

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.start_date = datetime.datetime.now()
job.is_finished = False

session = db_session.create_session()
session.add(job)
session.commit()
