import json
import yaml
import requests


def load_json_or_yaml(file_path):
    """Load either json or yaml document from file path or url or JSON doc

    :param: file_path: The path of the url doc, could be url or file path
    """
    # handle json doc
    if isinstance(file_path, dict):
        return file_path
    # handle url
    elif file_path.startswith("http"):
        with requests.get(file_path) as url:
            # check if http requests returns a success status code
            if url.status_code != 200:
                raise ValueError("Invalid URL!")
            else:
                _data = url.content
    # handle file path
    else:
        try:
            with open(file_path) as f:
                _data = f.read()
        except FileNotFoundError:
            raise ValueError("Invalid File Path!")
    try:
        if type(_data) == bytes:
            _data = _data.decode('utf-8')
        data = json.loads(_data)
    except json.JSONDecodeError:   # for py>=3.5
    # except ValueError:               # for py<3.5
        try:
            data = yaml.load(_data, Loader=yaml.SafeLoader)
        except (yaml.scanner.ScannerError,
                yaml.parser.ParserError):
            raise ValueError("Not a valid JSON or YAML format.")
    return data