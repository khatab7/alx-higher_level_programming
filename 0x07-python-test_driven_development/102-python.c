#include "main.h"

/**
 * print_python_string - Prints information about a Python string object
 * @p: The PyObject pointer to the string object
 */
void print_python_string(PyObject *p)
{
    PyUnicodeObject *str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    str = (PyUnicodeObject *)p;

    if (PyUnicode_IS_COMPACT_ASCII(str))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %zd\n", PyUnicode_GET_LENGTH(str));
    printf("  value: %ls\n", PyUnicode_AsWideCharString(str, NULL));
}
