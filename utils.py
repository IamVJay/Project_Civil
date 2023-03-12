import numpy as np
import json
import pickle

class Concrete():
    def __init__(self,data):
        self.data = data
        print(self.data)

    def __loading(self): # private method      
        """
        Pickle & JSON file importing
        """

        with open('artifacts/project_data.json','r') as file:
            self.project_data = json.load(file)  
                                        
        with open("artifacts/model.pkl",'rb') as file:
            self.model = pickle.load(file)



    def get_Compressive_Strength_Predction(self):
        """
        Compressive Strength Predction
        """
        self.__loading()

        Cement =  self.data['html_Cement']
        Blast_Furnace_Slag =  self.data['html_Blast_Furnace_Slag']
        Fly_Ash =  self.data['html_Fly_Ash']
        Water =  self.data['html_Water']
        Superplasticizer =  self.data['html_Superplasticizer']
        Coarse_Aggregate =  self.data['html_Coarse_Aggregate']
        Fine_Aggregate =  self.data['html_Fine_Aggregate']
        Age =  self.data['html_Age']


        user_data = np.zeros(len(self.project_data['column_names']))
        user_data[0] = Cement
        user_data[1] = Blast_Furnace_Slag
        user_data[2] = Fly_Ash
        user_data[3] = Water
        user_data[4] = Superplasticizer
        user_data[5] = Coarse_Aggregate
        user_data[6] = Fine_Aggregate
        user_data[7] = Age

        return self.model.predict([user_data])[0]       