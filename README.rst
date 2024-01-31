=======
Wizcoin
=======


.. image:: https://img.shields.io/pypi/v/wizcoin.svg
        :target: https://pypi.python.org/pypi/wizcoin

.. image:: https://img.shields.io/travis/adam-severi/wizcoin.svg
        :target: https://travis-ci.com/adam-severi/wizcoin

.. image:: https://readthedocs.org/projects/wizcoin/badge/?version=latest
        :target: https://wizcoin.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A Python module to represent the galleon, sickle and knut coin of wizard currency.


* Free software: MIT license
* Documentation: https://wizcoin.readthedocs.io.


Features
--------

Here's some xample code demonstrating how this module is used:
    >>> import wizcoin
    >>> coin = qizcoin.WizCoin(2, 5, 10)
    >>> str(coin)
    '2g, 5s, 10k'
    >>>coin.value()
    1141

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
