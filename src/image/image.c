#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef enum {
    png, jpg, jpeg,
} EXT;

typedef struct {
    PyObject_HEAD
    EXT ext;
    int width;
    int heigth;
    int **bmp;
    int bmp_color_count;
} ImageObject;

static PyMethodDef MyMethdos[] = {
};

static struct PyModuleDef image_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "_image",
    .m_doc = "Module for image processing in pure c",
    .m_methods = MyMethdos,
    .m_size = -1,
};

PyMODINIT_FUNC PyInit_image(void) { 
    return PyModule_Create(&image_module);
}
