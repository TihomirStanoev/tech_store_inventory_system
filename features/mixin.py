class CapacityMixin:
    """
    A mixin class that provides standardized lists of valid storage and RAM capacities.
    This helps ensure consistency across different device classes.
    """
    STORAGE_CAPACITY = [2 ** gb for gb in range(6,12)] # [64, 128, 256, 512, 1024, 2048]
    RAM_CAPACITY = [2 ** gb for gb in range(2,8)] # [4, 8, 16, 32, 64, 128]

