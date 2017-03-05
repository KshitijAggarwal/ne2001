""" Tests on utils module
"""

import numpy as np
import pytest

from ne2001 import utils

from astropy.coordinates import Angle
from astropy import units as u
from astropy.units.core import UnitConversionError


def test_parse_lbd():
    """ Parse lbd """
    # Simple floats
    in_l,in_b,in_d = 1., 1., 50.
    l,b,d = utils.parse_lbd(in_l, in_b, in_d)
    # Test
    for xx in [l,b,d]:
        assert isinstance(xx,float)
    # Angles
    in_l,in_b,in_d = Angle(1.*u.deg), Angle(1.*u.deg), 50.
    l,b,d = utils.parse_lbd(in_l, in_b, in_d)
    assert np.isclose(in_l.value, l)
    # Distance
    in_l,in_b,in_d = Angle(1.*u.deg), Angle(1.*u.deg), 50.*u.kpc
    l,b,d = utils.parse_lbd(in_l, in_b, in_d)
    assert np.isclose(in_d.value, d)
    # Again
    in_l,in_b,in_d = Angle(1.*u.deg), Angle(1.*u.deg), 500.*u.pc
    l,b,d = utils.parse_lbd(in_l, in_b, in_d)
    assert np.isclose(d, 0.5)
    # Bad input
    in_l,in_b,in_d = Angle(1.*u.deg), Angle(1.*u.deg), 500.*u.s
    with pytest.raises(UnitConversionError):
        l,b,d = utils.parse_lbd(in_l, in_b, in_d)
    in_l,in_b,in_d = Angle(1.*u.deg), Angle(1.*u.deg), [500]
    with pytest.raises(IOError):
        l,b,d = utils.parse_lbd(in_l, in_b, in_d)



def test_parse_DM():
    """ Parse lbd """
    # Simple floats
    in_DM = 20.
    DM = utils.parse_DM(in_DM)
    assert isinstance(DM, float)
    # Quantity
    in_DM = 20. * u.pc / u.cm**3
    DM = utils.parse_DM(in_DM)
    assert np.isclose(DM, in_DM.value)