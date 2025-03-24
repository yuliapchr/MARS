from flask import Blueprint, jsonify
from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).all()
    return jsonify({
        'jobs': [job.to_dict(only=('id', 'user.name', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for job in jobs_list]
    })
