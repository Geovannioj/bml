import pytest
import bml


def test_project_defines_author_and_version():
    assert hasattr(bml, '__author__')
    assert hasattr(bml, '__version__')
