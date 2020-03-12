class SmartAPIParser():
    """Parse SmartAPI specifications
    """"

    def load_spec(self, spec=None):
        self.spec = spec
        self.info = {"endpoints": []}

    def fetch_api_name(self):
        """fetch the name of the API
        """
        return self.spec['info']['title']

    def fetch_server_url(self):
        """fetch the server url of the API
        """
        return self.spec['servers'][0]['url']

    def fetch_api_tags(self):
        """fetch the api tags info of the API
        """
        if "tags" in self.spec:
            return [_item['name'] for _item in self.spec['tags']]
        else:
            return []

    def fetch_semantic_mapping_path(self, endpoint_spec):
        """fetch the path of semantic mapping json doc
        """
        return endpoint_spec["x-bte-semanticmapping"]["$ref"]
    
    def fetch_semantic_mapping(self, ref):
        """fetch the semantic mapping json file based on the path in $ref
        """
        path = ref.split('/')
        assert path[1] == "components"
        assert path[2] == "x-bte-semanticmapping"
        return self.spec["components"]["x-bte-semanticmapping"][path[-1]]
    
    def fetch_param(self, endpoint_spec):
        """fetch the parameter name of the endpoint
        
        params
        ======
        endpoint_spec: the smartAPI spec related to the endpoint
        """
        if 'parameters' in endpoint_spec:
            return endpoint_spec['parameters'][0].get('name')
        else:
            return None

    def fetch_endpoint_info(self):
        endpoint_summary = []
        for path, path_info in self.spec["path"].items():
            for method, method_info in path_info.items():
                if "x-bte-semanticmapping" in method_info:
                    method_summary = {'method': method,
                                      'path': path,
                                      'api_type': self.fetch_api_tags(),
                                      'api_name': self.fetch_api_name(),
                                      'param': self.fetch_param(method_info)}
                    mapping_path = self.fetch_semantic_mapping_path(method_info)
                    method_summary['mapping'] = self.fetch_semantic_mapping(mapping_path)
                    endpoint_summary.append(method_summary)
        return endpoint_summary

    

    




    