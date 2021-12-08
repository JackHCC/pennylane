# Copyright 2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility functions for circuit cutting"""
import networkx as nx
import itertools

def draw(g: nx.Graph):
    pos = nx.nx_agraph.graphviz_layout(g, prog="dot")

    for p1, p2 in itertools.combinations(pos.keys(), r=2):
        if pos[p1] == pos[p2]:
            pos[p1] = (pos[p1][0], pos[p1][0] - 1)

    label_dict = {o: o.name for o in g.nodes}
    nx.draw(g, with_labels=True, labels=label_dict, pos=pos)
