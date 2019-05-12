from sklearn_pipeline_utils import DFSelector
from sklearn.pipeline import Pipeline
import pandas as pd

df = pd.DataFrame({
    'col1': ['a', 'b', 'a'],
    'col2': [1, 2, 3]
})

def test_dfselector():
    
    df_col1 = pd.DataFrame(df['col1'], index=df.index)
    
    pipeline = Pipeline([
        ('dfselectcol1', DFSelector('col1'))
    ])

    expected_result = pipeline.transform(df)
    
    pipeline2 = Pipeline([
        ('dfselectcol1', DFSelector(['col1', 'col2']))
    ])

    expected_result2 = pipeline2.transform(df)

    assert (df_col1.equals(expected_result))
    assert (df.equals(expected_result2))