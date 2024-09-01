from setuptools import setup, Extension

ext = list()
ext.append(Extension(
    name='_image',
    sources=[
        './src/image/image.c',
    ],
))

setup(
    ext_modules=ext,
)