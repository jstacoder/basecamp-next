import json
import requests
from oauth2 import OAuth2


class BasecampError(Exception):
    pass


class Client(object):

    LAUNCHPAD_URL = 'https://launchpad.37signals.com'
    BASE_URL = 'https://basecamp.com/%s/api/v1'

    def __init__(self, access_token, user_agent, account_id=None):
        """Initialize client for making requests.

        user_agent -- string identifying the app, and an url or email related
        to the app; e.g. "BusyFlow (http://busyflow.com)".
        """
        self.account_id = account_id
        self.session = requests.session(
                headers={'User-Agent': user_agent,
                         'Authorization': 'Bearer %s' % access_token,
                         'Content-Type': 'application/json; charset=utf-8'})

    def qualified_url(self, url):
        assert self.account_id is not None, "No account id given!"
        return '%s/%s.json' % (self.BASE_URL % self.account_id, url)

    def accounts(self):
        url = '%s/authorization.json' % self.LAUNCHPAD_URL
        return self.session.get(url).content


class Endpoint(object):

    def __init__(self, client):
        self.client = client

    def _get(self, url):
        resp = self.client.session.get(self.client.qualified_url(url))
        if resp.status_code != 200:
            raise BasecampError(resp.status_code)
        return json.loads(resp.content)

    def _post(self, url, data={}, expect=201):
        resp = self.client.session.post(self.client.qualified_url(url),
                json.dumps(data))
        if resp.status_code != expect:
            raise BasecampError(resp.status_code)
        if resp.content:
            return json.loads(resp.content)

    def _put(self, url, data={}):
        resp = self.client.session.put(self.client.qualified_url(url),
                json.dumps(data))
        if resp.status_code != 200:
            raise BasecampError(resp.status_code)
        return json.loads(resp.content)

    def _delete(self, url):
        resp = self.client.session.delete(self.client.qualified_url(url))
        if resp.status_code != 204:
            raise BasecampError(resp.status_code)


class Projects(Endpoint):

    BASE_URL = 'projects'

    def list(self, archived=False):
        if archived:
            return self._get('%s/archived' % self.BASE_URL)
        return self._get(self.BASE_URL)

    def get(self, project_id):
        return self._get('%s/%s' % (self.BASE_URL, project_id))

    def post(self, name, description=None):
        return self._post(self.BASE_URL,
                {'name': name,
                 'description': description})

    def update(self, project_id, name, description=None):
        return self._put('%s/%s' % (self.BASE_URL, project_id),
                {'name': name,
                 'description': description})

    def archive(self, project_id, archived=True):
        return self._put('%s/%s' % (self.BASE_URL, project_id),
                {'archived': archived})

    def activate(self, project_id):
        return self.archive(project_id, False)

    def delete(self, project_id):
        return self._delete('%s/%s' % (self.BASE_URL, project_id))

    def accesses(self, project_id):
        return self._get('%s/%s/accesses' % (self.BASE_URL, project_id))

    def grant_access(self, project_id, ids=[], emails=[]):
        if not ids and not emails:
            return
        return self._post('%s/%s/accesses' % (self.BASE_URL, project_id),
                {'ids': ids, 'email_addresses': emails}, expect=204)

    def revoke_access(self, project_id, person_id):
        return self._delete('%s/%s/accesses/%s' %
                (self.BASE_URL, project_id, person_id))


class People(Endpoint):

    BASE_URL = 'people'

    def list(self):
        return self._get(self.BASE_URL)

    def get(self, person_id=None):
        if not person_id:
            return self._get('%s/me' % self.BASE_URL)
        return self._get('%s/%s' % (self.BASE_URL, person_id))

    def delete(self, person_id):
        return self._delete('%s/%s' % (self.BASE_URL, person_id))



class Auth(object):

    AUTH_URL_BASE = 'https://launchpad.37signals.com/authorization/'
    AUTH_URL_NEW = 'new'
    AUTH_URL_TOKEN = 'token'

    def __init__(self, client_id, client_secret, redirect_url):
        self.oauth2 = OAuth2(client_id,
                client_secret,
                self.AUTH_URL_BASE,
                redirect_url,
                self.AUTH_URL_NEW,
                self.AUTH_URL_TOKEN)

    def authorize_url(self):
        """Return an authorization url that opens a dialog for a user.
        """
        return self.oauth2.authorize_url(type='web_server')

    def access_token(self, code):
        """Return a dictionary with access token, expiration time, and
        refresh token.
        """
        response = self.oauth2.get_token(code, type='web_server')
        return response
