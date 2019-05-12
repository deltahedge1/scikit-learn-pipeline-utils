# Helpful package for custom transformers to use in sklearn pipelines

## Installation
`pip install -i https://test.pypi.org/simple/ scikit-learn-pipeline-utils`

## Quick Start
```
from sklearn_pipeline_utils import DFSelector
from sklearn.pipeline import Pipeline
import pandas as pd

df = pd.DataFrame({
    "col1": ["a", "b", "a"],
    "col2": [1, 2, 3]
})

pipeline = Pipeline([
    ("dfselectcol1", DFSelector("col1"))
    ])

print(pipeline.transform(df))
```

## Dataframe Transformers List
1. DFSelector
2. DFObjectSelector
3. DFFeatureUnion
4. DFImputer
5. DFImputerMostFrequent
6. DFOrdinalEncoder
7. DFStandardScaler 