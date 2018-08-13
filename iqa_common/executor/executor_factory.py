from iqa_common.executor import ExecutorLocal, ExecutorSsh, ExecutorContainer, ExecutorAnsible, Executor


class ExecutorFactory(object):
    @staticmethod
    def create_executor(impl: str, **kwargs) -> Executor:
        if impl == ExecutorLocal.implementation:
            return ExecutorLocal()
        elif impl == ExecutorSsh.implementation:
            return ExecutorSsh(**kwargs)
        elif impl == ExecutorContainer.implementation:
            return ExecutorContainer(**kwargs)
        elif impl == ExecutorAnsible.implementation:
            return ExecutorAnsible(**kwargs)
        else:
            raise ValueError('Invalid executor implementation')
