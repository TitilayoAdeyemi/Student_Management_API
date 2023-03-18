from flask import Flask
from .students.views import student_namespace
from .user_auth.views import auth_namespace
from .courses.view import course_namespace
from flask_restx import Api
from .config.config import config_dict
from .utils import db
from .models.students import Student
from .models.courses import Courses
from .models.grades import Grades
from .models.lecturers import Lecturer
from .models.students_courses import StudentCourse
from .models.users import User, UserRole
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app(config = config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    

    api = Api(app)

    migrate = Migrate(app, db)

    jwt = JWTManager(app)


    api.add_namespace(student_namespace)
    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(course_namespace)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db' : db,
            'User' : User,
            'Student' : Student,
            'StudentCourse' : StudentCourse,
            'Courses' : Courses,
            'Grades' : Grades,
            'Lecturer' : Lecturer,
            'UserRole' :UserRole
        }

    return app