import kfp


def merge_csv():
    import pandas as pd

    s = pd.Series([4, 2, 0, 8], name='legs')
    print(s.sum())

    print("DONE PIPE")


create_step_merge_csv = kfp.components.create_component_from_func(
    func=merge_csv,
    output_component_file='sample__component.yaml',  # This is optional. It saves the component spec for future use.
    base_image='python:3.7',
    packages_to_install=['pandas==1.1.4'])
