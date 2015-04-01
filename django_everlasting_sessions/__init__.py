import time

from django.conf import settings

SESSION_COOKIE_REFRESH = getattr(settings, 'SESSION_COOKIE_REFRESH', 86400)  # 1 day

SESSION_LAST_UPDATE_TIME_KEY = '_session_last_update_time'


class SessionUpdateMiddleware(object):
	def process_response(self, request, response):
		if response.status_code != 500 and request.session.accessed and not request.session.get_expire_at_browser_close():
			last_update_time = request.session.get(SESSION_LAST_UPDATE_TIME_KEY)
			now = int(time.time())
			if request.session.modified or not last_update_time or now - last_update_time >= SESSION_COOKIE_REFRESH:
				request.session[SESSION_LAST_UPDATE_TIME_KEY] = now
		return response
