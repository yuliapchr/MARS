from flask import Blueprint, jsonify, make_response
from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).all()
    return jsonify({
        'jobs': [job.to_dict(
            only=('id', 'user.name', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished')) for
            job in jobs_list]
    })


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs_id(job_id):
    sess = db_session.create_session()
    jobs_id = sess.query(Jobs).filter(Jobs.id == job_id).first()
    if not jobs_id:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({
        'jobs_id': jobs_id.to_dict()
    })
