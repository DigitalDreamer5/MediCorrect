def translate_terms(text: str) -> str:
	if not isinstance(text, str):
		return text

	dictionary = {
		"bukhar": "fever",
		"khasi": "cough",
		"dil ghabra raha hai": "palpitations",
		"sar dard": "headache",
		"zukaam": "common cold",
		"gala dukh raha hai": "sore throat",
		"saans phool rahi hai": "shortness of breath (dyspnea)",
		"pet dard": "abdominal pain",
		"dast": "diarrhea",
		"ulti": "vomiting",
		"chakkar aa raha hai": "dizziness / vertigo",
		"kamzori": "fatigue / weakness",
		"jodo me dard": "joint pain (arthralgia)",
		"peshab jal raha hai": "burning urination (dysuria)",
		"peth phool raha hai": "bloating",
		"seene me jalan": "heartburn / acid reflux",
		"seene me dard": "chest pain",
		"kaan dard": "ear pain (otalgia)",
		"aankh lal hai": "eye redness (conjunctivitis)",
		"nakh se khoon": "nosebleed (epistaxis)",
		"gabrahat": "anxiety / restlessness",
		"ghabrahat ho rahi hai": "anxiety episode",
		"garmi lag rahi hai": "hot flashes",
		"sardi lag rahi hai": "chills",
		"pair sujan": "leg swelling (edema)",
		"chehre par daane": "acne / skin lesions",
		"khujli": "itching (pruritus)",
		"daant dard": "toothache",
		"pith dard": "back pain",
		"gud me jalan": "rectal burning",
		"gud me khujli": "anal itching (pruritus ani)",
		"hath pair sunn": "numbness / tingling"
	}

	txt = text.lower()
	for local_term, clinical_term in dictionary.items():
		txt = txt.replace(local_term, clinical_term)

	return txt
