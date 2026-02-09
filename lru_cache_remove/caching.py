"""
    Copied from https://github.com/python/cpython/blob/3.13/Lib/functools.py#L551
    With function `remove` added, and culled support for maxsize to be null
"""
import time
from functools import _make_key, update_wrapper, lru_cache, wraps
from threading import RLock
from collections import namedtuple
from typing import Dict, List, TypeVar, Callable, Any, cast

_CacheInfo = namedtuple("_CacheInfo", ["hits", "misses", "maxsize", "currsize"])


def lru_cache_custom(maxsize=128):
    """Least-recently-used cache decorator.

    Arguments to the cached function must be hashable.

    View the cache statistics named tuple (hits, misses, maxsize, currsize)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().
    Access the underlying function with f.__wrapped__.

    """
    if maxsize < 0:
        maxsize = 0

    def decorating_function(user_function):
        wrapper = _lru_cache_wrapper_custom(user_function, maxsize, _CacheInfo)
        wrapper.cache_parameters = lambda: {'maxsize': maxsize, 'typed': False}
        return update_wrapper(wrapper, user_function)

    return decorating_function


def _lru_cache_wrapper_custom(user_function, maxsize, _CacheInfo):
    assert maxsize > 0
    # Constants shared by all lru cache instances:
    sentinel = object()  # noqa: F841  # unique object used to signal cache misses
    make_key = _make_key  # build a key from the function arguments
    PREV, NEXT, KEY, RESULT = 0, 1, 2, 3  # names for the link fields

    cache: Dict = {}
    hits = misses = 0
    full = False
    cache_get = cache.get  # bound method to lookup a key or return None
    cache_len = cache.__len__  # get cache size without calling len()
    lock = RLock()  # because linkedlist updates aren't threadsafe
    root: List = []  # root of the circular doubly linked list
    root[:] = [root, root, None, None]  # initialize by pointing to self

    def wrapper(*args, **kwds):
        # Size limited caching that tracks accesses by recency
        nonlocal root, hits, misses, full
        key = make_key(args, kwds, False)
        with lock:
            link = cache_get(key)
            if link is not None:
                # Move the link to the front of the circular queue
                link_prev, link_next, _key, result = link
                link_prev[NEXT] = link_next
                link_next[PREV] = link_prev
                last = root[PREV]
                last[NEXT] = root[PREV] = link
                link[PREV] = last
                link[NEXT] = root
                hits += 1
                return result
            misses += 1

        result = user_function(*args, **kwds)
        with lock:
            if key in cache:
                pass
            elif full:
                oldroot = root
                oldroot[KEY] = key
                oldroot[RESULT] = result
                root = oldroot[NEXT]
                oldkey = root[KEY]
                oldresult = root[RESULT]  # noqa: F841
                root[KEY] = root[RESULT] = None
                del cache[oldkey]
                cache[key] = oldroot
            else:
                last = root[PREV]
                link = [last, root, key, result]
                last[NEXT] = root[PREV] = cache[key] = link
                full = (cache_len() >= maxsize)

        return result

    def cache_info():
        with lock:
            return _CacheInfo(hits, misses, maxsize, cache_len())

    def cache_clear():
        nonlocal hits, misses, full
        with lock:
            cache.clear()
            root[:] = [root, root, None, None]
            hits = misses = 0
            full = False

    def remove(*args, **kwds) -> bool:
        nonlocal full
        key = make_key(args, kwds, False)
        with lock:
            link = cache_get(key)
            if link is None:
                return False
            link_prev, link_next, _key, result = link
            link_prev[NEXT] = link_next
            link_next[PREV] = link_prev
            del cache[key]
            full = False
        return True

    wrapper.cache_info = cache_info  # type: ignore
    wrapper.cache_clear = cache_clear  # type: ignore
    wrapper.remove = remove  # type: ignore
    return wrapper


T = TypeVar('T', bound=Callable[..., Any])


def ttl_cache(maxsize: int = 1, seconds: float = 10) -> Callable[[T], T]:
    """
    Decorator that caches the result of a function with a time-to-live (TTL).
    The cache is invalidated after the specified number of seconds.

    [maxsize] should only be used when the decorated method takes arguments.

    Usage:
        @ttl_cache(maxsize=2, seconds=30.1)
        def my_function(arg1, arg2):
            ...
    """
    def decorator(func: T) -> T:
        @lru_cache(maxsize=maxsize)
        def cached_func(ttl_hash: float, *args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            ttl_hash = round(time.time() / seconds)
            return cached_func(ttl_hash, *args, **kwargs)

        # Clean up the wrapper's attributes to look like the original function
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        wrapper.__annotations__ = func.__annotations__

        return cast(T, wrapper)

    return decorator
