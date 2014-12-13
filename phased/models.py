from django.conf import settings
from hashlib import sha1

if not hasattr(settings, 'PHASED_SECRET_DELIMITER'):
    settings.PHASED_SECRET_DELIMITER = sha1(getattr(settings, 'SECRET_KEY', '')).hexdigest()

# quoting the sekrit delimiter to make sure Debug Toolbar doesn't render it
settings.PHASED_SECRET_DELIMITER = '"%s"' % settings.PHASED_SECRET_DELIMITER
