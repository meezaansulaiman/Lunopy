
def build_query_string(query_obj):
    query_string = '?'

    if query_obj is not None or len(query_obj.keys()) == 0:
        query_list = list(map(lambda x: '{0}={1}'.format(x, query_obj[x]), query_obj.keys()))

        return query_string + '&'.join(query_list)
    else:
        return ''


def build_api_call(base_url, account_id, method, query_string):
    if account_id is None:
        return '{0}/{1}{2}'.format(base_url, method, query_string)
    else:
        return '{0}/accounts/{1}/{2}{3}'.format(base_url, account_id, method, query_string)