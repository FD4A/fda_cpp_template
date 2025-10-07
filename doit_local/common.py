output_path="/mnt/nvme/VScode/fda_containers/doit_out"
output_base=f"--output_base={output_path}"

def get_target_bin_path_name(target: str) -> str:
    """ input - //src/ut:test2
        output - /src/ut/test2
    """
    return target.replace(':','/')[2:]