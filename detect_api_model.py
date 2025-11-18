

 import os
 import logging
 import threading
 from transformers import pipeline
 from transformers.utils import logging as hf_logging


# # ----------------------------
 Silence transformers / torch / tf logs
# # ----------------------------
 hf_logging.set_verbosity_error()
 os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
 logging.getLogger().setLevel(logging.ERROR)


# # ----------------------------
# # Lazy, thread-safe model loader (DistilBERT fast replacement)
# # ----------------------------
 _detector = None
 _lock = threading.Lock()


 # You can change this to another fast model if you prefer
_DEFAULT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"


# def get_detector(model_name: str = _DEFAULT_MODEL, device: int = -1):
 	"""Return a singleton pipeline instance. device=-1 forces CPU; 0 for first GPU."""
 	global _detector
 	with _lock:
 		if _detector is None:
 			print(f"⚡ Loading model: {model_name} (this may take a moment)...")
 			_detector = pipeline(
 				"text-classification",
 				model=model_name,
 				tokenizer=model_name,
 				device=device,
 				top_k=1
 			)
 			print("✅ Model loaded!")
 		return _detector


 def detect_health_claim(text: str):
 	model = get_detector()
 	# pipeline returns a list of dicts; we take the top label
 	outputs = model(text)
 	if isinstance(outputs, list) and len(outputs) > 0:
 		return outputs[0].get("label")

# fallback
	return None
