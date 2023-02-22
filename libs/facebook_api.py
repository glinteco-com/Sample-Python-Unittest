import requests


class FacebookAPI:
    def get_userinfo(self, username):
        try:
            response = requests.get("https://facebook.com/")
            if response.status_code == 200:
                return response.json()
            return {}
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
        return {}
