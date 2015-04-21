from distutils.core import setup
setup(name = 'OLPython',
      version = '0.1',
      url = 'http://audun-.github.io/olp',
      author = 'Audun B. Mo, @_audun_',
      author_email = "audun@kinesthesiac.com",
      description = "One-liner python! Write , execute and store python scripts from the CLI",
      py_modules = ['OLPExtensions', 'OLPExceptions', 'OLPModules', 'OLPManager'],
      scripts = ['olp']
      )
