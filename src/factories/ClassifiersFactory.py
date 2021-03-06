from typing import List

from src.analyzer.types.ClassificationSchema import ClassificationSchema
from src.classifiers.AbstractClassifier import AbstractClassifier
from src.classifiers.ClassifierKNN import ClassifierKNN
from src.classifiers.ClassifierNM import ClassifierNM
from src.classifiers.ClassifierNN import ClassifierNN
from src.classifiers.types.ClassifeirsTypes import ClassifierType
from src.structures.DatasetElement import DatasetElement


class ClassifiersFactory:

    @staticmethod
    def get_classifier(classifier_config: ClassificationSchema, train_group: List[DatasetElement],
                       compared_traits: List[int], classes_ids: List[int]) -> AbstractClassifier:
        if classifier_config['type'] == ClassifierType.NN:
            return ClassifierNN(train_group, compared_traits, classifier_config['calculator'])
        if classifier_config['type'] == ClassifierType.KNN:
            return ClassifierKNN(train_group, compared_traits, classifier_config['calculator'], classifier_config['k'])
        if classifier_config['type'] == ClassifierType.NM:
            return ClassifierNM(train_group, compared_traits, classifier_config['calculator'], classes_ids)
