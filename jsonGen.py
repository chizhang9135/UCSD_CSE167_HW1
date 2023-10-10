import json
import copy

def generate_interpolated_jsons(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    OFFSET = 5
    max_steps = 0

    # Determine the maximum steps required for all transformations
    for obj in data["objects"]:
        if "transform" in obj:
            for transform in obj["transform"]:
                for _, value in transform.items():
                    if isinstance(value, list):
                        for v in value:
                            steps = abs(v) // OFFSET
                            if steps > max_steps:
                                max_steps = steps
                    elif isinstance(value, (int, float)):
                        steps = abs(value) // OFFSET
                        if steps > max_steps:
                            max_steps = steps

    for step in range(1, max_steps + 1):
        new_data = copy.deepcopy(data)

        for obj in new_data["objects"]:
            if "transform" in obj:
                for transform in obj["transform"]:
                    for key, value in transform.items():
                        if isinstance(value, list):
                            for i, v in enumerate(value):
                                if v > 0:
                                    transform[key][i] = min(v, OFFSET * step)
                                else:
                                    transform[key][i] = max(v, -OFFSET * step)
                        elif isinstance(value, (int, float)):
                            if value > 0:
                                transform[key] = min(value, OFFSET * step)
                            else:
                                transform[key] = max(value, -OFFSET * step)

        with open(filename.split('.')[0] + f'_{step}.json', 'w') as f:
            json.dump(new_data, f, indent=4)


if __name__ == "__main__":
    generate_interpolated_jsons("dir/file.json")
