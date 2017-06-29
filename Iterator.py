import visit as Vi

import PathCreator as Pa
import Inputs as In

# The next line can be commented to import and use in the VisIt GUI.
Vi.Launch()  # Here to allow import of other modules.

import MakeImagesPython as Mk

Image = Mk.MakeImages(In.Files)
Operators = In.Operators

Image.Plot()


def Iterator(OperatorSet=None, myList=None):
    """Iterate through several operator options."""

    Pa.PathCreator()  # Creates necessary folders.

    for item in Operators:
        if OperatorSet is not None:

            Vi.RemoveAllOperators()

            # Apply single dictionary operator.
            try:
                Operator = (item.keys())[0]
                myList = (item.values())[0]
                Image.Operator(Operator, myList)
            except Exception:
                pass

            # Apply single list operator.
            try:
                Operator = item[0]
                myList = item[1]
                Image.Operator(Operator, myList)
            except Exception:
                pass

            # Multiple Operators.
            try:
                for multiitem in item:

                    # Apply dictionary operator.
                    try:
                        Operator = (multiitem.keys())[0]
                        myList = (multiitem.values())[0]
                        Image.Operator(Operator, myList)
                    except Exception:
                        pass

                    # Apply list operator.
                    try:
                        Operator = multiitem[0]
                        myList = multiitem[1]
                        Image.Operator(Operator, myList)
                    except Exception:
                        pass

            except Exception:
                pass

        Image.Save()
