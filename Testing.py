import unittest
from PAM import PAM
from Data import Data
import pandas as pd
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_determine_closest_in_dictionary(self):
        """
        Test for PAM function
        """
        test_dict = {  # arbitrary set dictionary to test
            "1": 55, "2": 22, "3": 11, "4": 1
        }
        result_list = PAM.order_by_dict_values(test_dict)  # returns list of tuples (not dictionary)
        result = result_list[0][1]  # obtain first value dictionary is ordered by
        self.assertEqual(result, 1, "minimum value")  # determines if it is smallest element
        self.assertNotEqual(result, 55, "Not Max Val")

    def test_PAM_super(self):
        """
        Test if inheritance is working properly
        test if euclidean is working properly for both single and dictionary returns
        """
        data = Data('abalone', pd.read_csv(r'data/abalone.data', header=None), 8)  # load data
        df = data.df.sample(n=10)  # minimal data frame
        data.split_data(data_frame=df)  # sets test and train data
        pam = PAM(k_val=2, data_instance=data)  # create PAM instance to check super
        pam_train_data = pam.train_df  # train_df is an instance from parent class
        self.assertTrue(pam_train_data.equals(data.train_df), "Same data")
        self.assertFalse(pam_train_data.equals(data.test_df))

        row_c, row_q = np.split(pam_train_data, 2)  # split the same data into size of
        _, row_comp = next(row_c.copy().iterrows())  # get a row
        _, row_query = next(row_q.copy().iterrows())  # get a row
        dict_dist = pam.get_euclidean_distance_dict(row_query, row_c)

        single_distance = pam.get_euclidean_distance(row_query, row_comp)  # get distance
        self.assertTrue(isinstance(single_distance, float))  # check the it returns a float
        self.assertTrue(isinstance(dict_dist, dict))  # check if it is a dictionary


if __name__ == '__main__':
    unittest.main()