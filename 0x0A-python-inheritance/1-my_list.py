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
        if list(self) and isinstance(self, list):
            if all(isinstance(x, int) for x in self):
                print(sorted(list(self)))
