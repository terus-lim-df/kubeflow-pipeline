#!/usr/bin/env python3

import kfp
from kfp.components import func_to_container_op, InputPath, OutputPath
import_op = kfp.components.load_component_from_url("https://raw.githubusercontent.com/terus-lim-df/kubeflow-pipeline/main/sample__component.yaml")


# Combining all pipelines together in a single pipeline
def file_passing_pipelines():
    import_op()


if __name__ == '__main__':
    # Compiling the pipeline
    kfp.compiler.Compiler().compile(file_passing_pipelines, "yaml/" + __file__.split("/")[-1] + '.yaml')
