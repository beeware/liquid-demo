Liquid demo
===========

This is a demonstration app, showing Toga used to build a standalone
desktop application that is just a wrapper around a web page. It wraps
GitHub, but it's a one line source modification to make it wrap any
other webpage. It should be fairly obvious from the source code which
line needs to be modified.

Usage
-----

Briefcase can be used to wrap this as a standalone app under macOS::

    $ mkdir liquid
    $ virtualenv --python=$(which python3)
    $ pip install briefcase
    $ git checkout http://github.com/pybee/liquid-demo.git
    $ cd liquid-demo
    $ python setup.py macos

This will create a macOS directory that will contain "GitHub.app".
This app file can be placed in your Applications folder,

Modificatons
------------

Once you've got the basics working, you can make modifications. You could:

* Turn this project into a cookiecutter template

* Add menu items or a toolbar to access common URLs

* Add a custom icon

Why "Liquid"?
-------------

`Fluid`_ is an app used to wrap websites as macOS apps.

.. _Fluid: http://fluidapp.com

Community
---------

Liquid is part of the `BeeWare suite`_. You can talk to the community through:

* `@pybeeware on Twitter`_

* The `pybee/general`_ channel on Gitter.

We foster a welcoming and respectful community as described in our
`BeeWare Community Code of Conduct`_.

Contributing
------------

If you experience problems with Liquid, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: http://pybee.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _pybee/general: https://gitter.im/pybee/general
.. _BeeWare Community Code of Conduct: http://pybee.org/community/behavior/
.. _log them on Github: https://github.com/pybee/liquid-demo/issues
.. _fork the code: https://github.com/pybee/liquid-demo
.. _submit a pull request: https://github.com/pybee/liquid-demo/pulls
