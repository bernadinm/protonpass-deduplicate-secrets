import json

def deduplicate(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Invalid data structure.")

    vaults = data.get('vaults', {})
    if not vaults:
        raise ValueError("No vaults found for deduplication.")

    seen_names = set()
    duplicate_count = 0
    total_original_count = 0

    for vault_name, vault_data in vaults.items():
        items = vault_data.get('items', [])
        total_original_count += len(items)
        deduplicated_items = []
        for record in items:
            item_name = record['data']['metadata']['name']
            if item_name not in seen_names:
                seen_names.add(item_name)
                deduplicated_items.append(record)
            else:
                duplicate_count += 1
        vault_data['items'] = deduplicated_items  # Update the items list with deduplicated items

    deduplication_stats = {
        "original_count": total_original_count,
        "deduplicated_count": total_original_count - duplicate_count,
        "duplicate_count": duplicate_count
    }

    # Saving deduplicated data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    return deduplication_stats

# Call the function with the path to your JSON file and specify the output file name
stats = deduplicate('data.json', 'deduplicated_output.json')
print(stats)
