"""
Tests for new NLP features (Morphology, Language ID, NER).
"""
import pytest
from morphology import analyze_morphology
from language_identifier import identify_languages
from ner import extract_entities
from english_validation import validate_english_pos
from rule_tagger import RuleBasedTagger

def test_morphology():
    tokens = ["मित्राने", "dog-ne", "kela"]
    # Dummy pos results just to simulate context
    pos_results = [{"token": "मित्राने", "tag": "NOUN"}, 
                   {"token": "dog-ne", "tag": "NOUN"},
                   {"token": "kela", "tag": "VERB"}]
    
    res = analyze_morphology(tokens, pos_results)
    
    assert len(res) == 3
    # Check fused suffix logic fallback (might not catch मित्राने precisely without Marathi dictionary, 
    # but let's check it doesn't crash)
    assert res[0]["Token"] == "मित्राने"
    
    # Check hyphenated case logic
    assert res[1]["Token"] == "dog-ne"
    assert res[1]["Root"] == "dog"
    assert res[1]["Suffix"] == "-ne"
    assert res[1]["Case"] == "Oblique/Marker"
    
    # Check light verb
    assert res[2]["Token"] == "kela"
    assert res[2]["Other"] == "Light Verb + Past Tense"

def test_language_identifier():
    tokens = ["मी", "आज", "college", "मध्ये", "assignment", "complete", "केला", "."]
    res = identify_languages(tokens)
    
    assert res["stats"]["Total Tokens"] == 8
    
    langs = {r["Token"]: r["Language"] for r in res["results"]}
    assert langs["मी"] == "Marathi"
    assert langs["आज"] == "Marathi"
    assert langs["college"] == "English"
    assert langs["मध्ये"] == "Marathi"
    assert langs["assignment"] == "English"
    assert langs["complete"] == "English"
    assert langs["केला"] == "Marathi"
    assert langs["."] == "Other"

def test_ner():
    tokens = ["मी", "काल", "mumbai", "ला", "गेलो", "आणि", "तिथे", "tcs", "मध्ये", "interview", "दिला", "."]
    entities = extract_entities(tokens)
    
    assert len(entities) >= 2
    
    locs = [e["Entity"] for e in entities if e["Entity Type"] == "LOCATION"]
    orgs = [e["Entity"] for e in entities if e["Entity Type"] == "ORGANIZATION"]
    
    assert "mumbai" in locs
    assert "tcs" in orgs

def test_english_validation():
    ensemble_results = [
        {"token": "morning", "tag": "VERB", "source": "hmm"},
        {"token": "sun", "tag": "NOUN", "source": "hmm"}
    ]
    res = validate_english_pos(ensemble_results)
    
    assert len(res) == 2
    # 'morning' as VERB should be contradicted by WordNet NOUN evidence
    assert res[0]["Token"] == "morning"
    assert res[0]["Ensemble POS"] == "VERB"
    assert "NOUN" in res[0]["WordNet Evidence"]
    # Expect Validated POS to be corrected (probably to NOUN)
    assert res[0]["Validated POS"] != "VERB"
    assert res[0]["Validated POS"] == "NOUN"
    
    # 'sun' as NOUN should be accepted
    assert res[1]["Token"] == "sun"
    assert res[1]["Ensemble POS"] == "NOUN"
    assert res[1]["Validated POS"] == "NOUN"
