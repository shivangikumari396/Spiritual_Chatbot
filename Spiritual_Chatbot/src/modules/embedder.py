import os
import pickle
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS

class Embedder:

    def __init__(self):
        self.PATH = "embeddings"
        self.createEmbeddingsDir()

    def createEmbeddingsDir(self):
        if not os.path.exists(self.PATH):
            os.mkdir(self.PATH)

    def storeDocEmbeds(self, file_path, original_filename):
        loader = CSVLoader(file_path=file_path, encoding="utf-8", csv_args={'delimiter': ','})
        data = loader.load()
        # Store CSV data or process it as needed
        with open(f"{self.PATH}/{original_filename}.pkl", "wb") as f:
            pickle.dump(data, f)

    def getDocEmbeds(self, file_path, original_filename):
        if not os.path.isfile(f"{self.PATH}/{original_filename}.pkl"):
            self.storeDocEmbeds(file_path, original_filename)
        with open(f"{self.PATH}/{original_filename}.pkl", "rb") as f:
            vectors = pickle.load(f)
        return vectors
