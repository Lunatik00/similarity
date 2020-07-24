# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nmslib
import tensorflow as tf
from tensorflow_similarity.indexer.utils import (load_packaged_dataset)

class Indexer(object):
    """ Indexer class that indexes Embeddings. This allows for efficient
        searching of approximate nearest neighbors for a given embedding
        in metric space.

        Args:
            model_path (string): The path to the model that should be used to calculate embeddings
            dataset_examples_path (string): The path to the json lines file containing the dataset
            dataset_labels_path (string): The path to the json lines file containing the labels for the dataset
            index_dir (string): The path to the directory where the indexer should be saved,
            space (string): The space (a space is a combination of data and the distance) to use in the indexer
                            for a list of available spaces see: https://github.com/nmslib/nmslib/blob/master/manual/spaces.md
    """

    def __init__(self, dataset_examples_path, dataset_labels_path, model_path, index_dir, space="cosinesimil"):
        self.model = tf.keras.models.load_model(model_path, custom_objects={'tf': tf})
        self.dataset_examples, self.dataset_labels = load_packaged_dataset(dataset_examples_path, dataset_labels_path, self.model.layers[0].name)
        self.index_dir = index_dir
        self.index = nmslib.init(method='hnsw', space=space)
        self.thresholds = dict()

    def build(self, verbose=0):
        """ build an index from a dataset 

            Args:
                verbose (int): Verbosity mode (0 = silent, 1 = progress bar)
        """
        embeddings = self.model.predict(self.dataset_examples)
        self.index.addDataPointBatch(embeddings)
        print_progess = verbose > 0
        self.index.createIndex(print_progress=print_progess)

    def find(item, num_neighbors):
        """ find the closest data points and their associated data in the index

            Args:
                item (Item): The item for a which a query of the most similar items should be performed
                num_neighbors (int): The number of neighbors that should be returned

            Returns:
                neighbors (list(Item)): A list of the nearest neighbor items
        """
        # TODO
        pass

    def save():
        """ Store an indexer on the disk
        """
        # TODO
        pass

    def load(path):
        """ Load an indexer from the disk

            Args:
                The path to the file that the indexer is be loaded from
        """
        # TODO
        pass
    
    def add(item):
        """ Add an item to the index
        
            Args:
                item (Item): The item to be added to the index
        """
        # TODO
        pass

    def remove(item):
        """ Remove an item from the index
            Args:
                item (Item): The item to removed added to the index
        """
        # TODO
        pass

    def rebuild():
        """ Rebuild the index after updates were made
        """
        # TODO
        pass

    def compute_thresholds():
        """ Compute thresholds for similarity using V measure score
        """
        # TODO
        pass