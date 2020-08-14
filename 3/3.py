#!/usr/bin/env python3

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def as_dict(self):
        ''' Returns the tree beginning at this node as a dict '''
        dict = {"val": self.val, "left": None, "right": None} # initialize dict
        if self.left: dict["left"] = self.left.as_dict()      # recurse left
        if self.right: dict["right"] = self.right.as_dict()   # recurse right
        return dict


def serialize(node):
    ''' Serialize a full tree as JSON '''
    return json.dumps(node.as_dict())

def deserialize(s):
    ''' Deserialize a full tree from JSON or dictionary to a Node tree '''

    if isinstance(s, str): s = json.loads(s) # in root case, parse JSON string to dict

    node = Node(s['val']) # instantiate the Node for this layer

    if s['left']: node.left = deserialize(s['left']) # if a left branch exists, recurse down it
    if s['right']: node.right = deserialize(s['right']) # if a right branch exists, recurse down it
    return node


def test_serialize_deserialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    #         root
    #         /  \
    #     left   right
    #    / 
    #  left.left

    assert deserialize(serialize(node)).left.left.val == 'left.left'