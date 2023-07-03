import pickle
import json
import numpy as np
import config

class Medicale_insurences_util:

    # load user input
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def __load_self_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        # load data and pickel file 
        self.__load_self_data()
        
        gender = self.json_data['Gender'][self.gender]
        smoker = self.json_data['Smoker'][self.smoker]
        region = 'region_'+self.region

        region_index = self.json_data["Column Names"].index(region)
        region_index

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.age
        test_array[0,1] = gender
        test_array[0,2] = self.bmi
        test_array[0,3] = self.children
        test_array[0,4] = smoker
        test_array[0,region_index] = 1

        predicted_charges = np.around(self.model.predict(test_array)[0],3)
        return predicted_charges