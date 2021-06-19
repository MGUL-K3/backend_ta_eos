# TODO Refactor


def string_to_int(string: str) -> int:
    return int("0b" + string, 2)


def int_to_bin_string(value: int) -> str:
    return str(bin(value))[2:]


def generate_obj(value: str, bin_dec: str, index: int) -> dict:
    seq_obj = {"index": index, "bin_dec": bin_dec, "value": value}
    if bin_dec == "0":
        seq_obj["value"] = "0" * len(value)

    return seq_obj


def generate_final_obj(f_value: str, s_value: str):
    int_f_value = string_to_int(f_value)
    int_s_value = string_to_int(s_value)
    value = int_to_bin_string(int_f_value * int_s_value)
    return {"index": None, "bin_dec": None, "value": value}


def generate_seq_of_objects(f_value: str, s_value: str):
    seq = []
    for bin_dec, index in zip(reversed(s_value), range(len(s_value))):
        seq += [generate_obj(f_value, bin_dec, index)]

    seq += [generate_final_obj(f_value, s_value)]
    return seq


def generate_seq_of_objects_r(f_value: str, s_value: str):
    seq = []
    for bin_dec, index in zip(s_value, range(1, len(s_value) + 1)):
        seq += [generate_obj("0" * index + f_value, bin_dec, index)]

    seq += [generate_final_obj(f_value, s_value)]
    return seq
