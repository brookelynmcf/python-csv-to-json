import csv
import json

file = open('../DrugDosing.csv', 'r')
json_file = open('../DrugDosing.json', 'w')

# include_cols = ["Drug", "US Black Box", "Contraindications", "Special Precautions", "ISMP High Alert", "Additional Adverse Reactions"]
reader = csv.DictReader(file)
tmpDict = {}
for row in reader:
   # tmpdict = (row['Drug'], row['US Black Box'], row['Contraindications'], row['Special Precautions'], row['ISMP High Alert'], row['Additional Adverse Reactions'])
   tmpDict["Drug"] = row["Drug"]
   tmpDict["USBlackBox"] = row["US Black Box"]
   tmpDict["Contraindications"] = row["Contraindications"]
   tmpDict["SpecialPrecautions"] = row["Special Precautions"]
   tmpDict["ISMP"] = row["ISMP High Alert"]
   tmpDict["AdditionalAdverseReactions"] = row["Additional Adverse Reactions"]
   json.dump(tmpDict, json_file)
print("Your file is ready")
