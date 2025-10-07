from doit_local.common import output_base
from doit_local.common import get_target_bin_path_name

from doit import get_initial_workdir
from doit.tools import Interactive


def param_target() -> dict:
    return {'name': 'target',
            'long': 'target',
            'type': str,
            'default': ''}


def task_run_ut():
    cmd = {
        'actions': [
            f'bazel {output_base} test --test_output=all //src/...'
        ],
        'verbosity': 2,
    }
    return cmd


def task_build_and_run_target():

    def build_target(target: str) -> str:
        return str(f"bazel {output_base} build {target}")

    def run_target(target: str) -> str:
        return str(f"./bazel-bin/{get_target_bin_path_name(target)}")

    cmd = {
        'params': [
            param_target(),
        ],
        'actions': [
            Interactive(build_target),
            Interactive(run_target),
        ],
        'verbosity': 2,
    }
    return cmd


def task_cleanup():
    cmd = {
        'actions': [
            'rm -rfd ./doit_out',
            'rm -rfd ./bazel-bin',
            'rm -rfd ./bazel-fda_containers',
            'rm -rfd ./bazel-out',
            'rm -rfd ./bazel-testlogs',
            'rm -rfd .doit.db',
            'rm -rfd __pycache__',
            'rm -rfd doit_local/__pycache__',
        ]
    }
    return cmd
