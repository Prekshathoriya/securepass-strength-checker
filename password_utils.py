from zxcvbn import zxcvbn
import random
import string

# Analyze password strength
def check_password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # 0 = weak, 4 = very strong
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    feedback = result['feedback']
    suggestions = feedback.get('suggestions', [])
    warning = feedback.get('warning', '')

    return {
        'score': score,
        'crack_time': crack_time,
        'suggestions': suggestions,
        'warning': warning
    }

# Generate a strong passphrase
def generate_strong_passphrase(length=4):
    words = ["secure", "cloud", "fortress", "dragon", "galaxy", "matrix", "hunter", "shadow"]
    return '-'.join(random.choices(words, k=length))

# Generate a random complex password
def generate_complex_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))
