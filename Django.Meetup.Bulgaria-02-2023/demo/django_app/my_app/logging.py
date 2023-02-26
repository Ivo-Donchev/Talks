from decimal import Decimal

from django.utils.log import ServerFormatter
from django.db import connection


class CustomWebServerFormatter(ServerFormatter):
    def format(self, record):
        queries = connection.queries

        create_queries = [query for query in queries if 'INSERT ' in query['sql']]
        select_queries = [query for query in queries if 'SELECT ' in query['sql']]
        update_queries = [query for query in queries if 'UPDATE ' in query['sql']]
        delete_queries = [query for query in queries if 'DELETE ' in query['sql']]

        is_transaction = any([
            query
            for query in queries
            if (
                'BEGIN' in query['sql'] or
                'COMMIT' in query['sql']
            )
        ])

        record.create_queries_count = len(create_queries)
        record.create_queries_time = sum([Decimal(q['time']) for q in create_queries])

        record.select_queries_count = len(select_queries)
        record.select_queries_time = sum([Decimal(q['time']) for q in select_queries])

        record.update_queries_count = len(update_queries)
        record.update_queries_time = sum([Decimal(q['time']) for q in update_queries])

        record.delete_queries_count = len(delete_queries)
        record.delete_queries_time = sum([Decimal(q['time']) for q in delete_queries])

        record.is_transaction = is_transaction

        return super().format(record)
