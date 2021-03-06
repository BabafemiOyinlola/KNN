import random
import numpy as np

class Preprocess:

    def read_csv(self, filepath, header=True):
        dataset = []
        read = open(filepath, "r")
        content = read.readlines()

        if(len(content) == 0):
                return
        else:
            if header == True:
                for line in range(1, len(content)):
                    dataset.append(content[line].rstrip().split(','))
            elif header == False:
                for line in range(len(content)):
                    row = content[line].rstrip().split(',')
                    if len(row) > 1:
                        dataset.append(row)
            read.close()
        return dataset

    #read breast cancer data - this is separate because ID is deleted from the data
    def read_breast_cancer_data(self, filepath, header=True):
        dataset = []
        read = open(filepath, "r")
        content = read.readlines()

        if(len(content) == 0):
                return
        else:
            if header == True:
                for line in range(1, len(content)):
                    row = content[line].rstrip().split(',')
                    dataset.append(row[1:len(row)])
            elif header == False:
                for line in range(len(content)):
                    row = content[line].rstrip().split(',')
                    if len(row) > 1:
                        dataset.append(row[1:len(row)])
            read.close()
        return dataset


    #Split into train and test set
    def split_data(self, data, label_pos, ratio=0.3):
        train, test = [], []

        test_num = int(ratio * len(data))
        for i in range(test_num):
            index = random.randint(0, (len(data)-1))
            item = data[index]
            test.append(item)
            del data[index]

        for i in range(len(data)):
            index = random.randint(0, (len(data)-1))
            item = data[index]
            train.append(item)
            del data[index]
        
        X_train, y_train, X_test, y_test =  self.seprate_feat_label(train, test, label_pos)

        return(X_train, y_train, X_test, y_test)

    #label_pos is the location of the label column. 0 for first column and -1 for last column
    def seprate_feat_label(self, train, test, label_pos):
        X_train, y_train, X_test, y_test = [], [], [], []

        if label_pos == -1:
            for i in range(len(train)):
                feat = train[i]
                feat = feat[0:len(train[0])-1]
                feat = [float(i) for i in feat]
                X_train.append(feat)
                y_train.append(train[i][-1])

            for i in range(len(test)):
                feat = test[i]
                feat = feat[0:len(test[0])-1]
                feat = [float(i) for i in feat]
                X_test.append(feat)
                y_test.append(test[i][-1])
        
        elif label_pos == 0:
            for i in range(len(train)):
                feat = train[i]
                feat = feat[1:len(train[0])]
                feat = [float(i) for i in feat]
                X_train.append(feat)
                y_train.append(train[i][0])

            for i in range(len(test)):
                feat = test[i]
                feat = feat[1:len(test[0])]
                feat = [float(i) for i in feat]
                X_test.append(feat)
                y_test.append(test[i][0])
            
        return (X_train, y_train, X_test, y_test)

    def normalise_data(self, data):
        temp = np.array(data, dtype=float)
        data_copy = temp.copy()

        rows = temp.shape[0]
        cols = temp.shape[1]
        for i in range(cols):
            col_max = np.amax(temp[:, i])
            col_min = np.amin(temp[:, i])
            for j in range(rows):
                if col_max == 0 and col_min == 0:
                    data_copy[j, i] = 0
                elif (col_max - col_min) == 0:
                    data_copy[j, i] = col_max
                else:                        
                    data_copy[j, i] = (temp[j, i] - col_min) / (col_max - col_min)

        return data_copy