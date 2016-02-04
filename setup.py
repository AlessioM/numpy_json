from setuptools import setup

if __name__ == "__main__":
  setup(name="numpy_json",
    version='0.1',
    long_description=open("README.md").read(),
    py_modules=['numpy_json'],
    author="AlessioM",
    url='https://github.com/AlessioM/numpy_json',
    license='MIT',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: POSIX',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: MacOS :: MacOS X',
      'Topic :: Software Development :: Libraries',
      'Topic :: Utilities',
      'Programming Language :: Python :: 2'
    ],
    install_requires=["numpy", "json"],
    platforms=['unix', 'linux', 'osx', 'win32'],
  )