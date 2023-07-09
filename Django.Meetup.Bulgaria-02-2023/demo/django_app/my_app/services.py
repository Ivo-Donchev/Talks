import time
import logging


def function_call_decorator(logger):
    def inner(func):
        def result_function(*args, **kwargs):
            logger.debug(
                f'Function {func.__name__} called with args={args} and kwargs={kwargs}'
            )

            return func(*args, **kwargs)
        return result_function
    return inner


@function_call_decorator(logger=logging.getLogger(__name__))
def service_with_third_party_calls(*args, **kwargs):
    return
