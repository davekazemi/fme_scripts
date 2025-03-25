
import json
import os
from typing import Optional, Dict, Union, Any
from enum import Enum



class Action(Enum):
    SET = 'Set Custom Metadata'
    GET = 'Get Custom Metadata'
    REMOVE = 'Remove Custom Metadata'

class Method(Enum):
    ALL = 'All'
    JUST_KEY = 'Justkey'
    
class MetadataManager_ADS:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def set_custom_metadata_key(self, key: str, value: str):
        if not self.file_path or not key:
            raise ValueError("file_path and key must not be empty")
        metadata=self.get_custom_metadata()
        if metadata is None:
            metadata={}
        else:
            # convert text metadata like '{"test":"test"}' to a dict
            if type(metadata) is str:
                try:                    
                    metadata=json.loads(metadata.replace("'", '"'))
                    
                
                except Exception as e:
                    print(f"Error converting metadata to dict: {e}")
                    raise e
                
        metadata[key]=value
        self.set_custom_metadata(metadata)
    
    def get_custom_metadata_key(self, key:str):
        metadata=self.get_custom_metadata()
        if metadata is None:
            return None
        if type(metadata) is str:
            metadata=json.loads(metadata)
        return metadata.get(key,None)

    def set_custom_metadata(self, metadata: Union[str, Dict[str, Any]]) -> None:

        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist")
            return
        try:
            cs_file_path=f"{self.file_path}:custom_metadata"
            with open(cs_file_path, "w") as f:
                if type(metadata) is str:
                    f.write(metadata)
                else:
                    txtmetadata=json.dumps(metadata)
                    f.write(txtmetadata)
        except Exception as e:
            print(f"Error setting custom metadata for {self.file_path}: {e}")

    def get_custom_metadata(self) -> Optional[str]:
        try:
            cs_file_path=f"{self.file_path}:custom_metadata"
            if os.path.exists(cs_file_path):
                with open(cs_file_path, "r") as f:
                    txtmetadata = f.read()
                    if txtmetadata:

                        return str(txtmetadata)
            else:
                return None
        except Exception as e:
            print(f"Error getting custom metadata for {file_path}: {e}")
            return None

    def remove_custom_metadata(self):
        try:
            cs_file_path=f"{self.file_path}:custom_metadata"
            if os.path.exists(cs_file_path):
                os.remove(cs_file_path)
        except Exception as e:  
            print(f"Error removing custom metadata for {file_path}: {e}")


class Metadatamanager_JSON:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.metadata_json_path =os.path.join(os.path.dirname(file_path),f'{os.path.splitext(os.path.basename(file_path))[0]}_metadata_.json')

    def set_custom_metadata_key(self, key: str, value: str):
        try:
            metadata=self.get_custom_metadata()
            if metadata is None:
                metadata={}
            metadata[key]=value
            self.set_custom_metadata(metadata)
        except Exception as e:
            print(f"Error setting custom metadata for {self.file_path}: {e}")

    def get_custom_metadata_key(self, key: str):
        try:
            metadata=self.get_custom_metadata()
            if metadata is None:
                return None
            return metadata.get(key,None)
        except Exception as e:
            print(f"Error getting custom metadata for {self.file_path}: {e}")
            return None

    def set_custom_metadata(self, metadata: Dict[str, Any]):
        try:
            with open(self.metadata_json_path, "w") as f:
                json.dump(metadata, f)
        except Exception as e:
            print(f"Error setting custom metadata for {self.file_path}: {e}")
    
    def get_custom_metadata(self):
        metadata={}
        try:
            if os.path.exists(self.metadata_json_path):
                with open(self.metadata_json_path, "r") as f:
                    metadata=json.load(f)
        except Exception as e:
            print(f"Error getting custom metadata for {self.file_path}: {e}")
            return None
        return metadata

    def remove_custom_metadata(self):
        try:
            if os.path.exists(self.metadata_json_path):
                os.remove(self.metadata_json_path)
        except Exception as e:
            print(f"Error removing custom metadata for {self.file_path}: {e}")
            
            

if __name__ == "__main__":
    metadata_manager = Metadatamanager_JSON("C:\\TEMP\\corect.bcnv")
    metadata_manager.set_custom_metadata_key("test", "test")
    print(metadata_manager.get_custom_metadata_key("test")) # should print test
    metadata_manager.remove_custom_metadata()
    print(metadata_manager.get_custom_metadata_key("test")) # should print None 
    metadata_manager.set_custom_metadata_key("test", "test")
    print(metadata_manager.get_custom_metadata_key("test")) # should print test
    metadata_manager.remove_custom_metadata()
    print(metadata_manager.get_custom_metadata_key("test")) # should print None     
    metadata_manager.set_custom_metadata({"test": "test"})
    print(metadata_manager.get_custom_metadata_key("test")) # should print test
    metadata_manager.remove_custom_metadata()
    print(metadata_manager.get_custom_metadata_key("test")) # should print None 
    metadata_manager.set_custom_metadata('{"test":"test"}')
    print(metadata_manager.get_custom_metadata_key("test")) # should print test
    metadata_manager.remove_custom_metadata()
    metadata_manager.set_custom_metadata("{'test':'test'}")
    print(metadata_manager.get_custom_metadata()) # should print {"test":"test"}
    
        




