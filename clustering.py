from flask import jsonify
from sklearn import datasets, svm


def load_data():

    # Load Dataset from scikit-learn.
    digits = datasets.load_digits()

    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])

    return jsonify({'prediction': repr(prediction)})
