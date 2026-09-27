

class Node:
    def __init__(self,feature=None,threshold=None,left=None,right=None,*,value=None):
        self.feature
        self.threshold
        self.left
        self.right
        self.value=None

    def is_leaf_node(self):
        return self.value is not None
class DecisionTree:
    def __int__():