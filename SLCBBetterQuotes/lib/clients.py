import urllib


class QuotesClient:

    GET_QUOTE_URL = "https://twitch.center/customapi/quote?token={key}&data={query}"
    ADD_QUOTE_URL = "https://twitch.center/customapi/addquote?token={key}&data={query}"
    DELETE_QUOTE_URL = "https://twitch.center/customapi/delquote?token={key}&data={query}"
    LIST_QUOTE_URL = "https://twitch.center/customapi/quote/list?token={key}"

    def __init__(self, parent, read_only_key, admin_key):
        self.parent = parent
        self.read_only_key = read_only_key
        self.admin_key = admin_key

    def get_quote(self, query=""):
        encoded_query = urllib.quote(query.encode('utf8'))
        url = self.GET_QUOTE_URL.format(key=self.read_only_key, query=encoded_query)
        result = self.parent.GetRequest(url, {})
        return result

    def add_quote(self, query):
        encoded_query = urllib.quote(query.encode('utf8'))
        url = self.ADD_QUOTE_URL.format(key=self.admin_key, query=encoded_query)
        result = self.parent.GetRequest(url, {})
        return result

    def delete_quote(self, query):
        encoded_query = urllib.quote(query.encode('utf8'))
        url = self.DELETE_QUOTE_URL.format(key=self.admin_key, query=encoded_query)
        result = self.parent.GetRequest(url, {})
        return result

    def list_quotes(self):
        url = self.LIST_QUOTE_URL.format(key=self.read_only_key)
        result = self.parent.GetRequest(url, {})
        return result
