# Run in assets/minecraft/models/item

import json
import os

to_convert = input("File to create definitions of: ")

def createDefinition(input):
    namespace = "minecraft"
    model = None
    try:
        namespace, model = input.split(":")
    except Exception as _:
        model = input
        pass
    path = f"../../../{namespace}/items/{model}"
    print("Creating for", model, "at", namespace)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path+".json", 'x') as out:
        out.write(json.dumps({
            "model": {
                "type": "minecraft:model",
                "model": input
            }
        }, indent=4))


with open(to_convert, 'r', encoding='utf-8') as f:
    contents = json.load(f)
    if not 'overrides' in contents:
        print("Nope")
        exit()
    for override in contents.get('overrides'):
        try:
            model = override.get("model")
            createDefinition(model)
        except Exception as e:
            print("Error while processing", override)
            print(e)

input()