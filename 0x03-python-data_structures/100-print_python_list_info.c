#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to objects in a python list
 * Return: Nothing
*/

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyListObject *list;
	/* Have to define a new variable to use it after casting PyObject *p */
	/* *p must be forcely casted like that to PyListObject, or it won't work */
	/* Using PyListObject to be able to access its struct members/elements */
	list = (PyListObject *)p;

	/* PyList_Check: Checks if there's a list or not | if it's not empty ?! */
	/* 1- PyList_Size: gets what actually is in the list at the moment */
	/* 2- list->allocated: gets what been alloacted since the beginning */
	/* 1 & 2 are Py_ssize_t which is ssize_t originally >> long signed int */

	/**
	 * list->ob_item[i]->ob_type->tp_name:
	 * ob_item: double ptr + ob_type: ptr + tp_name: ptr && list: ptr
	*/

	if PyList_Check(p)
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", list->allocated);
		for (; i < PyList_Size(p); i++)
		{
			printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		}
	}
}
