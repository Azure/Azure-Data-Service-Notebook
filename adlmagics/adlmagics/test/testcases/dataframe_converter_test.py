import unittest
from pandas import DataFrame

from adlmagics.converters.dataframe_converter import DataFrameConverter

class DataFrameConverterTest(unittest.TestCase):
    def test_convert_with_none(self):
        self.assertTrue(self.__converter.convert(None).equals(DataFrame()))

    def test_convert_with_a_list_of_models(self):
        class Model:
            def __init__(self, p1, p2):
                self.p1 = p1
                self.p2 = p2
            
        model_count = 10
        models = [Model(ix, str(ix)) for ix in range(model_count)]

        df = self.__converter.convert(models)

        expected_df = DataFrame({
            "p1" : [ix for ix in range(model_count)],
            "p2" : [str(ix) for ix in range(model_count)]})

        self.assertTrue(expected_df.equals(df))

    def test_convert_with_a_model(self):
        class Model:
            def __init__(self, p1, p2):
                self.p1 = p1
                self.p2 = p2
            
        model = Model(1, "1")

        df = self.__converter.convert(model)

        expected_df = DataFrame({
            "p1" : [1],
            "p2" : ["1"]})

        self.assertTrue(expected_df.equals(df))

    def test_convert_with_a_matrix(self):
        df = self.__converter.convert([[1, 2], [3, 4]])

        expected_df = DataFrame({
            0 : [1, 3],
            1 : [2, 4]})

        self.assertTrue(expected_df.equals(df))

    def test_convert_with_nonconvertible(self):
        self.assertRaises(ValueError, self.__converter.convert, 1)

    def setUp(self):
        self.__converter = DataFrameConverter()

    def tearDown(self):
        self.__converter = None