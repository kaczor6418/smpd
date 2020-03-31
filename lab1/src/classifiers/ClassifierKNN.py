import math
from typing import List, Dict

from src.Leaf import Leaf
from src.Point import Point
from src.classifiers.ClassifierNN import ClassifierNN
from src.classifiers.typedDictionaries.NearestElement import NearestElement


class ClassifierKNN:

    @staticmethod
    def classify(train_group: List[Leaf], test_element: Point, trait_x_id: int, trait_y_id: int, k: int) -> int:
        nearest_element_id_distance: NearestElement = ClassifierNN.create_nearest_element(-1, math.inf)
        elements_id_distances: Dict[int, List[float]] = dict()
        for train_element in train_group:
            train_element_point: Point = train_element.create_point_from_traits(trait_x_id, trait_y_id)
            distance: float = test_element.calculate_distance_to_point(train_element_point)
            if elements_id_distances.get(train_element.leaf_name_id) is None:
                elements_id_distances[train_element.leaf_name_id] = [distance]
            else:
                elements_id_distances.get(train_element.leaf_name_id).append(distance)
        for nn_id, nn_distances in elements_id_distances.items():
            sum_of_distances_to_k_nn = sum(sorted(nn_distances, key=float)[:k])
            if sum_of_distances_to_k_nn < nearest_element_id_distance['distance']:
                nearest_element_id_distance = ClassifierNN.create_nearest_element(nn_id, sum_of_distances_to_k_nn)
        return nearest_element_id_distance['leaf_name_id']
