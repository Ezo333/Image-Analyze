import os
import hashlib
import json

def get_cache_file(cache_type):
    if cache_type == 'document':
        return 'app/cache_document.json'
    elif cache_type == 'image':
        return 'app/cache_image.json'
    else:
        return 'app/cache.json'

def delete_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file: {e}")

def get_image_hash(image_path):
    hasher = hashlib.sha256()
    with open(image_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def load_cache(cache_type):
    cache_file = get_cache_file(cache_type)
    try:
        with open(cache_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_cache(cache, cache_type):
    cache_file = get_cache_file(cache_type)
    with open(cache_file, 'w') as f:
        json.dump(cache, f)

def get_cached_result(image_path, cache_type):
    image_hash = get_image_hash(image_path)
    cache = load_cache(cache_type)
    return cache.get(image_hash)

def set_cached_result(image_path, result, cache_type):
    if result.get("error"):
        return
    image_hash = get_image_hash(image_path)
    cache = load_cache(cache_type)
    cache[image_hash] = result
    save_cache(cache, cache_type)