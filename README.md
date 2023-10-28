# protonpass-deduplicate-secrets
Help with deduplicating your protonpass secrets, especially if you accidentially uploaded the same secrets twice.

This process is about unzipping the ProtonPass vault and eliminating duplicated items, then re-zipping it again. The objective is to remove any existing duplicate entries to streamline the data present in the vault. After processing, the cleaned vault can be re-uploaded to ProtonPass.

The tool reads the vault's JSON file, finds and removes duplicates based on the names of items, then writes the deduplicated vault data back into a new JSON file.

### Process Overview
1. Unzip the ProtonPass vault downloaded from ProtonPass.
2. Run the deduplication script on the downloaded file. This will generate a new JSON file with deduplicated items.
3. Replace the original data.json in the ProtonPass vault with the newly generated deduplicated_output.json.
4. Re-zip the contents of the ProtonPass vault.
5. Upload the cleaned zip file back to ProtonPass.

## Instructions

```bash
Proton Pass/> python dedupe.py
```

## Implementation Details

The `deduplicate` function reads the data JSON file provided as the first parameter (in this case 'data.json'), and writes the deduplicated output to a new JSON file specified as the second parameter (in this case 'deduplicated_output.json'). The function returns statistics about the original count of items, the number of deduplicated items, and the number of duplicates found.

## Notes
`deduplicated_output.json` should replace the `data.json` in the unzipped directory. 

Be careful not to lose any data when swapping and try keeping a backup of the original file before running the deduplication script. Always verify that the output data is correct before deleting any backups. 

## Warnings
This tool parses the entire vault. As such, performance may vary based on the size of your vault.

