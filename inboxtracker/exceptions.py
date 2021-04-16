class InboxTrackerException(Exception):
    pass


class InboxTrackerAPIException(InboxTrackerException):
    """Handle 4xx and 5xx errors from the API"""
    def __init__(self, response, *args, **kwargs):
        # noinspection PyBroadException
        try:
            errors = response.json()['errors']
            error_template = "{message} Code: {code} Description: {desc} \n"
            errors = [error_template.format(message=e.get('message', ''),
                                            code=e.get('code', 'none'),
                                            desc=e.get('description', 'none'))
                      for e in errors]
        # TODO: select exception to catch here
        except:  # noqa: E722
            errors = [response.text or ""]
        self.status = response.status_code
        self.response = response
        self.errors = errors
        message = """Call to {uri} returned {status_code}, errors:
        {errors}
        """.format(
            uri=response.url,
            status_code=response.status_code,
            errors='\n'.join(errors)
        )
        super(InboxTrackerAPIException, self).__init__(message, *args, **kwargs)
