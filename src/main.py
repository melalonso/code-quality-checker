from src.postprocessor import postprocess
from src.preprocessor import preprocess

if __name__ == '__main__':
    project_names = preprocess()  # Returns list of downloaded and analyzed projects
    postprocess(project_names)  # Uses static analyzers results to train deep learning models
