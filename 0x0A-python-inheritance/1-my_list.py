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
        print(sorted(list(self)))
