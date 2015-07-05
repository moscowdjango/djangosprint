import os
import logging
from django.contrib.auth.models import User
from django.conf import settings


logger = logging.getLogger('django')
logger.setLevel(logging.INFO)


def create():
    user = User.objects.get(username = 'admin')
    if settings.DEBUG:
        password = "password"
    else:
        password = os.environ.get('ADMIN_PASSWORD')
        if not password:
            logger.info("ADMIN_PASSWORD not set in production")
            return
    if not user:
        logger.info("creating admin user")
        user = User.create_superuser('admin', 'admin@localhost', password)
        user.save()
    else:
        logger.info("admin user already exist, changing password")
        user.set_password(password)
        user.save()

