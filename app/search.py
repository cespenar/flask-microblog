from app import opensearch


def add_to_index(index, model):
    if not opensearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    opensearch.index(index=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not opensearch:
        return
    opensearch.delete(index=index, id=model.id)


def query_index(index, query, page, per_page):
    if not opensearch:
        return [], 0
    search = opensearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page}
    )
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']
