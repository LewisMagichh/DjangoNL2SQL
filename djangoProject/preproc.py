import json
import _jsonnet
import attr
import os
import sys
from djangoProject.nltsql.ratsql.commands import infer
from djangoProject.settings import BASE_DIR

@attr.s
class PreprocessConfig:
    config = attr.ib()
    config_args = attr.ib()

@attr.s
class TrainConfig:
    config = attr.ib()
    config_args = attr.ib()
    logdir = attr.ib()

@attr.s
class InferConfig:
    config = attr.ib()
    config_args = attr.ib()
    logdir = attr.ib()
    section = attr.ib()
    beam_size = attr.ib()
    output = attr.ib()
    step = attr.ib()
    use_heuristic = attr.ib(default=False)
    mode = attr.ib(default="infer")
    limit = attr.ib(default=None)
    output_history = attr.ib(default=False)

@attr.s
class EvalConfig:
    config = attr.ib()
    config_args = attr.ib()
    logdir = attr.ib()
    section = attr.ib()
    inferred = attr.ib()
    output = attr.ib()

def proprection():
    exp_config_file = os.path.join(BASE_DIR,'djangoProject/nltsql/experiments/spider-glove-run.jsonnet')
    exp_config = json.loads(_jsonnet.evaluate_file(exp_config_file))
    model_config_file = exp_config["model_config"]

    model_config_args = exp_config["model_config_args"]
    model_config_args = json.dumps(model_config_args)

    logdir =exp_config["logdir"]

    step = 33100
    infer_output_path = f"{exp_config['eval_output']}/{exp_config['eval_name']}-step{step}.infer"
    infer_config = InferConfig(
        model_config_file,
        model_config_args,
        logdir,
        exp_config["eval_section"],
        exp_config["eval_beam_size"],
        infer_output_path,
        step,
        use_heuristic=exp_config["eval_use_heuristic"]
    )
    infer.main(infer_config)