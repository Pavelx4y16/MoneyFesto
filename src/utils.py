def validate_init_arguments(cls):
    """This is class decorator.
    The main goal is to run validation function ("__validate_init_arguments"),
       which should be created in every class if we want to use this decorator.
    This decorator simplifies call to the validation method, increases readability and reduces code duplications
    Example of usage:

      @validate_init_arguments
      class Person:
        def __validate_init_arguments(self, name, age=25):
            assert isinstance(name, str)
            assert isinstance(age, int)

        def __init__(self, name, age=25):
            self.name = name
            self.age = age

    As we see from example: all you need, just to mark your class with '@validate_init_arguments'
       and implement corresponding validation function.

    Notes: 1) signatures of validation function and __init__ should be identical (including default parameters)
           2) decorated class can be safely inherited, because the identical method naming problem is resolved by
                usage of private ("__*") methods. That means, validation function will not be overriden by
                Child's validation function.
    """
    original_init = cls.__init__

    def decorated_init(self, *args, **kwargs):
        validate = getattr(self, f"_{cls.__name__}__validate_init_arguments")
        validate(*args, **kwargs)
        original_init(self, *args, **kwargs)

    cls.__init__ = decorated_init

    return cls
