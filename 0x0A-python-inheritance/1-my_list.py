#!/usr/bin/python3
""" My list Module. """


class MyList(list):
    """ Attributes: None """

    def print_sorted(self):
        """ Prints sorted list.
        Args:
            List from the BaseClass.
        Returns:
            None
        """
        try:
            if list(self):
                print(sorted(list(self)))
        except Exception as error:
            print("Traceback (most recent call last):")
            print("...")
            print("{}: {}".format(type(error).__name__, error))
