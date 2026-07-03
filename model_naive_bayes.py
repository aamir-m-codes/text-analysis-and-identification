import read_data, preprocessing
from collections import defaultdict

def from_scratch(data):
    train_data_generated, train_data_written, test_data_generated, test_data_written = preprocessing.split_train_test(data)

    train_data_generated = preprocessing.lower_case(train_data_generated)
    train_data_written = preprocessing.lower_case(train_data_written)

    test_data_generated = preprocessing.lower_case(test_data_generated)
    test_data_written = preprocessing.lower_case(test_data_written)

    train_data_generated = preprocessing.split_features(train_data_generated)
    train_data_written = preprocessing.split_features(train_data_written)

    test_data_generated = preprocessing.split_features(test_data_generated)
    test_data_written = preprocessing.split_features(test_data_written)

    vocab = defaultdict(int)
    train_gen_bow = defaultdict(int)
    train_wri_bow = defaultdict(int)
    test_gen_bow = defaultdict(int)
    test_wri_bow = defaultdict(int)
    cond_gen_bow = defaultdict(int)
    cond_wri_bow = defaultdict(int)


    for doc in train_data_generated:
        for w in doc:
            vocab[w] +=1
            train_gen_bow[w] +=1

    for doc in train_data_written:
        for w in doc:
            vocab[w] +=1
            train_wri_bow[w] +=1

    


data = read_data.read_csv()
from_scratch(data)