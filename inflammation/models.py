"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array."""
    return np.min(data, axis=0)


def daily_std(data):
    """Calculate the daily std of a 2D inflammation data array."""
    return np.std(data, axis=0)


def daily_above_threshold(patient_num, data, threshold):
    """Determine whether or not each daily inflammation value exceeds a given threshold for a given patient.

    :param patient_num: The patient row number
    :param data: A 2D data array with inflammation data
    :param threshold: An inflammation threshold to check each daily value against
    :returns: An integer representing the number of days a patient's inflammation is over a given threshold
    """
    def count_above_threshold(a, b):
        if b:
            return a + 1
        else:
            return a

   # Use map to determine if each daily inflammation value exceeds a given threshold for a patient
   above_threshold = map(lambda x: x > threshold, data[patient_num])
   # Use reduce to count on how many days inflammation was above the threshold for a patient
   return reduce(count_above_threshold, above_threshold, 0)