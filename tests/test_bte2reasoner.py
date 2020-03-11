import unittest
from biothings_explorer.user_query_dispatcher import FindConnection
from biothings_explorer.hint import Hint
import requests
import json

ht = Hint()
cxcr4 = ht.query('CXCR4')['Gene'][0]
fc = FindConnection(input_obj=cxcr4, output_obj='ChemicalSubstance', intermediate_nodes=None)
fc.connect(verbose=True)
response = fc.to_reasoner_std()

class TestSingleHopQuery(unittest.TestCase):

    def test_result_section(self):
        res = requests.post("http://transltr.io:7071/validate_result",
                            headers={"accept": "text/plain", "content-type": "application/json"},
                            data=json.dumps(response["results"])).json()
        self.assertEqual(res, "Successfully validated")

    def test_query_graph_section(self):
        res = requests.post("http://transltr.io:7071/validate_querygraph",
                            headers={"accept": "text/plain", "content-type": "application/json"},
                            data=json.dumps(response["query_graph"])).json()
        self.assertEqual(res, "Successfully validated")

    def test_knowledge_graph_section(self):
        res = requests.post("http://transltr.io:7071/validate_knowledgegraph",
                            headers={"accept": "text/plain", "content-type": "application/json"},
                            data=json.dumps(response["knowledge_graph"])).json()
        self.assertEqual(res, "Successfully validated")
