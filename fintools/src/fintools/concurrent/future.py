import uuid
import time
from threading import Thread
from typing import Generic, TypeVar, Callable

from fintools.utils import compose


A = TypeVar('A')
B = TypeVar('B')

results_registry = {}


class FutureValueStatus:
    PENDING = "pending"
    DONE = "done"

    def __init__(self, value, status):
        self.value = value
        self.status = status

    def __repr__(self):
        return f"FutureValueStatus({self.value}, {self.status})"

    @classmethod
    def pending(cls):
        return FutureValueStatus(value=None, status=cls.PENDING)

    def done(self, value):
        self.value = value
        self.status = self.DONE


def worker_wrapper(worker: Callable, key: str, *args, **kwargs) -> Callable:
    def wrapper():
        global results_registry
        results_registry[key].done(value=worker(*args, **kwargs))
    return wrapper


class Future(Generic[A]):

    def __init__(self, worker: Callable[..., A], *args, **kwargs):
        self.worker = worker
        self.key = str(uuid.uuid4())
        self.wrapper = worker_wrapper(worker, self.key, *args, **kwargs)
        self.thread = Thread(target=self.wrapper)
        self._result = None
        results_registry[self.key] = FutureValueStatus.pending()
        self.thread.start()

    def __str__(self):
        self.cleanup()
        if self._result is None:
            return f"Future({self.key})"
        return f"Future({self._result})"

    def __repr__(self):
        return str(self)

    def is_resolved(self):
        return self.key not in results_registry or results_registry[self.key].status == "done"

    def cleanup(self):
        if self.key in results_registry and results_registry[self.key].status == "done":
            self._result = results_registry.pop(self.key).value

    def wait(self, cleanup: bool = False) -> A:
        if self.key not in results_registry:
            return self._result
        if results_registry[self.key].status == "pending":
            self.thread.join()
        self._result = results_registry[self.key].value
        if cleanup:
            self.cleanup()
        return self._result

    def flat_map(self, f: Callable[[A], 'Future[B]']) -> 'Future[B]':
        return Future(worker=lambda: f(self.wait(cleanup=True)).wait(cleanup=True))

    @staticmethod
    def pure(x: A) -> 'Future[A]':
        return Future(worker=lambda: x)

    def map(self, f: Callable[[A], B]) -> 'Future[B]':
        function = compose(this=f, and_then=self.pure)
        return self.flat_map(function)
