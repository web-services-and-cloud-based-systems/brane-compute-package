from turtle import done

from unittest.mock import patch, mock_open
import pytest
import pandas as pd

import compute


def test_get_df():
    # checks if the internal function get_df can read and return a dataframe or not
    test_input_path = './sample.csv'
    assert type(compute.get_df(test_input_path)) == pd.DataFrame


def test_mount():
    done

def test_get_shape():
    # checks if the function data_shape can read and returns correct shape of dataframe or not
    test_input_path = './sample.csv'
    assert compute.data_shape(test_input_path) == 'Shape is:(10, 12)'

def test_get_model_accuracy():
    # checks if the function get_model_accuracy returns accuracy is less than 0 for given model
    test_input_path = './prep_data1.csv'
    result = float(compute.get_model_accuracy(test_input_path, 'dtc'))
    value_assert = result < 1
    assert value_assert

def test_modelling():
    # checks if modelling functions works for preprocessed data dataset and model
    # ie. after training model and prediction 
    test_input_path = './prep_data0.csv'
    train_data_input_path = './prep_data1.csv'
    # third parameter takes model alias here rfc stands for RandomForestClassifier
    result = compute.modelling(train_data_input_path, test_input_path, 'rfc')

    

def test_preprocessing():
    # checks if preprocessing function works correctly
    # after completing all the steps of preprocessing, 
    train_data_input_path = './train.csv'
    # second parameter is isTrain i.e. whether data provided is training dataset
    result = compute.preprocessing(train_data_input_path, 1)
   