"""Tests for the Patient model."""

from inflammation.models import Patient
import numpy.testing as npt

def test_create_patient():

    name = 'Alice'
    w = 50
    h = 1.8
    p = Patient(name=name, weight=w, height=h)

    assert p.name == name
    assert p.weight == w
    assert p.height == h

def test_patient_compute_bmi():

    name = 'maria'
    weight = 60
    heigth = 1.6

    maria = Patient(name=name, weight=weight, height=heigth)
    expected_bmi = 23.4375
    bmi = maria.get_body_mass_index()

    npt.assert_almost_equal(bmi, expected_bmi)



