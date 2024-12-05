import json

to_convert = input("File to convert: ")
output_file = input("Output file: ")

result = {
    "model": {
        "type": "minecraft:range_dispatch",
        "property": "minecraft:custom_model_data",
        "index": 0
    }
}

entries = []

with open(to_convert, 'r', encoding='utf-8') as f:
    contents = json.load(f)
    for override in contents.get('overrides'):
        try:
            model = override.get("model")
            cmd = override.get("predicate").get("custom_model_data")
            entry = {
                "threshold": cmd,
                "model": {
                    "type": "minecraft:model",
                    "model": model
                }
            }
            entries.append(entry)
        except Exception as _:
            print("Error while processing", override)

result['model']['entries'] = entries

with open(output_file, 'x') as outfile:
    outfile.write(json.dumps(result, indent=4))

print(f'Finished with {len(entries)} models')
input()
