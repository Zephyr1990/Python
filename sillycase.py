def sillycase(new_word):
	how_long = len(silly)
	half = int(round(length/2.0))
	lower_half = silly[:half].lower()
	upper_half = silly[half:].upper()
	return lower_half + upper_half