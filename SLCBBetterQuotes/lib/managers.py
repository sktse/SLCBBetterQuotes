import logging

logger = logging.getLogger()


class CommandManager:
    GET_QUOTE_COMMAND = "!quote"
    ADD_QUOTE_COMMAND = "!addquote"
    DELETE_QUOTE_COMMAND = "!delquote"
    LIST_QUOTES_COMMAND = "!listquote"
    QUOTE_COMMANDS = [
        GET_QUOTE_COMMAND,
        ADD_QUOTE_COMMAND,
        DELETE_QUOTE_COMMAND,
        LIST_QUOTES_COMMAND,
    ]

    def __init__(self, parent=None, client=None, script_settings=None):
        self.parent = parent
        self.client = client
        self.script_settings = script_settings

    def execute(self, data):
        first_param = data.GetParam(0)
        if first_param not in self.QUOTE_COMMANDS:
            # The first word is not a recognized quote command
            return

        query_string = self.get_parameter_as_string(data)
        if first_param == self.GET_QUOTE_COMMAND:
            if not self.has_permission(
                data.User,
                self.script_settings.GetQuotePermission,
                self.script_settings.GetQuoteInfo,
            ):
                # User does not have permission
                return

            return self.client.get_quote(
                query=query_string,
            )
        elif first_param == self.ADD_QUOTE_COMMAND:
            if not self.has_permission(
                data.User,
                self.script_settings.AddQuotePermission,
                self.script_settings.addQuoteInfo,
            ):
                # User does not have permission
                return

            return self.client.add_quote(
                query=query_string,
            )
        elif first_param == self.DELETE_QUOTE_COMMAND:
            if not self.has_permission(
                data.User,
                self.script_settings.DeleteQuotePermission,
                self.script_settings.DeleteQuoteInfo,
            ):
                # User does not have permission
                return

            return self.client.delete_quote(
                query=query_string,
            )
        else:
            if not self.has_permission(
                data.User,
                self.script_settings.ListQuotesPermission,
                self.script_settings.ListQuotesInfo,
            ):
                # User does not have permission
                return

            return self.client.list_quotes()

    def get_parameter_as_string(self, data):
        param_count = data.GetParamCount()
        parameters = []
        for i in range(1, param_count):
            param = data.GetParam(i)
            parameters.append(param)

        return " ".join(parameters)

    def has_permission(self, user, permission, info):
        return self.parent.HasPermission(
            user,
            permission,
            info)
