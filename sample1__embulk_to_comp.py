import kfp
import os


# /home/minikf/embulk/./try1/csv/sample_
def read_csv(i_file):
    os.system('export i_file=' + i_file + '; embulk run /path_to_liquid_file/load_sample.yml.liquid')


create_step_merge_csv = kfp.components.create_component_from_func(
    func=read_csv,
    output_component_file='sample1__embulk_component.yaml',  # This is optional. It saves the component spec for future use.
    base_image='python:3.7')
